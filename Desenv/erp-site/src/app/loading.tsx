"use client";
import React, { useEffect } from "react";
import { Skeleton } from "primereact/skeleton";

export default function Loading() {
  return (
    <>
      <div className="flex mt-12rem">
        <div className="field col-12 md:col-6 mt-12">
          <Skeleton className="mb-2"></Skeleton>
          <Skeleton width="10rem" className="mb-2"></Skeleton>
          <Skeleton width="5rem" className="mb-2"></Skeleton>
          <Skeleton height="2rem" className="mb-2"></Skeleton>
          <Skeleton width="10rem" height="4rem"></Skeleton>
          <Skeleton className="mb-2"></Skeleton>
          <Skeleton width="10rem" className="mb-2"></Skeleton>
          <Skeleton width="5rem" className="mb-2"></Skeleton>
          <Skeleton height="2rem" className="mb-2"></Skeleton>
          <Skeleton width="10rem" height="4rem"></Skeleton>
          <Skeleton className="mb-2"></Skeleton>
          <Skeleton width="10rem" className="mb-2"></Skeleton>
          <Skeleton width="5rem" className="mb-2"></Skeleton>
          <Skeleton height="2rem" className="mb-2"></Skeleton>
          <Skeleton width="10rem" height="4rem"></Skeleton>
        </div>
        <div className="field col-12 md:col-6">
          <Skeleton className="mb-2" borderRadius="16px"></Skeleton>
          <Skeleton
            width="10rem"
            className="mb-2"
            borderRadius="16px"
          ></Skeleton>
          <Skeleton
            width="5rem"
            borderRadius="16px"
            className="mb-2"
          ></Skeleton>
          <Skeleton
            height="2rem"
            className="mb-2"
            borderRadius="16px"
          ></Skeleton>
          <Skeleton width="10rem" height="4rem" borderRadius="16px"></Skeleton>
          <Skeleton className="mb-2"></Skeleton>
          <Skeleton width="10rem" className="mb-2"></Skeleton>
          <Skeleton width="5rem" className="mb-2"></Skeleton>
          <Skeleton height="2rem" className="mb-2"></Skeleton>
          <Skeleton width="10rem" height="4rem"></Skeleton>
          <Skeleton className="mb-2"></Skeleton>
          <Skeleton width="10rem" className="mb-2"></Skeleton>
          <Skeleton width="5rem" className="mb-2"></Skeleton>
          <Skeleton height="2rem" className="mb-2"></Skeleton>
          <Skeleton width="10rem" height="4rem"></Skeleton>
        </div>
      </div>
    </>
  );
}
