import { createStyles, Group, Text, rem } from "@mantine/core";
import { Link } from "react-router-dom";
import { IconChartLine } from "@tabler/icons-react";

const useStyles = createStyles((theme, fontSize) => ({
  logo: {
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: rem(fontSize),
    lineHeight: 1.8,
    fontWeight: 900,

    [theme.fn.smallerThan("xs")]: {
      display: "none",
    },
  },
}));

export default function Logo({ logoSize = 48, fontSize = 28 }) {
  const { classes } = useStyles(fontSize);
  return (
    <Link title="Go to home page" style={{ textDecoration: "none" }} to={"/"}>
      <Group className={classes.logo}>
        <IconChartLine color="red" size={logoSize} strokeWidth={2} />
        <Text inherit>
          <Text inherit span color="blue">
            my
          </Text>
          <Text inherit span color="yellow">
            job
          </Text>
          <Text inherit span color="green">
            viz
          </Text>
        </Text>
      </Group>
    </Link>
  );
}
