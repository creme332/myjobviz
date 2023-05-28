import { Container } from "@mantine/core";
import StatsGrid from "../components/graphs/StatsGrid";
import HorizontalBarChart from "../components/graphs/HorizontalBarChart";
import PieChart from "../components/graphs/PieChart";
import AreaChart from "../components/graphs/LineChart";
export default function Results() {
  const data = [
    {
      title: "Jobs scraped this month",
      stats: "112",
      description:
        "24% more than in the same month last year, 33% more that two years ago",
    },
    {
      title: "Last update",
      stats: "16 hours ago",
      description: "myjobmu website",
    },
    { title: "Total jobs scraped", stats: "2553", description: 0 },
  ];
  return (
    <Container>
      <StatsGrid data={data} />
      <AreaChart />
      <HorizontalBarChart themeIndex={0} />
      <Container w={500}>
        <PieChart />
      </Container>
      <HorizontalBarChart themeIndex={1} />
      <HorizontalBarChart themeIndex={2} />
      <HorizontalBarChart themeIndex={3} />
      <HorizontalBarChart themeIndex={4} />
      <HorizontalBarChart themeIndex={5} />
    </Container>
  );
}
