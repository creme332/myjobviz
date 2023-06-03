import { Container, Alert } from "@mantine/core";
import StatsGrid from "../components/graphs/StatsGrid";
import HorizontalBarChart from "../components/graphs/HorizontalBarChart";
import PieChart from "../components/graphs/PieChart";
import AreaChart from "../components/graphs/LineChart";
import { IconAlertCircle } from "@tabler/icons-react";
import FireStoreManager from "../utils/FireStoreManager";
import { useState, useEffect } from "react";
export default function Results() {
  const [allData, setAllData] = useState(null);

  const data = [
    {
      title: "Jobs scraped this month",
      stats: "112",
      description: "24% more than in the same month last year",
    },
    {
      title: "Last update",
      stats: "16 hours ago",
      description: "myjob.mu website is scraped on a daily basis",
    },
    {
      title: "Total jobs scraped",
      stats: allData ? allData.database_size.size : "2553",
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
  };

  async function fetchData() {
    const result = await FireStoreManager().getAllDocs();
    setAllData(result);
    // console.log(allData);
    // console.log(split(result.web_data));
  }

  useEffect(() => {
    fetchData();
  }, []);

  function sort_object(dict) {
    const labelsArr = Object.keys(dict);
    const dataArr = labelsArr.map((k) => dict[k]);

    const arrayOfObj = labelsArr.map((d, i) => {
      return {
        label: d,
        data: parseInt(dataArr[i]) || 0,
      };
    });

    const sortedArrayOfObj = arrayOfObj.sort(function (a, b) {
      return b.data - a.data;
    });

    const newLabelsArray = [];
    const newDataArray = [];

    sortedArrayOfObj.forEach(function (d) {
      newLabelsArray.push(d.label);
      newDataArray.push(d.data);
    });

    return [newLabelsArray, newDataArray];
  }

  function getHorizontalBarcharts() {
    if (!allData) return;
    // console.log(allData);
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
      const [labelsArray, dataArray] = sort_object(data);

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
    if (!allData) return;
    const pieChartKeys = ["loc_data", "os_data", "salary_data"];

    const validKeys = Object.keys(allData).filter((k) =>
      pieChartKeys.includes(k)
    );

    return validKeys.map((k, index) => {
      const data = allData[k];
      const [labelsArray, dataArray] = sort_object(data);

      if (k === "os_data")
        return (
          <Container>
            <PieChart
              key={`piechart-${k}`}
              dataArray={dataArray}
              labelsArray={labelsArray}
              titleName={chartTitle[k]}
            />
            <Alert
              key={`piechart-alert-${k}`}
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
        console.log(i);
        const newDataArray = [...dataArray];
        const newLabelArray = [...labelsArray];
        const SeeDescriptionCount = newDataArray.splice(i, 1)[0];
        console.log(SeeDescriptionCount);
        const j = labelsArray.indexOf("Not disclosed");
        newDataArray[j] += SeeDescriptionCount;
        newLabelArray.splice(i, 1);
        return (
          <Container>
            <PieChart
              key={`piechart-${k}`}
              dataArray={newDataArray}
              labelsArray={newLabelArray}
              titleName={chartTitle[k]}
            />
            <Alert
              key={`piechart-alert-${k}`}
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
      <StatsGrid data={data} />
      <Container w={640}>{getPieCharts()}</Container>

      {getHorizontalBarcharts()}
      <AreaChart />
    </Container>
  );
}
