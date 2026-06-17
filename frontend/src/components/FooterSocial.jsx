import {
  createStyles,
  Container,
  ActionIcon,
  Text,
  Stack,
  rem,
} from "@mantine/core";
import { IconBrandGithub, IconMail, IconDatabase } from "@tabler/icons-react";
import Logo from "./Logo";

const useStyles = createStyles((theme) => ({
  footer: {
    marginTop: rem(120),
    paddingTop: rem(60),
    paddingBottom: rem(40),
    backgroundColor:
      theme.colorScheme === "dark"
        ? theme.colors.dark[8]
        : theme.colors.gray[0],
    borderTop: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[3]
    }`,
  },

  inner: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    gap: rem(40),

    [theme.fn.smallerThan("sm")]: {
      flexDirection: "column",
      alignItems: "center",
      textAlign: "center",
      gap: rem(30),
    },
  },

  section: {
    flex: 1,
    minWidth: 0,
  },

  logoSection: {
    maxWidth: rem(350),

    [theme.fn.smallerThan("sm")]: {
      maxWidth: "100%",
    },
  },

  description: {
    marginTop: theme.spacing.sm,
    fontSize: theme.fontSizes.sm,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    lineHeight: 1.6,
  },

  title: {
    fontSize: theme.fontSizes.sm,
    fontWeight: 700,
    textTransform: "uppercase",
    marginBottom: theme.spacing.sm,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[1]
        : theme.colors.gray[7],
    letterSpacing: rem(0.5),
  },

  links: {
    display: "flex",
    flexDirection: "column",
    gap: theme.spacing.xs,
  },

  link: {
    fontSize: theme.fontSizes.sm,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    textDecoration: "none",
    transition: "color 150ms ease",
    display: "flex",
    alignItems: "center",
    gap: rem(6),

    "&:hover": {
      color:
        theme.colorScheme === "dark"
          ? theme.colors.dark[0]
          : theme.colors.gray[8],
      textDecoration: "underline",
    },

    [theme.fn.smallerThan("sm")]: {
      justifyContent: "center",
    },
  },

  socialSection: {
    [theme.fn.smallerThan("sm")]: {
      width: "100%",
    },
  },

  socialLinks: {
    display: "flex",
    gap: theme.spacing.md,

    [theme.fn.smallerThan("sm")]: {
      justifyContent: "center",
    },
  },

  socialLink: {
    border: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]
    }`,
    transition: "all 150ms ease",

    "&:hover": {
      transform: "translateY(-2px)",
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[1],
    },
  },

  socialLabel: {
    fontSize: theme.fontSizes.xs,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[2]
        : theme.colors.gray[6],
    marginTop: rem(4),
  },

  bottom: {
    marginTop: rem(40),
    paddingTop: rem(30),
    borderTop: `${rem(1)} solid ${
      theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.gray[3]
    }`,
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    flexWrap: "wrap",
    gap: rem(16),

    [theme.fn.smallerThan("sm")]: {
      flexDirection: "column",
      textAlign: "center",
    },
  },

  copyright: {
    fontSize: theme.fontSizes.xs,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[3]
        : theme.colors.gray[5],
  },

  stats: {
    display: "flex",
    gap: rem(20),
    fontSize: theme.fontSizes.xs,
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[3]
        : theme.colors.gray[5],

    [theme.fn.smallerThan("sm")]: {
      flexDirection: "column",
      gap: rem(8),
    },
  },

  stat: {
    display: "flex",
    alignItems: "center",
    gap: rem(6),
  },

  statDot: {
    width: rem(4),
    height: rem(4),
    borderRadius: "50%",
    backgroundColor: theme.colors.green[6],

    [theme.fn.smallerThan("sm")]: {
      display: "none",
    },
  },

  datasetIcon: {
    width: rem(14),
    height: rem(14),
  },
}));

function FooterSocial() {
  const { classes } = useStyles();
  const currentYear = new Date().getFullYear();

  return (
    <div className={classes.footer}>
      <Container size="xl">
        <div className={classes.inner}>
          {/* Logo and Description Section */}
          <div className={`${classes.section} ${classes.logoSection}`}>
            <Logo logoSize={38} fontSize={25} />
            <Text className={classes.description}>
              Visualizing IT job market trends in Mauritius. Helping job seekers
              and professionals make informed career decisions with real-time
              data and insights.
            </Text>
          </div>

          {/* Quick Links Section */}
          <div className={classes.section}>
            <Text className={classes.title}>Quick Links</Text>
            <div className={classes.links}>
              <a href="/" className={classes.link}>
                Home
              </a>
              <a href="/results" className={classes.link}>
                View Results
              </a>
              <a href="/methodology" className={classes.link}>
                Methodology
              </a>
            </div>
          </div>

          {/* Resources Section */}
          <div className={classes.section}>
            <Text className={classes.title}>Resources</Text>
            <div className={classes.links}>
              <a
                href="https://huggingface.co/datasets/goated69/mauritius-it-jobs"
                target="_blank"
                rel="noopener noreferrer"
                className={classes.link}
              >
                <IconDatabase
                  size={14}
                  stroke={1.5}
                  className={classes.datasetIcon}
                />
                Open Dataset
              </a>
              <a
                href="https://myjob.mu"
                target="_blank"
                rel="noopener noreferrer"
                className={classes.link}
              >
                Data Source (MyJob.mu)
              </a>
              <a
                href="https://github.com/creme332/myjobviz"
                target="_blank"
                rel="noopener noreferrer"
                className={classes.link}
              >
                View on GitHub
              </a>
            </div>
          </div>

          {/* Social Section */}
          <div className={`${classes.section} ${classes.socialSection}`}>
            <Text className={classes.title}>Connect</Text>
            <div className={classes.socialLinks}>
              <Stack spacing={4} align="center">
                <ActionIcon
                  className={classes.socialLink}
                  component="a"
                  href="https://github.com/creme332/myjobviz"
                  target="_blank"
                  rel="noopener noreferrer"
                  size="lg"
                  aria-label="Visit GitHub repository"
                >
                  <IconBrandGithub size="1.3rem" stroke={1.5} />
                </ActionIcon>
                <Text className={classes.socialLabel}>GitHub</Text>
              </Stack>

              <Stack spacing={4} align="center">
                <ActionIcon
                  className={classes.socialLink}
                  component="a"
                  href="mailto:c34560814@gmail.com"
                  size="lg"
                  aria-label="Send email"
                >
                  <IconMail size="1.3rem" stroke={1.5} />
                </ActionIcon>
                <Text className={classes.socialLabel}>Email</Text>
              </Stack>
            </div>
          </div>
        </div>

        {/* Bottom Section */}
        <div className={classes.bottom}>
          <Text className={classes.copyright}>
            © {currentYear} MyJobViz. Open source project. Data sourced from
            MyJob.mu
          </Text>

          <div className={classes.stats}>
            <div className={classes.stat}>
              <div className={classes.statDot} />
              <span>Updated Daily</span>
            </div>
            <div className={classes.stat}>
              <div className={classes.statDot} />
              <span>Made in Mauritius</span>
            </div>
          </div>
        </div>
      </Container>
    </div>
  );
}

export default FooterSocial;
