import { useState, useEffect } from "react";
import {
  createStyles,
  Header,
  Container,
  Group,
  Burger,
  Paper,
  Transition,
  ActionIcon,
  useMantineColorScheme,
  rem,
  Text,
  Box,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { IconMoonStars, IconSun } from "@tabler/icons-react";
import { Link, useLocation } from "react-router-dom";
import Logo from "./Logo";

const HEADER_HEIGHT = rem(70);

const useStyles = createStyles((theme) => ({
  root: {
    position: "sticky",
    top: 0,
    zIndex: 100,
    borderBottom: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
    backgroundColor:
      theme.colorScheme === "dark"
        ? theme.fn.rgba(theme.colors.dark[7], 0.95)
        : theme.fn.rgba(theme.white, 0.95),
    backdropFilter: "blur(10px)",
    transition: "box-shadow 150ms ease",
  },

  scrolled: {
    boxShadow: theme.shadows.sm,
  },

  dropdown: {
    position: "absolute",
    top: HEADER_HEIGHT,
    left: 0,
    right: 0,
    zIndex: 0,
    borderTopRightRadius: 0,
    borderTopLeftRadius: 0,
    borderTopWidth: 0,
    overflow: "hidden",
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.white,

    [theme.fn.largerThan("sm")]: {
      display: "none",
    },
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    height: "100%",
  },

  links: {
    [theme.fn.smallerThan("sm")]: {
      display: "none",
    },
  },

  burger: {
    [theme.fn.largerThan("sm")]: {
      display: "none",
    },
  },

  link: {
    display: "flex",
    alignItems: "center",
    lineHeight: 1,
    padding: `${rem(10)} ${rem(16)}`,
    borderRadius: theme.radius.md,
    textDecoration: "none",
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[0]
        : theme.colors.gray[7],
    fontSize: theme.fontSizes.sm,
    fontWeight: 500,
    transition: "all 150ms ease",
    position: "relative",

    "&:hover": {
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[1],
      transform: "translateY(-1px)",
    },

    [theme.fn.smallerThan("sm")]: {
      borderRadius: 0,
      padding: `${rem(16)} ${theme.spacing.md}`,
      fontSize: theme.fontSizes.md,
    },
  },

  linkActive: {
    backgroundColor: theme.fn.variant({
      variant: "light",
      color: theme.primaryColor,
    }).background,
    color: theme.fn.variant({ variant: "light", color: theme.primaryColor })
      .color,
    fontWeight: 600,

    "&:hover": {
      backgroundColor: theme.fn.variant({
        variant: "light",
        color: theme.primaryColor,
      }).background,
    },

    "&::after": {
      content: '""',
      position: "absolute",
      bottom: 0,
      left: "50%",
      transform: "translateX(-50%)",
      width: "80%",
      height: rem(2),
      backgroundColor: theme.fn.variant({
        variant: "filled",
        color: theme.primaryColor,
      }).background,
      borderRadius: theme.radius.xl,

      [theme.fn.smallerThan("sm")]: {
        display: "none",
      },
    },
  },

  themeToggle: {
    border: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.white,
    transition: "all 150ms ease",

    "&:hover": {
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[0],
      transform: "rotate(15deg)",
    },
  },

  themeLabel: {
    fontSize: theme.fontSizes.xs,
    fontWeight: 500,
    marginLeft: theme.spacing.xs,

    [theme.fn.smallerThan("md")]: {
      display: "none",
    },
  },
}));

export default function HeaderWithTabs({ links }) {
  const location = useLocation();
  const [opened, { toggle, close }] = useDisclosure(false);
  const [active, setActive] = useState(location.pathname);
  const [scrolled, setScrolled] = useState(false);
  const { classes, cx } = useStyles();
  const { colorScheme, toggleColorScheme } = useMantineColorScheme();
  const dark = colorScheme === "dark";

  useEffect(() => {
    setActive(location.pathname);
  }, [location]);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const items = links.map((link) => (
    <Link
      key={link.id}
      className={cx(classes.link, {
        [classes.linkActive]: active === link.pathname,
      })}
      onClick={() => {
        setActive(link.pathname);
        close();
      }}
      to={link.pathname}
    >
      {link.tabName}
    </Link>
  ));

  return (
    <Header
      height={HEADER_HEIGHT}
      className={cx(classes.root, { [classes.scrolled]: scrolled })}
    >
      <Container size="xl" className={classes.header}>
        <Logo />
        <Group spacing={8} className={classes.links}>
          {items}
          <Box
            sx={(theme) => ({
              display: "flex",
              alignItems: "center",
              marginLeft: rem(12),
              paddingLeft: rem(12),
              borderLeft: `${rem(1)} solid ${
                theme.colorScheme === "dark"
                  ? theme.colors.dark[4]
                  : theme.colors.gray[3]
              }`,
            })}
          >
            <ActionIcon
              className={classes.themeToggle}
              size="lg"
              onClick={() => toggleColorScheme()}
              title={`Switch to ${dark ? "light" : "dark"} mode`}
              aria-label="Toggle color scheme"
            >
              {dark ? (
                <IconSun size="1.2rem" />
              ) : (
                <IconMoonStars size="1.2rem" />
              )}
            </ActionIcon>
            <Text className={classes.themeLabel} color="dimmed">
              {dark ? "Light" : "Dark"}
            </Text>
          </Box>
        </Group>

        <Burger
          aria-label="Toggle navigation"
          opened={opened}
          onClick={toggle}
          className={classes.burger}
          size="sm"
        />

        <Transition transition="pop-top-right" duration={200} mounted={opened}>
          {(styles) => (
            <Paper className={classes.dropdown} withBorder style={styles}>
              {items}
            </Paper>
          )}
        </Transition>
      </Container>
    </Header>
  );
}
