import {
  Container,
  Title,
  Text,
  Card,
  Stack,
  Group,
  ThemeIcon,
  Box,
  createStyles,
  rem,
} from "@mantine/core";
import {
  IconShovel,
  IconDatabaseEdit,
  IconZoomCode,
  IconChartHistogram,
  IconArrowDown,
} from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  title: {
    fontSize: rem(34),
    fontWeight: 900,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    marginBottom: theme.spacing.md,
    textAlign: "center",

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(24),
    },
  },

  subtitle: {
    textAlign: "center",
    maxWidth: rem(600),
    margin: "0 auto",
    marginBottom: `calc(${theme.spacing.xl} * 2)`,

    [theme.fn.smallerThan("sm")]: {
      marginBottom: theme.spacing.xl,
    },
  },

  card: {
    position: "relative",
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.white,
    transition: "transform 150ms ease, box-shadow 150ms ease",

    "&:hover": {
      transform: "scale(1.02)",
      boxShadow: theme.shadows.md,
    },
  },

  stepNumber: {
    position: "absolute",
    top: theme.spacing.md,
    right: theme.spacing.md,
    fontSize: rem(48),
    fontWeight: 700,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[4]
        : theme.colors.gray[2],
    lineHeight: 1,
  },

  iconWrapper: {
    marginBottom: theme.spacing.md,
  },

  cardTitle: {
    fontWeight: 700,
    fontSize: rem(20),
    marginBottom: theme.spacing.xs,
  },

  cardDescription: {
    fontSize: theme.fontSizes.sm,
    lineHeight: 1.6,
  },

  arrowContainer: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    margin: `${theme.spacing.sm} 0`,
  },
}));

export default function Methodology() {
  const { classes } = useStyles();

  const steps = [
    {
      icon: IconShovel,
      color: "red",
      title: "Data Collection",
      description:
        "Our automated scraper runs daily to collect IT job postings from myjob.mu, Mauritius' leading job portal. Each job listing is carefully extracted with all its metadata including title, description, salary, location, and requirements.",
    },
    {
      icon: IconZoomCode,
      color: "blue",
      title: "Data Processing",
      description:
        "Text analysis algorithms parse job descriptions to extract key information. We identify programming languages, frameworks, tools, databases, cloud platforms, and other technologies mentioned in each posting to build comprehensive statistics.",
    },
    {
      icon: IconDatabaseEdit,
      color: "yellow",
      title: "Data Storage",
      description:
        "Processed statistics are aggregated and stored in a database, ensuring reliable access and real-time updates. Historical data is preserved to enable trend analysis and month-over-month comparisons of the job market.",
    },
    {
      icon: IconChartHistogram,
      color: "green",
      title: "Visualization",
      description:
        "Interactive charts and graphs are dynamically generated using Chart.js and React, transforming raw statistics into meaningful insights. Users can explore trends in technology demand, salary ranges, job locations, and emerging skills in the IT sector.",
    },
  ];

  return (
    <Container size="lg" mt={40} mb={60}>
      <Stack spacing="xl">
        <Box>
          <Title className={classes.title}>How It Works</Title>
          <Text color="dimmed" className={classes.subtitle}>
            Our data pipeline transforms raw job postings into actionable
            insights about the Mauritius IT job market
          </Text>
        </Box>

        <Stack spacing={0}>
          {steps.map((step, index) => (
            <Box key={step.title}>
              <Card shadow="sm" p="lg" radius="md" className={classes.card}>
                <span className={classes.stepNumber}>{index + 1}</span>

                <Group align="flex-start" noWrap>
                  <ThemeIcon
                    size={60}
                    radius="md"
                    variant="light"
                    color={step.color}
                    className={classes.iconWrapper}
                  >
                    <step.icon size={32} />
                  </ThemeIcon>

                  <Stack spacing="xs" style={{ flex: 1 }}>
                    <Text className={classes.cardTitle}>{step.title}</Text>
                    <Text color="dimmed" className={classes.cardDescription}>
                      {step.description}
                    </Text>
                  </Stack>
                </Group>
              </Card>

              {index < steps.length - 1 && (
                <Box className={classes.arrowContainer}>
                  <ThemeIcon size="lg" radius="xl" variant="light" color="gray">
                    <IconArrowDown size={20} />
                  </ThemeIcon>
                </Box>
              )}
            </Box>
          ))}
        </Stack>
      </Stack>
    </Container>
  );
}
