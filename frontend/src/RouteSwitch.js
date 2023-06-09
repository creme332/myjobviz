import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import HeaderWithTabs from "./components/HeaderWithTabs";
import { MantineProvider, ColorSchemeProvider } from "@mantine/core";
import FooterSocial from "./components/FooterSocial";
import Results from "./pages/Results";
import Methodology from "./pages/Methodology";

const RouteSwitch = () => {
  const tabs = [
    { tabName: "Home", pathname: "/", id: "home-tab" },
    { tabName: "Results", pathname: "/results", id: "results-tab" },
    {
      tabName: "Methodology",
      pathname: "/methodology",
      id: "methodology-tab",
    },
  ];
  const [colorScheme, setColorScheme] = useState("light");
  const toggleColorScheme = (value) =>
    setColorScheme(value || (colorScheme === "dark" ? "light" : "dark"));

  return (
    <ColorSchemeProvider
      colorScheme={colorScheme}
      toggleColorScheme={toggleColorScheme}
    >
      <MantineProvider
        theme={{
          colorScheme,
          primaryColor: "red",
        }}
        withGlobalStyles
        withNormalizeCSS
      >
        <BrowserRouter>
          <HeaderWithTabs links={tabs} />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/results" element={<Results />} />
            <Route path="/methodology" element={<Methodology />} />
          </Routes>
          <FooterSocial />
        </BrowserRouter>
      </MantineProvider>
    </ColorSchemeProvider>
  );
};

export default RouteSwitch;
