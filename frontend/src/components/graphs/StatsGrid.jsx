import {
  createStyles,
  Text,
  Paper,
  Group,
  rem,
  ThemeIcon,
  Stack,
} from "@mantine/core";
import {
  IconCalendarStats,
  IconClock,
  IconDatabase,
} from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  root: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
    gap: theme.spacing.lg,

    [theme.fn.smallerThan("sm")]: {
      gridTemplateColumns: "1fr",
    },
  },

  card: {
    position: "relative",
    overflow: "hidden",
    transition: "transform 150ms ease, box-shadow 150ms ease",

    "&:hover": {
      transform: "translateY(-4px)",
      boxShadow: theme.shadows.md,
    },
  },

  title: {
    fontWeight: 500,
    fontSize: theme.fontSizes.sm,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[1]
        : theme.colors.gray[6],
    textTransform: "uppercase",
    letterSpacing: rem(0.5),
  },

  count: {
    fontSize: rem(32),
    fontWeight: 700,
    lineHeight: 1.2,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
  },

  description: {
    fontSize: theme.fontSizes.sm,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[3]
        : theme.colors.gray[6],
    lineHeight: 1.6,
  },

  iconWrapper: {
    position: "absolute",
    top: rem(16),
    right: rem(16),
    opacity: 0.1,
  },
}));

const iconMap = {
  0: IconCalendarStats,
  1: IconClock,
  2: IconDatabase,
};

const colorMap = {
  0: "blue",
  1: "orange",
  2: "green",
};

export default function StatsGrid({ data }) {
  const { classes } = useStyles();

  const stats = data.map((stat, index) => {
    const Icon = iconMap[index] || IconDatabase;
    const color = colorMap[index] || "blue";

    return (
      <Paper
        key={stat.title}
        className={classes.card}
        p="xl"
        radius="md"
        shadow="sm"
        withBorder
      >
        <Stack spacing="md">
          <Group position="apart" align="flex-start">
            <div style={{ flex: 1 }}>
              <Text className={classes.title}>{stat.title}</Text>
            </div>
            <ThemeIcon size={48} radius="md" variant="light" color={color}>
              <Icon size={28} stroke={1.5} />
            </ThemeIcon>
          </Group>

          <div>
            <Text className={classes.count}>{stat.stats}</Text>
            <Text className={classes.description} mt="xs">
              {stat.description}
            </Text>
          </div>
        </Stack>

        <div className={classes.iconWrapper}>
          <Icon size={120} stroke={1} />
        </div>
      </Paper>
    );
  });

  return <div className={classes.root}>{stats}</div>;
}
