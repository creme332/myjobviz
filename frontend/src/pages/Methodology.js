import { Timeline, Text, Container, Flex } from "@mantine/core";
import {
  IconShovel,
  IconDatabaseEdit,
  IconZoomCode,
  IconChartHistogram,
} from "@tabler/icons-react";

export default function Methodology() {
  const iconSize = 30;
  return (
    <Container mt={30}>
      <Flex justify={"center"}>
        <Timeline bulletSize={40} lineWidth={4}>
          <Timeline.Item
            bullet={<IconShovel size={iconSize} />}
            title="Scraping"
          >
            <Text color="dimmed" size="sm">
              IT job posts are scraped from myjob.mu website
            </Text>
          </Timeline.Item>
          <Timeline.Item
            bullet={<IconZoomCode size={iconSize} />}
            title="Statistics"
          >
            <Text color="dimmed" size="sm">
              Data is extracted from job posts and create statistics.
            </Text>
          </Timeline.Item>
          <Timeline.Item
            title="Database"
            bullet={<IconDatabaseEdit size={iconSize} />}
          >
            <Text color="dimmed" size="sm">
              Statistics are saved to a database.
            </Text>
          </Timeline.Item>
          <Timeline.Item
            title="Display"
            bullet={<IconChartHistogram size={iconSize} />}
          >
            <Text color="dimmed" size="sm">
              Charts are generated on frontend using statistics from database.
            </Text>
          </Timeline.Item>
        </Timeline>
      </Flex>
    </Container>
  );
}
