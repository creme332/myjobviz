import {
  createStyles,
  Container,
  Title,
  Text,
  Button,
  Card,
  Group,
  ThemeIcon,
  Box,
  SimpleGrid,
  rem,
} from "@mantine/core";
import { useNavigate } from "react-router-dom";
import {
  IconChartBar,
  IconTrendingUp,
  IconDatabase,
  IconBriefcase,
  IconArrowRight,
  IconChartLine,
  IconClock,
  IconBuildingSkyscraper,
} from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  hero: {
    position: "relative",
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.white,
    borderBottom: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[2]
    }`,
  },

  heroInner: {
    display: "flex",
    justifyContent: "space-between",
    paddingTop: rem(80),
    paddingBottom: rem(80),
    minHeight: rem(600),

    [theme.fn.smallerThan("md")]: {
      flexDirection: "column",
      paddingTop: rem(60),
      paddingBottom: rem(60),
      minHeight: "auto",
    },
  },

  heroContent: {
    maxWidth: rem(600),
    paddingRight: rem(60),

    [theme.fn.smallerThan("md")]: {
      maxWidth: "100%",
      paddingRight: 0,
      marginBottom: rem(40),
    },
  },

  eyebrow: {
    fontSize: rem(14),
    fontWeight: 600,
    textTransform: "uppercase",
    letterSpacing: rem(1),
    color: theme.colors.blue[6],
    marginBottom: rem(16),
  },

  heroTitle: {
    fontSize: rem(56),
    fontWeight: 900,
    lineHeight: 1.1,
    marginBottom: rem(24),
    color: theme.colorScheme === "dark" ? theme.white : theme.black,

    [theme.fn.smallerThan("md")]: {
      fontSize: rem(42),
    },

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(36),
    },
  },

  heroDescription: {
    fontSize: rem(20),
    lineHeight: 1.6,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[7],
    marginBottom: rem(40),

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(18),
    },
  },

  ctaGroup: {
    [theme.fn.smallerThan("sm")]: {
      flexDirection: "column",
    },
  },

  primaryCta: {
    height: rem(54),
    paddingLeft: rem(40),
    paddingRight: rem(40),
    fontSize: rem(16),
    fontWeight: 600,
    backgroundColor: theme.colors.blue[6],
    border: 0,

    "&:hover": {
      backgroundColor: theme.colors.blue[7],
    },

    [theme.fn.smallerThan("sm")]: {
      width: "100%",
    },
  },

  secondaryCta: {
    height: rem(54),
    paddingLeft: rem(40),
    paddingRight: rem(40),
    fontSize: rem(16),
    fontWeight: 600,
    color: theme.colorScheme === "dark" ? theme.white : theme.colors.gray[8],
    border: `2px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[4]
    }`,

    "&:hover": {
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[6]
          : theme.colors.gray[0],
    },

    [theme.fn.smallerThan("sm")]: {
      width: "100%",
    },
  },

  heroStats: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    gap: rem(24),
    flex: 1,

    [theme.fn.smallerThan("md")]: {
      display: "none",
    },
  },

  statCard: {
    backgroundColor:
      theme.colorScheme === "dark"
        ? theme.colors.dark[7]
        : theme.colors.gray[0],
    border: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[3]
    }`,
    borderRadius: theme.radius.md,
    padding: rem(24),
    display: "flex",
    alignItems: "center",
    gap: rem(20),
  },

  statIconWrapper: {
    minWidth: rem(56),
  },

  statContent: {
    flex: 1,
  },

  statValue: {
    fontSize: rem(28),
    fontWeight: 800,
    lineHeight: 1,
    marginBottom: rem(6),
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
  },

  statLabel: {
    fontSize: rem(14),
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    fontWeight: 500,
  },

  featuresSection: {
    backgroundColor:
      theme.colorScheme === "dark"
        ? theme.colors.dark[7]
        : theme.colors.gray[0],
    paddingTop: rem(80),
    paddingBottom: rem(80),

    [theme.fn.smallerThan("sm")]: {
      paddingTop: rem(60),
      paddingBottom: rem(60),
    },
  },

  sectionHeader: {
    textAlign: "center",
    marginBottom: rem(60),

    [theme.fn.smallerThan("sm")]: {
      marginBottom: rem(40),
    },
  },

  sectionTitle: {
    fontSize: rem(40),
    fontWeight: 800,
    marginBottom: rem(16),
    color: theme.colorScheme === "dark" ? theme.white : theme.black,

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(32),
    },
  },

  sectionSubtitle: {
    fontSize: rem(18),
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    maxWidth: rem(700),
    margin: "0 auto",
  },

  featureCard: {
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.white,
    border: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[3]
    }`,
    borderRadius: theme.radius.lg,
    padding: rem(32),
    height: "100%",
    transition: "all 0.2s ease",

    "&:hover": {
      borderColor: theme.colors.blue[6],
      transform: "translateY(-4px)",
      boxShadow: theme.shadows.md,
    },
  },

  featureIcon: {
    marginBottom: rem(20),
  },

  featureTitle: {
    fontSize: rem(20),
    fontWeight: 700,
    marginBottom: rem(12),
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
  },

  featureDescription: {
    fontSize: rem(15),
    lineHeight: 1.6,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
  },

  bottomCta: {
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.white,
    paddingTop: rem(80),
    paddingBottom: rem(80),
    borderTop: `1px solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[2]
    }`,

    [theme.fn.smallerThan("sm")]: {
      paddingTop: rem(60),
      paddingBottom: rem(60),
    },
  },

  bottomCtaContent: {
    textAlign: "center",
    maxWidth: rem(600),
    margin: "0 auto",
  },

  bottomCtaTitle: {
    fontSize: rem(36),
    fontWeight: 800,
    marginBottom: rem(16),
    color: theme.colorScheme === "dark" ? theme.white : theme.black,

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(28),
    },
  },

  bottomCtaText: {
    fontSize: rem(18),
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    marginBottom: rem(32),
  },
}));

export default function HeroSection() {
  const { classes } = useStyles();
  const navigate = useNavigate();

  const features = [
    {
      icon: IconChartBar,
      title: "Salary Data",
      description:
        "See what IT jobs pay in Mauritius. Compare salaries across different roles and companies.",
      color: "blue",
    },
    {
      icon: IconTrendingUp,
      title: "Daily Updates",
      description:
        "Fresh data every day from myjob.mu so you always have the latest information.",
      color: "green",
    },
    {
      icon: IconDatabase,
      title: "Track Trends",
      description:
        "Watch how the job market changes over time. Spot new opportunities early.",
      color: "violet",
    },
    {
      icon: IconBriefcase,
      title: "Job Details",
      description:
        "Learn what skills employers want, where jobs are located, and what they offer.",
      color: "orange",
    },
  ];

  const heroStats = [
    {
      icon: IconChartLine,
      value: "8,000+",
      label: "IT Jobs Analyzed",
      color: "blue",
    },
    {
      icon: IconClock,
      value: "Daily",
      label: "Data Updates",
      color: "green",
    },
    {
      icon: IconBuildingSkyscraper,
      value: "50+",
      label: "Companies Tracked",
      color: "violet",
    },
  ];

  return (
    <Box>
      {/* Hero Section */}
      <div className={classes.hero}>
        <Container size="xl">
          <div className={classes.heroInner}>
            <div className={classes.heroContent}>
              <Text className={classes.eyebrow}>IT Job Data</Text>
              <Title className={classes.heroTitle}>
                Find IT Jobs in Mauritius
              </Title>
              <Text className={classes.heroDescription}>
                Get real data on salaries, skills, and job openings. Make better
                career choices.
              </Text>
              <Group className={classes.ctaGroup} spacing="md">
                <Button
                  onClick={() => navigate("/results")}
                  className={classes.primaryCta}
                  rightIcon={<IconArrowRight size={18} />}
                >
                  View Data
                </Button>
                <Button
                  onClick={() => navigate("/methodology")}
                  className={classes.secondaryCta}
                  variant="default"
                >
                  How It Works
                </Button>
              </Group>
            </div>

            <div className={classes.heroStats}>
              {heroStats.map((stat, index) => {
                const Icon = stat.icon;
                return (
                  <div key={index} className={classes.statCard}>
                    <div className={classes.statIconWrapper}>
                      <ThemeIcon
                        size={56}
                        radius="md"
                        color={stat.color}
                        variant="light"
                      >
                        <Icon size={28} stroke={2} />
                      </ThemeIcon>
                    </div>
                    <div className={classes.statContent}>
                      <Text className={classes.statValue}>{stat.value}</Text>
                      <Text className={classes.statLabel}>{stat.label}</Text>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </Container>
      </div>

      {/* Features Section */}
      <div className={classes.featuresSection}>
        <Container size="xl">
          <div className={classes.sectionHeader}>
            <Title className={classes.sectionTitle}>What You'll Find</Title>
            <Text className={classes.sectionSubtitle}>
              All the job market data you need in one place.
            </Text>
          </div>

          <SimpleGrid
            cols={4}
            spacing="xl"
            breakpoints={[
              { maxWidth: "md", cols: 2, spacing: "lg" },
              { maxWidth: "sm", cols: 1, spacing: "md" },
            ]}
          >
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <Card key={index} className={classes.featureCard}>
                  <ThemeIcon
                    size={60}
                    radius="md"
                    color={feature.color}
                    variant="light"
                    className={classes.featureIcon}
                  >
                    <Icon size={32} stroke={2} />
                  </ThemeIcon>
                  <Text className={classes.featureTitle}>{feature.title}</Text>
                  <Text className={classes.featureDescription}>
                    {feature.description}
                  </Text>
                </Card>
              );
            })}
          </SimpleGrid>
        </Container>
      </div>

      {/* Bottom CTA */}
      <div className={classes.bottomCta}>
        <Container size="xl">
          <div className={classes.bottomCtaContent}>
            <Title className={classes.bottomCtaTitle}>Ready to explore?</Title>
            <Text className={classes.bottomCtaText}>
              Start browsing IT job data now.
            </Text>
            <Button
              onClick={() => navigate("/results")}
              size="lg"
              className={classes.primaryCta}
              rightIcon={<IconArrowRight size={18} />}
            >
              View All Data
            </Button>
          </div>
        </Container>
      </div>
    </Box>
  );
}
