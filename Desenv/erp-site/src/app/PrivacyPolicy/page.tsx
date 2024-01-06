"use client";
import AppHeader from "@components/AppHeader";
import React, { useEffect, useState } from "react";
//import { Document, Page, pdfjs } from "react-pdf";

const PrivacyPolicyPage: React.FC = () => {
  const [numPages, setNumPages] = useState<number>();
  const [pageNumber, setPageNumber] = useState<number[]>([
    1, 2, 3, 4, 5, 6, 7, 8, 9,
  ]);

  const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
    setNumPages(numPages);
  };

  return (
    <div className="sub-topbar  ">
      <AppHeader title="POLÍTICAS DE PRIVACIDADE" />
      {/* <Document
        className="grid  align-items-center  justify-content-center"
        file="/assets/pdf/politica-privacidade.pdf"
        onLoadSuccess={onDocumentLoadSuccess}
      >
        {pageNumber.map((pdf, index) => (
          <Page key={index} className="m-5" pageNumber={pdf} />
        ))}
      </Document> */}
    </div>
  );
};

export default PrivacyPolicyPage;
