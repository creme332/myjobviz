import os.path


def update_job_count_badge(new_job_count: int) -> None:
    """
    Updates the job badge found in the README.

    README must contain a line with `![{badge_id}]({badge_url})`

    Args:
        new_job_count (int): new job count
    """
    badge_id = "job-count-1"
    badge_color = 'orange'

    # ! location of README in root directory relative to main.py
    file_path = os.path.dirname(__file__) + '/../../README.md'

    # ! badge_url and new_badge should not contain any spaces
    badge_url = ('https://img.shields.io'
                 '/badge/Total%20jobs%20scraped'
                 f'-{new_job_count}-{badge_color}')

    new_badge = (f'![{badge_id}]({badge_url})')

    new_file_content = ''
    with open(file_path, 'r', encoding='utf-8') as f:
        # get all lines
        lines = [line for line in f]

        # get line number of first line containing job count badge
        line_num = [i for i in range(0, len(lines)) if badge_id in lines[i]][0]

        # get first line in readme containing job count badge
        modify_line = lines[line_num]

        # * This line contains many space-separated badges
        # * Modify only the badge which match badge_id
        all_badges = modify_line.split(' ')

        # get index of job count badge
        badge_num = [i for i in range(
            0, len(all_badges)) if badge_id in all_badges[i]][0]

        # update badge and line
        all_badges[badge_num] = new_badge
        lines[line_num] = ' '.join(all_badges)

        # concatenate lines
        new_file_content = ''.join(lines)

    # update file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
