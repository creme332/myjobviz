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

  async function fetchData() {
    const result = await FireStoreManager().getAllDocs();
    setAllData(result);
    console.log(allData);
    console.log(split(result.web_data));
  }

  useEffect(() => {
    fetchData();
  }, []);

  function split(dict) {
    const labelsArray = Object.keys(dict);
    const dataArray = labelsArray.map((k) => dict[k]);
    return { labelsArray, dataArray };
  }

  function getCharts() {
    if (allData) {
      const allKeys = Object.keys(allData);
      console.log(allKeys);
      return allKeys.map((k, index) => {
        return (
          <HorizontalBarChart
            key={`horizontal-barchart-${k}`}
            dataArray={split(allData[k]).dataArray}
            labelsArray={split(allData[k]).labelsArray}
            dataLabel="Count"
            titleName="Web frameworks"
            themeIndex={index}
          />
        );
      });
    }
  }
  return (
    <Container>
      <StatsGrid data={data} />
      {getCharts()}
      <AreaChart />
      <Container w={500}>
        <PieChart />
      </Container>
      <Alert icon={<IconAlertCircle size="1rem" />} title="Note" color="red">
        Only 2% of jobs disclosed a salary range.
      </Alert>
      <HorizontalBarChart themeIndex={2} />
      <Alert icon={<IconAlertCircle size="1rem" />} title="Note" color="green">
        The percentage represents the percentage jobs mentioning an operating
        system. Not all jobs mention OS.
      </Alert>
    </Container>
  );
}
