import { createStyles, Container, Group, ActionIcon, rem } from "@mantine/core";
import { IconBrandGithub, IconMail, IconChartLine } from "@tabler/icons-react";
import Logo from "./Logo";
const useStyles = createStyles((theme) => ({
  logo: {
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: rem(22),
    lineHeight: 1.8,
    fontWeight: 900,

    [theme.fn.smallerThan("xs")]: {
      display: "none",
    },
  },

  footer: {
    marginTop: rem(120),
    borderTop: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[2]
    }`,
  },

  inner: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    paddingTop: theme.spacing.xl,
    paddingBottom: theme.spacing.xl,

    [theme.fn.smallerThan("xs")]: {
      flexDirection: "column",
    },
  },

  links: {
    [theme.fn.smallerThan("xs")]: {
      marginTop: theme.spacing.md,
    },
  },
}));

function FooterSocial() {
  const { classes } = useStyles();

  return (
    <div className={classes.footer}>
      <Container className={classes.inner}>
        <Logo logoSize={38} fontSize={25} />
        <Group spacing={25} className={classes.links} position="right" noWrap>
          <ActionIcon
            aria-label="Github"
            component="a"
            href="https://github.com/creme332/my-odin-projects/tree/main/photo-tagging"
            size="lg"
          >
            <IconBrandGithub size="1.5rem" stroke={1.5} />
          </ActionIcon>
          <ActionIcon
            aria-label="Email"
            component="a"
            href="mailto:c34560814@gmail.com"
            size="lg"
          >
            <IconMail size="1.5rem" stroke={1.5} />
          </ActionIcon>
        </Group>
      </Container>
    </div>
  );
}

export default FooterSocial;
