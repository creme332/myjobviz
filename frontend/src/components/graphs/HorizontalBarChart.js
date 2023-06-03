import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
);

export default function HorizontalBarChart({
  themeIndex = 0,
  labelsArray,
  dataArray,
  dataLabel = "Dataset",
  titleName = "Sample title",
}) {
  const themes = [
    {
      borderColor: "rgb(255, 99, 132)", // red
      backgroundColor: "rgba(255, 99, 132, 0.5)",
    },
    {
      borderColor: "rgb(53, 162, 235)", // blue
      backgroundColor: "rgba(53, 162, 235, 0.5)",
    },
    {
      borderColor: "rgba(255, 206, 86, 1)", // yellow
      backgroundColor: "rgba(255, 206, 86, 0.2)",
    },
    {
      borderColor: "rgba(75, 192, 192, 1)", // green
      backgroundColor: "rgba(75, 192, 192, 0.2)",
    },
    {
      borderColor: "rgba(153, 102, 255, 1)", //purple
      backgroundColor: "rgba(153, 102, 255, 0.2)",
    },
    {
      borderColor: "rgba(255, 159, 64, 1)", // orange
      backgroundColor: "rgba(255, 159, 64, 0.2)",
    },
  ];

  const options = {
    indexAxis: "y",
    elements: {
      bar: {
        borderWidth: 2,
      },
    },
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: titleName,
      },
    },
  };

  const data = {
    labels: labelsArray,
    datasets: [
      {
        label: dataLabel,
        data: dataArray,
        borderColor: themes[themeIndex % themes.length].borderColor,
        backgroundColor: themes[themeIndex % themes.length].backgroundColor,
      },
    ],
  };

  return <Bar options={options} data={data} />;
}
