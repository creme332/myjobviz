import {
  Container,
  Alert,
  Title,
  Text,
  Stack,
  Grid,
  Paper,
  Group,
  Badge,
  Divider,
  Box,
  Center,
  Loader,
  Tooltip,
  ActionIcon,
} from "@mantine/core";
import StatsGrid from "../components/graphs/StatsGrid";
import HorizontalBarChart from "../components/graphs/HorizontalBarChart";
import PieChart from "../components/graphs/PieChart";
import LineChart from "../components/graphs/LineChart";
import {
  IconAlertCircle,
  IconTrendingUp,
  IconInfoCircle,
} from "@tabler/icons-react";
import WordCloud from "../components/graphs/WordCloud";

export default function Results({ allData }) {
  if (!allData) {
    return (
      <Container mt={30}>
        <Center style={{ minHeight: "60vh" }}>
          <Stack align="center" spacing="lg">
            <Loader size="xl" variant="bars" />
            <Text size="lg" color="dimmed">
              Loading data...
            </Text>
          </Stack>
        </Center>
      </Container>
    );
  }

  const stats_grid_data = [
    {
      title: "Jobs scraped this month",
      stats: allData.metadata.job_count_this_month,
      description: "Number of jobs scraped since start of current month",
    },
    {
      title: "Last update",
      stats: date_diff_days(allData.metadata.last_update.toDate(), new Date()),
      description: "myjob.mu website is scraped on a daily basis",
    },
    {
      title: "Total jobs scraped",
      stats: allData.metadata.size,
      description: "Total number of jobs scraped from myjob.mu",
    },
  ];

  const chartTitle = {
    cloud_data: "Cloud platforms",
    db_data: "Databases",
    lang_data: "Programming, scripting, and markup languages",
    lib_data: "Other frameworks and libraries",
    loc_data: "Job locations",
    os_data: "Operating systems",
    salary_data: "Job salary",
    tools_data: "Other tools",
    web_data: "Web frameworks and technologies",
    job_trend_by_month: "Number of jobs scraped during last 6 months",
  };

  function date_diff_days(date1, date2) {
    const hours = parseInt(Math.abs(date1 - date2) / 36e5, 10);
    return `${hours} ${hours > 1 ? "hours" : "hour"} ago`;
  }

  function getLineChart() {
    /**
     * labelsArray must already be sorted by date. Smallest date first.
     * @param {string[]} labelsArray A list of strings with format YYYY-M-x or YYYY-MM-x
     * @returns A list of strings with year and month. Eg June 2023
     */
    function parseDate(labelsArray) {
      const allMonths = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      return labelsArray.map((el) => {
        const year = el.split("-")[0];
        const monthIndex = el.split("-")[1];
        return `${allMonths[monthIndex - 1]} ${year}`;
      });
    }

    const data = allData.job_trend_by_month;
    const [labelsArray, dataArray] = dictToArray(data, false, true);

    return (
      <Paper shadow="sm" p="xl" radius="md" withBorder>
        <Group position="apart" mb="md">
          <div>
            <Title order={3}>Job Market Trends</Title>
            <Text size="sm" color="dimmed" mt={5}>
              Monthly job posting volume over the last 6 months
            </Text>
          </div>
          <Badge
            size="lg"
            variant="light"
            color="blue"
            leftSection={<IconTrendingUp size={16} />}
          >
            6 Months
          </Badge>
        </Group>
        <LineChart
          title={chartTitle.job_trend_by_month}
          labelsArray={parseDate(labelsArray)}
          dataArray={dataArray}
        />
      </Paper>
    );
  }

  /**
   * Returns the keys and values of a dictionary as 2 separate arrays
   * @param {dict} dict Dictionary
   * @param {Boolean} sortByValue If true, arrays are sorted in ascending order of key value. If false, arrays are sorted in descending order of
   * @returns {[labelsArray, dataArray]}
   */
  function dictToArray(dict, sortByValue = true) {
    const labelsArr = Object.keys(dict);
    const dataArr = labelsArr.map((k) => dict[k]);

    // convert dict to an array of dictionaries where each array element
    // represents a key-value pair
    const arrayOfDict = labelsArr.map((d, i) => {
      return {
        key: d,
        data: parseInt(dataArr[i]) || 0,
      };
    });

    // sort array
    let sortedArrayOfDict;
    if (sortByValue) {
      // sort in descending order of values
      sortedArrayOfDict = arrayOfDict.sort(function (a, b) {
        return b.data - a.data;
      });
    } else {
      // sort in ascending order of keys
      sortedArrayOfDict = arrayOfDict.sort(function (a, b) {
        return a.key.localeCompare(b.key);
      });
    }

    // convert sorted array of dictionaries back to arrays
    const newLabelsArray = [];
    const newDataArray = [];

    sortedArrayOfDict.forEach(function (d) {
      newLabelsArray.push(d.key);
      newDataArray.push(d.data);
    });

    return [newLabelsArray, newDataArray];
  }

  function getWordCloud() {
    const data = allData.job_title_data;
    const keys = Object.keys(data);
    const words = [];
    for (const key of keys) {
      words.push({ text: key, value: data[key] });
    }

    return (
      <Paper shadow="sm" p="xl" radius="md" withBorder>
        <Stack spacing="md">
          <div>
            <Title order={3}>Job Title Keywords</Title>
            <Text size="sm" color="dimmed" mt={5}>
              Most frequently appearing keywords in job titles
            </Text>
          </div>
          <Box style={{ minHeight: 400 }}>
            <WordCloud words={words} />
          </Box>
        </Stack>
      </Paper>
    );
  }

  function getHorizontalBarcharts() {
    const horizonalBarChartKeys = [
      "cloud_data",
      "db_data",
      "lang_data",
      "lib_data",
      "tools_data",
      "web_data",
    ];

    const validKeys = Object.keys(allData).filter((k) =>
      horizonalBarChartKeys.includes(k)
    );

    return validKeys.map((k, index) => {
      const data = allData[k];
      const [labelsArray, dataArray] = dictToArray(data);

      return (
        <Paper
          key={`horizontal-barchart-${k}`}
          shadow="sm"
          p="xl"
          radius="md"
          withBorder
        >
          <Stack spacing="md">
            <div>
              <Title order={3}>{chartTitle[k]}</Title>
              <Text size="sm" color="dimmed" mt={5}>
                Frequency of mentions in job postings
              </Text>
            </div>
            <HorizontalBarChart
              dataArray={dataArray}
              labelsArray={labelsArray}
              dataLabel="Frequency"
              titleName={chartTitle[k]}
              themeIndex={index}
            />
          </Stack>
        </Paper>
      );
    });
  }

  function getPieCharts() {
    const pieChartKeys = ["loc_data", "os_data", "salary_data"];

    const validKeys = Object.keys(allData).filter((k) =>
      pieChartKeys.includes(k)
    );

    return validKeys.map((k) => {
      const data = allData[k];
      const [labelsArray, dataArray] = dictToArray(data);

      let tooltipText = null;
      let chartData = { labels: labelsArray, data: dataArray };

      if (k === "os_data") {
        tooltipText =
          "Not all jobs mention an operating system in the job description.";
      }

      if (k === "salary_data") {
        // merge "See description" and "not disclosed"
        const i = labelsArray.indexOf("See description");
        const newDataArray = [...dataArray];
        const newLabelArray = [...labelsArray];
        const SeeDescriptionCount = newDataArray.splice(i, 1)[0];
        const j = labelsArray.indexOf("Not disclosed");
        newDataArray[j] += SeeDescriptionCount;
        newLabelArray.splice(i, 1);
        chartData = { labels: newLabelArray, data: newDataArray };
        tooltipText =
          'Jobs posts which set the salary to "See description" were counted in the "Not disclosed" category.';
      }

      return (
        <Paper
          key={`piechart-${k}`}
          shadow="sm"
          p="xl"
          radius="md"
          withBorder
          style={{ height: "100%" }}
        >
          <Stack spacing="md" style={{ height: "100%" }}>
            <Group position="apart" noWrap>
              <div style={{ flex: 1 }}>
                <Title order={3}>{chartTitle[k]}</Title>
                <Text size="sm" color="dimmed" mt={5}>
                  Distribution across categories
                </Text>
              </div>
              {tooltipText && (
                <Tooltip
                  label={tooltipText}
                  multiline
                  width={220}
                  withArrow
                  position="left"
                  color="blue"
                >
                  <ActionIcon variant="subtle" color="blue" size="lg">
                    <IconInfoCircle size={20} />
                  </ActionIcon>
                </Tooltip>
              )}
            </Group>
            <Box style={{ flex: 1 }}>
              <PieChart
                dataArray={chartData.data}
                labelsArray={chartData.labels}
                titleName={chartTitle[k]}
              />
            </Box>
          </Stack>
        </Paper>
      );
    });
  }

  return (
    <Container size="xl" mt={30} mb={60}>
      <Stack spacing="xl">
        {/* Header Section */}
        <Box>
          <Title order={1} mb="xs">
            IT Job Market Insights
          </Title>
          <Text size="lg" color="dimmed">
            Comprehensive analysis of the Mauritian IT job market
          </Text>
        </Box>

        {/* Stats Grid */}
        <StatsGrid data={stats_grid_data} />

        {/* Disclaimer */}
        <Alert
          icon={<IconAlertCircle size="1rem" />}
          title="Data Disclaimer"
          color="orange"
          variant="light"
        >
          Please be aware that while efforts have been made to ensure accurate
          representation and meaningful interpretations, there is a possibility
          of misinterpretations or errors in the analysis. The conclusions drawn
          from the data should be approached with caution.
        </Alert>

        <Divider my="xl" />

        {/* Trends Section */}
        <Box>
          <Title order={2} mb="lg">
            Market Trends
          </Title>
          {getLineChart()}
        </Box>

        <Divider my="xl" />

        {/* Overview Section - Pie Charts */}
        <Box>
          <Title order={2} mb="lg">
            Market Overview
          </Title>
          <Grid gutter="lg">
            {getPieCharts().map((chart, index) => (
              <Grid.Col key={`pie-grid-${index}`} xs={12} md={6} lg={4}>
                {chart}
              </Grid.Col>
            ))}
          </Grid>
        </Box>

        <Divider my="xl" />

        {/* Technology Breakdown */}
        <Box>
          <Title order={2} mb="lg">
            Technology Breakdown
          </Title>
          <Text size="md" color="dimmed" mb="xl">
            Detailed analysis of technologies, frameworks, and tools mentioned
            in job postings
          </Text>
          <Stack spacing="xl">{getHorizontalBarcharts()}</Stack>
        </Box>

        <Divider my="xl" />

        {/* Word Cloud Section */}
        <Box>
          <Title order={2} mb="lg">
            Job Title Analysis
          </Title>
          {getWordCloud()}
        </Box>
      </Stack>
    </Container>
  );
}
