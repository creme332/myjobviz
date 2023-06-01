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
      "loc_data",
      "os_data",
      "salary_data",
      "tools_data",
      "web_data",
    ];

    const validKeys = Object.keys(allData).filter((k) =>
      horizonalBarChartKeys.includes(k)
    );

    return validKeys.map((k, index) => {
      const data = allData[k];
      const [labelsArray, dataArray] = sort_object(data);
      console.log(labelsArray, dataArray);

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

  return (
    <Container>
      <StatsGrid data={data} />
      {getHorizontalBarcharts()}
      <AreaChart />
      <Container w={500}>
        <PieChart />
      </Container>
      <Alert icon={<IconAlertCircle size="1rem" />} title="Note" color="red">
        Only 2% of jobs disclosed a salary range.
      </Alert>
      <Alert icon={<IconAlertCircle size="1rem" />} title="Note" color="green">
        The percentage represents the percentage jobs mentioning an operating
        system. Not all jobs mention OS.
      </Alert>
    </Container>
  );
}
