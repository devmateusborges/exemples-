"use client";
import AppHeader from "@components/AppHeader";
import React, { useEffect, useState } from "react";
//import { Document, Page, pdfjs } from "react-pdf";

const TermsUsePage: React.FC = () => {
  const [numPages, setNumPages] = useState<number>();
  const [pageNumber, setPageNumber] = useState<number[]>([
    1, 2, 3, 4, 5, 6, 7, 8, 9,
  ]);

  const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
    setNumPages(numPages);
  };

  return (
    <div className="sub-topbar  ">
      <AppHeader title="TERMOS DE USO" className="" />
      <div className=" col-12 align-items-center  justify-content-center">
        {/* <Document
          className="grid align-items-center  justify-content-center"
          file="/assets/pdf/politica-privacidade.pdf"
          onLoadSuccess={onDocumentLoadSuccess}
        >
          {pageNumber.map((pdf: any, index: any) => (
            <Page key={index} className="m-5" pageNumber={pdf} />
          ))}
        </Document> */}
      </div>
    </div>
  );
};

export default TermsUsePage;
