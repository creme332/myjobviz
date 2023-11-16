import { Container, Alert, Title } from "@mantine/core";
import StatsGrid from "../components/graphs/StatsGrid";
import HorizontalBarChart from "../components/graphs/HorizontalBarChart";
import PieChart from "../components/graphs/PieChart";
import LineChart from "../components/graphs/LineChart";
import { IconAlertCircle } from "@tabler/icons-react";
import WordCloud from "../components/graphs/WordCloud";

export default function Results({ allData }) {
  const stats_grid_data = [
    {
      title: "Jobs scraped this month",
      stats: allData ? allData.metadata.job_count_this_month : "...",
      description: "Number of jobs scraped since start of current month",
    },
    {
      title: "Last update",
      stats: allData
        ? date_diff_days(allData.metadata.last_update.toDate(), new Date())
        : "... hours ago",
      description: "myjob.mu website is scraped on a daily basis",
    },
    {
      title: "Total jobs scraped",
      stats: allData ? allData.metadata.size : "...",
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
    if (!allData) return;

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
      <LineChart
        title={chartTitle.job_trend_by_month}
        labelsArray={parseDate(labelsArray)}
        dataArray={dataArray}
      />
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
    if (!allData) return null;
    const data = allData.job_title_data;
    const keys = Object.keys(data);
    const words = [];
    for (const key of keys) {
      words.push({ text: key, value: data[key] });
    }

    return (
      <Container>
        <Title order={1}>Keywords in job titles</Title>
        <WordCloud words={words} />
      </Container>
    );
  }

  function getHorizontalBarcharts() {
    if (!allData) return null;
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
        <HorizontalBarChart
          key={`horizontal-barchart-${k}`}
          dataArray={dataArray}
          labelsArray={labelsArray}
          dataLabel="Frequency"
          titleName={chartTitle[k]}
          themeIndex={index}
        />
      );
    });
  }

  function getPieCharts() {
    if (!allData) return null;
    const pieChartKeys = ["loc_data", "os_data", "salary_data"];

    const validKeys = Object.keys(allData).filter((k) =>
      pieChartKeys.includes(k)
    );

    return validKeys.map((k) => {
      const data = allData[k];
      const [labelsArray, dataArray] = dictToArray(data);

      if (k === "os_data")
        return (
          <Container key={`piechart-container-${k}`}>
            <PieChart
              dataArray={dataArray}
              labelsArray={labelsArray}
              titleName={chartTitle[k]}
            />
            <Alert
              icon={<IconAlertCircle size="1rem" />}
              title="Note"
              color="green"
            >
              Not all jobs mention an operating system in the job description.
            </Alert>
          </Container>
        );

      if (k === "salary_data") {
        // merge "See description" and "not disclosed"
        const i = labelsArray.indexOf("See description");
        const newDataArray = [...dataArray];
        const newLabelArray = [...labelsArray];
        const SeeDescriptionCount = newDataArray.splice(i, 1)[0];
        const j = labelsArray.indexOf("Not disclosed");
        newDataArray[j] += SeeDescriptionCount;
        newLabelArray.splice(i, 1);
        return (
          <Container key={`piechart-container-${k}`}>
            <PieChart
              dataArray={newDataArray}
              labelsArray={newLabelArray}
              titleName={chartTitle[k]}
            />
            <Alert
              icon={<IconAlertCircle size="1rem" />}
              title="Note"
              color="green"
            >
              Jobs posts which set the salary to "See description" were counted
              in the "Not disclosed" category.
            </Alert>
          </Container>
        );
      }
      return (
        <PieChart
          key={`piechart-${k}`}
          dataArray={dataArray}
          labelsArray={labelsArray}
          titleName={chartTitle[k]}
        />
      );
    });
  }

  return (
    <Container>
      <StatsGrid data={stats_grid_data} />
      <Alert
        icon={<IconAlertCircle size="1rem" />}
        title="Disclaimer"
        color="orange"
      >
        Please be aware that while efforts have been made to ensure accurate
        representation and meaningful interpretations, there is a possibility of
        misinterpretations or errors in the analysis. The conclusions drawn from
        the data should be approached with caution.
      </Alert>

      {getLineChart()}

      <Container size="sm">{getPieCharts()}</Container>

      {getHorizontalBarcharts()}
      {getWordCloud()}
    </Container>
  );
}
