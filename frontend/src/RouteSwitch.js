import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import HeaderWithTabs from "./components/HeaderWithTabs";
import { MantineProvider, ColorSchemeProvider } from "@mantine/core";
import FooterSocial from "./components/FooterSocial";

const RouteSwitch = () => {
  const tabs = [
    { tabName: "Home", pathname: "/", id: "home-tab" },
    { tabName: "Other", pathname: "/leaderboard", id: "other-tab" },
  ];
  const [colorScheme, setColorScheme] = useState("dark");
  const toggleColorScheme = (value) =>
    setColorScheme(value || (colorScheme === "dark" ? "light" : "dark"));

  return (
    <ColorSchemeProvider
      colorScheme={colorScheme}
      toggleColorScheme={toggleColorScheme}
    >
      <MantineProvider
        theme={{ colorScheme }}
        withGlobalStyles
        withNormalizeCSS
      >
        <BrowserRouter>
          <HeaderWithTabs links={tabs} />
          <Routes>
            <Route path="/" element={<Home />} />
          </Routes>
          <FooterSocial />
        </BrowserRouter>
      </MantineProvider>
    </ColorSchemeProvider>
  );
};

export default RouteSwitch;
