import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

from src.miner import _parse_date, JobScraper


def _el(text=''):
    """Mock Selenium WebElement with a text property."""
    m = MagicMock()
    m.text = text
    return m


def _link(href):
    """Mock anchor element whose get_attribute('href') returns href."""
    m = MagicMock()
    m.get_attribute.return_value = href
    return m


class TestParseDate(unittest.TestCase):

    def test_dd_mm_yyyy(self):
        self.assertEqual(_parse_date('01/01/2024'), datetime(2024, 1, 1))

    def test_iso_format(self):
        self.assertEqual(_parse_date('2024-06-15'), datetime(2024, 6, 15))

    def test_posted_prefix_short_month(self):
        self.assertEqual(_parse_date('Posted Jun 15, 2026'), datetime(2026, 6, 15))

    def test_closing_prefix_dd_mm_yyyy(self):
        self.assertEqual(_parse_date('Closing 15/07/2026'), datetime(2026, 7, 15))

    def test_added_prefix(self):
        self.assertEqual(_parse_date('Added 01/03/2025'), datetime(2025, 3, 1))

    def test_closes_prefix(self):
        self.assertEqual(_parse_date('Closes 31/12/2025'), datetime(2025, 12, 31))

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(_parse_date('  Posted Jun 15, 2026  '), datetime(2026, 6, 15))

    def test_unrecognized_text_returns_none(self):
        self.assertIsNone(_parse_date('not a date'))

    def test_empty_string_returns_none(self):
        self.assertIsNone(_parse_date(''))

    def test_unknown_prefix_returns_none(self):
        # 'Expires' is not in _DATE_PREFIXES, so text is not stripped and fails all formats
        self.assertIsNone(_parse_date('Expires 01/01/2024'))


class TestJobScraper(unittest.TestCase):

    def setUp(self):
        self.chrome_patcher = patch('src.miner.webdriver.Chrome')
        self.wait_patcher = patch('src.miner.WebDriverWait')
        self.mock_chrome_cls = self.chrome_patcher.start()
        self.mock_wait_cls = self.wait_patcher.start()

        self.mock_driver = MagicMock()
        self.mock_chrome_cls.return_value = self.mock_driver
        # WebDriverWait(...).until(...) returns immediately without blocking
        self.mock_wait_cls.return_value.until.return_value = None

    def tearDown(self):
        self.chrome_patcher.stop()
        self.wait_patcher.stop()

    # ------------------------------------------------------------------ #
    # collect_job_urls                                                     #
    # ------------------------------------------------------------------ #

    def test_collect_returns_discovered_urls(self):
        self.mock_driver.find_elements.return_value = [
            _link('https://www.myjob.mu/job/123/foo')
        ]
        scraper = JobScraper([])
        result = scraper.collect_job_urls()
        self.assertEqual(result, ['https://www.myjob.mu/job/123/foo'])

    def test_collect_excludes_already_scraped_urls(self):
        existing = 'https://www.myjob.mu/job/123/foo'
        self.mock_driver.find_elements.return_value = [_link(existing)]
        scraper = JobScraper([existing])
        self.assertEqual(scraper.collect_job_urls(), [])

    def test_collect_ignores_non_job_hrefs(self):
        self.mock_driver.find_elements.return_value = [
            _link('https://www.myjob.mu/companies/5/acme'),
            _link('https://www.myjob.mu/job/99/valid-job'),
            _link(None),
        ]
        scraper = JobScraper([])
        result = scraper.collect_job_urls()
        self.assertEqual(result, ['https://www.myjob.mu/job/99/valid-job'])

    def test_collect_matches_url_without_trailing_slash(self):
        # regression: old regex r'/job/\d+/' required trailing slash
        self.mock_driver.find_elements.return_value = [
            _link('https://www.myjob.mu/job/99534')
        ]
        scraper = JobScraper([])
        self.assertIn('https://www.myjob.mu/job/99534', scraper.collect_job_urls())

    def test_collect_does_not_scroll_when_limit_met_on_first_batch(self):
        self.mock_driver.find_elements.return_value = [
            _link('https://www.myjob.mu/job/1/a'),
            _link('https://www.myjob.mu/job/2/b'),
            _link('https://www.myjob.mu/job/3/c'),
        ]
        scraper = JobScraper([], limit=2)
        scraper.collect_job_urls()
        # _scroll_to_bottom calls execute_script; it should not be called
        # because the limit was already met after the first batch
        self.mock_driver.execute_script.assert_not_called()

    # ------------------------------------------------------------------ #
    # scrape_job_page                                                      #
    # ------------------------------------------------------------------ #

    def test_scrape_job_page_extracts_all_fields(self):
        self.mock_driver.find_element.side_effect = [
            _el('Software Engineer'),           # h3 — job title
            _el(''),                            # a[href*="/companies/"] span (text via JS)
            _el('Full-time'),                   # span.rounded-lg — employment type
            _el('Job Description\nWe need a developer.'),  # //h4[...]/../..
        ]
        self.mock_driver.execute_script.return_value = 'Acme Corp'
        self.mock_driver.find_elements.return_value = [
            _el('Moka'),
            _el('Not disclosed'),
            _el('Posted Jun 15, 2026'),
            _el('Closing 15/07/2026'),
        ]

        scraper = JobScraper([])
        job = scraper.scrape_job_page('https://www.myjob.mu/job/1/foo')

        self.assertEqual(job.job_title, 'Software Engineer')
        self.assertEqual(job.company, 'Acme Corp')
        self.assertEqual(job.employment_type, 'Full-time')
        self.assertEqual(job.location, 'Moka')
        self.assertEqual(job.salary, 'Not disclosed')
        self.assertEqual(job.date_posted, datetime(2026, 6, 15))
        self.assertEqual(job.closing_date, datetime(2026, 7, 15))
        self.assertIn('developer', job.job_details)

    def test_scrape_job_page_sets_url(self):
        self.mock_driver.find_element.side_effect = NoSuchElementException()
        self.mock_driver.find_elements.return_value = []

        url = 'https://www.myjob.mu/job/42/test-job'
        scraper = JobScraper([])
        job = scraper.scrape_job_page(url)

        self.assertEqual(job.url, url)

    def test_scrape_job_page_falls_back_to_unknown_company(self):
        self.mock_driver.find_element.side_effect = [
            _el('Some Job'),           # h3
            NoSuchElementException(),  # company span missing
            NoSuchElementException(),  # employment badge
            NoSuchElementException(),  # description xpath
            NoSuchElementException(),  # description fallback
        ]
        self.mock_driver.find_elements.return_value = []

        scraper = JobScraper([])
        job = scraper.scrape_job_page('https://www.myjob.mu/job/1/foo')

        self.assertEqual(job.company, 'Unknown')

    def test_scrape_job_page_missing_meta_items_leaves_defaults(self):
        self.mock_driver.find_element.side_effect = NoSuchElementException()
        self.mock_driver.find_elements.return_value = []

        scraper = JobScraper([])
        job = scraper.scrape_job_page('https://www.myjob.mu/job/1/foo')

        self.assertEqual(job.location, '')
        self.assertIsNone(job.date_posted)
        self.assertIsNone(job.closing_date)

    def test_scrape_job_page_partial_meta_items(self):
        self.mock_driver.find_element.side_effect = NoSuchElementException()
        # only location and salary present, no dates
        self.mock_driver.find_elements.return_value = [
            _el('Port Louis'),
            _el('Rs 50,000'),
        ]

        scraper = JobScraper([])
        job = scraper.scrape_job_page('https://www.myjob.mu/job/1/foo')

        self.assertEqual(job.location, 'Port Louis')
        self.assertEqual(job.salary, 'Rs 50,000')
        self.assertIsNone(job.date_posted)

    # ------------------------------------------------------------------ #
    # scrape                                                               #
    # ------------------------------------------------------------------ #

    def test_scrape_quits_driver_on_success(self):
        with patch.object(JobScraper, 'collect_job_urls', return_value=[]):
            JobScraper([]).scrape()
        self.mock_driver.quit.assert_called_once()

    def test_scrape_quits_driver_even_on_exception(self):
        # regression: driver.quit() must be in a finally block
        with patch.object(JobScraper, 'collect_job_urls',
                          return_value=['https://www.myjob.mu/job/1/foo']):
            with patch.object(JobScraper, 'scrape_job_page',
                              side_effect=RuntimeError('network error')):
                scraper = JobScraper([])
                with self.assertRaises(RuntimeError):
                    scraper.scrape()

        self.mock_driver.quit.assert_called_once()

    def test_scrape_returns_list_of_dicts(self):
        with patch.object(JobScraper, 'collect_job_urls',
                          return_value=['https://www.myjob.mu/job/1/foo']):
            self.mock_driver.find_element.side_effect = [
                _el('Developer'),
                _el(''),
                _el('Full-time'),
                _el('Build great things.'),
            ]
            self.mock_driver.execute_script.return_value = 'Corp'
            self.mock_driver.find_elements.return_value = []

            result = JobScraper([]).scrape()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertIn('job_title', result[0])
        self.assertIn('url', result[0])

    def test_scrape_enforces_limit(self):
        urls = [f'https://www.myjob.mu/job/{i}/job' for i in range(5)]
        with patch.object(JobScraper, 'collect_job_urls', return_value=urls):
            with patch.object(JobScraper, 'scrape_job_page',
                              return_value=MagicMock()) as mock_scrape:
                JobScraper([], limit=3).scrape()

        self.assertEqual(mock_scrape.call_count, 3)
