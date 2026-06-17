import D3WordCloud from "react-d3-cloud";

const COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"];

export default function WordCloud({ words }) {
  const maxVal = Math.max(...words.map((w) => w.value));
  return (
    <D3WordCloud
      data={words}
      fontSize={(word) => 14 + (word.value / maxVal) * 32}
      font="impact"
      fontStyle="normal"
      fontWeight="normal"
      rotate={0}
      padding={4}
      spiral="archimedean"
      fill={(_, index) => COLORS[index % COLORS.length]}
      random={() => 0.5}
    />
  );
}
