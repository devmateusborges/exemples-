"use client";
import React, { Key, useEffect, useRef } from "react";
import { Card } from "primereact/card";
import { ScrollTop } from "primereact/scrolltop";
import { Button } from "primereact/button";
import Image from "next/image";
import { AppProps, CardItem } from "../utils/AppInterfaces";

interface AppCardsProps extends AppProps {
  cards?: CardItem[];
  title?: React.ReactNode;
}

const AppCards: React.FC<AppCardsProps> = (props) => {
  return (
    <>
      <div className="w-12 grid flex">
        {props.cards ? (
          props.cards.map((item) => (
            <div
              key={item.id}
              className="col-12 xl:col-4 md:col-6 pb-5 flex justify-content-center"
            >
              <Card className="w-11">
                <slot name="header">
                  <div className="w-12 flex align-items-center justify-content-center">
                    <div>
                      {item.img ? (
                        <Image
                          src={`assets/images/${item.img}`}
                          height={150}
                          width={300}
                          alt="Imagem"
                        />
                      ) : (
                        <></>
                      )}
                    </div>
                  </div>
                </slot>
                <slot name="title">
                  <div className="flex justify-content-center text-3xl">
                    {item.titulo}
                  </div>
                </slot>

                <slot name="content">
                  <div
                    className="mb-4"
                    style={{ overflow: "auto", height: "200px" }}
                  >
                    <p dangerouslySetInnerHTML={{ __html: item.corpo }}></p>
                    <ScrollTop
                      target="parent"
                      threshold={100}
                      className="custom-scrolltop"
                      icon="pi pi-arrow-up"
                    />
                  </div>
                </slot>

                <slot name="footer">
                  <div className="flex justify-content-center">
                    {(() => {
                      if (item.assinar) {
                        return (
                          <Button
                            className="p-button-lg"
                            // TODO onclick={toSign(card.id)}
                            label="Assinar"
                          />
                        );
                      }
                    })()}
                  </div>
                </slot>
              </Card>
            </div>
          ))
        ) : (
          <></>
        )}
      </div>
    </>
  );
};

export default AppCards;
