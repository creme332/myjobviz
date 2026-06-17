import { useEffect, useState } from "react";
import { Box, Text, UnstyledButton, Stack } from "@mantine/core";

const SECTIONS = [
  { id: "section-trends", label: "Market Trends" },
  { id: "section-geo", label: "Geographic Distribution" },
  { id: "section-overview", label: "Market Overview" },
  { id: "section-tech", label: "Technology Breakdown" },
  { id: "section-titles", label: "Job Title Analysis" },
];

export default function TableOfContents() {
  const [active, setActive] = useState(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        // Pick the entry closest to the top of the viewport among visible ones
        const visible = entries.filter((e) => e.isIntersecting);
        if (visible.length > 0) {
          const topmost = visible.reduce((a, b) =>
            a.boundingClientRect.top < b.boundingClientRect.top ? a : b
          );
          setActive(topmost.target.id);
        }
      },
      { rootMargin: "-10% 0px -60% 0px", threshold: 0 }
    );

    SECTIONS.forEach(({ id }) => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, []);

  function scrollTo(id) {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  return (
    <Box
      style={{
        position: "fixed",
        right: 20,
        top: "50%",
        transform: "translateY(-50%)",
        zIndex: 200,
        background: "white",
        borderRadius: 8,
        boxShadow: "0 2px 12px rgba(0,0,0,0.10)",
        padding: "12px 0",
        minWidth: 190,
        border: "1px solid #e9ecef",
      }}
      sx={{ "@media (max-width: 1440px)": { display: "none" } }}
    >
      <Text
        size="xs"
        weight={700}
        color="dimmed"
        style={{ padding: "0 16px 8px", textTransform: "uppercase", letterSpacing: "0.05em" }}
      >
        On this page
      </Text>
      <Stack spacing={0}>
        {SECTIONS.map(({ id, label }) => {
          const isActive = active === id;
          return (
            <UnstyledButton
              key={id}
              onClick={() => scrollTo(id)}
              style={{
                display: "block",
                padding: "6px 16px",
                borderLeft: `3px solid ${isActive ? "#228be6" : "transparent"}`,
                background: isActive ? "#e7f5ff" : "transparent",
                transition: "background 0.15s, border-color 0.15s",
              }}
              sx={{
                "&:hover": {
                  background: "#f1f3f5",
                },
              }}
            >
              <Text
                size="sm"
                weight={isActive ? 600 : 400}
                color={isActive ? "blue" : "dimmed"}
                style={{ lineHeight: 1.4 }}
              >
                {label}
              </Text>
            </UnstyledButton>
          );
        })}
      </Stack>
    </Box>
  );
}
