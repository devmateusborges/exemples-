"use client";
import React, { useState, useEffect } from "react";
import { Button } from "primereact/button";
import AppVisible from "./toolkit-react/bases/AppVisible";

const AppCardCheckList: React.FC = () => {
  const [hiddenButtonScroll, setHiddenButtonScroll] = useState(false);
  function scrollTopSmooth() {
    window.scroll({ top: 0, left: 0, behavior: "smooth" });
  }

  useEffect(() => {
    function handleScroll(event: any) {
      let scrollTop = event.target.scrollingElement.scrollTop;

      if (scrollTop > 600) {
        setHiddenButtonScroll(true);
      } else {
        setHiddenButtonScroll(false);
      }
    }
    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div
      style={{
        position: "fixed",
        zIndex: 1,
        right: 20,
        bottom: 20,
      }}
    >
      <AppVisible visible={hiddenButtonScroll}>
        <Button
          icon="pi pi-arrow-up"
          className="fadein animation-duration-500 h-3rem w-3rem p-button-danger text-white shadow-3 border-round"
          onClick={scrollTopSmooth}
        />
      </AppVisible>
    </div>
  );
};

export default AppCardCheckList;
