import { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleQuantize } from "d3-scale";
import { Text, Group, Box } from "@mantine/core";

const GEO_URL = "/data/mu-districts.json";
const COLORS = ["#dbeafe", "#93c5fd", "#3b82f6", "#1d4ed8", "#1e3a8a"];
const NON_DISTRICT_KEYS = ["Mauritius", "Overseas"];

export default function ChoroplethMap({ locationData }) {
  const [tooltip, setTooltip] = useState(null);

  const districtEntries = Object.entries(locationData).filter(
    ([k]) => !NON_DISTRICT_KEYS.includes(k)
  );
  const maxVal = Math.max(...districtEntries.map(([, v]) => v));

  // Log scale so districts with low counts still get visible color differences
  const colorScale = scaleQuantize()
    .domain([0, Math.log1p(maxVal)])
    .range(COLORS);

  const rawThresholds = colorScale.thresholds();
  const legendBuckets = [
    { color: COLORS[0], label: `0 – ${Math.round(Math.expm1(rawThresholds[0]))}` },
    { color: COLORS[1], label: `${Math.round(Math.expm1(rawThresholds[0]))} – ${Math.round(Math.expm1(rawThresholds[1]))}` },
    { color: COLORS[2], label: `${Math.round(Math.expm1(rawThresholds[1]))} – ${Math.round(Math.expm1(rawThresholds[2]))}` },
    { color: COLORS[3], label: `${Math.round(Math.expm1(rawThresholds[2]))} – ${Math.round(Math.expm1(rawThresholds[3]))}` },
    { color: COLORS[4], label: `${Math.round(Math.expm1(rawThresholds[3]))}+` },
  ];

  return (
    <Box style={{ position: "relative" }}>
      <ComposableMap
        width={800}
        height={420}
        projection="geoMercator"
        projectionConfig={{ center: [57.5, -20.2], scale: 28000 }}
        style={{ width: "100%", height: "auto" }}
      >
        <Geographies geography={GEO_URL}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const count = locationData[geo.properties.name_1] ?? 0;
              return (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  fill={count > 0 ? colorScale(Math.log1p(count)) : "#e5e7eb"}
                  stroke="#fff"
                  strokeWidth={0.5}
                  style={{ hover: { opacity: 0.75, cursor: "pointer" } }}
                  onMouseEnter={() =>
                    setTooltip({ name: geo.properties.name_1, count })
                  }
                  onMouseLeave={() => setTooltip(null)}
                />
              );
            })
          }
        </Geographies>
      </ComposableMap>

      {tooltip && (
        <Box
          style={{
            position: "absolute",
            top: 12,
            right: 12,
            background: "rgba(0,0,0,0.75)",
            color: "#fff",
            padding: "6px 12px",
            borderRadius: 6,
            pointerEvents: "none",
            fontSize: 13,
          }}
        >
          <strong>{tooltip.name}</strong>
          <br />
          {tooltip.count} job{tooltip.count !== 1 ? "s" : ""}
        </Box>
      )}

      {/* Legend */}
      <Group spacing={4} mt={8} wrap="wrap">
        {legendBuckets.map(({ color, label }) => (
          <Group key={label} spacing={4} noWrap>
            <Box
              style={{
                width: 14,
                height: 14,
                borderRadius: 2,
                background: color,
                border: "1px solid #d1d5db",
                flexShrink: 0,
              }}
            />
            <Text size="xs" color="dimmed">
              {label}
            </Text>
          </Group>
        ))}
      </Group>

      {/* Footnote for non-district entries */}
      <Text size="xs" color="dimmed" mt={6}>
        {NON_DISTRICT_KEYS.map((k) =>
          locationData[k] != null ? (
            <span key={k} style={{ marginRight: 16 }}>
              <strong>{k}</strong>: {locationData[k]} jobs (not mapped to a district)
            </span>
          ) : null
        )}
      </Text>
    </Box>
  );
}
