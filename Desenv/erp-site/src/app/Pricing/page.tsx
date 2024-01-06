"use client";
import React, { useState, useEffect } from "react";
import AppHeader from "@components/AppHeader";
import { Card } from "primereact/card";
import { ScrollTop } from "primereact/scrolltop";
import { Button } from "primereact/button";

import PricingService from "@services/PricingService";

interface Pricing {
  key: number;
  id: number;
  titulo: String;
  conteudo: String;
  img: String;
}

const PricingPage: React.FC = (props) => {
  //===================================================
  const [cards, setCards] = useState<Pricing[]>([]);
  const PrincingService = new PricingService();

  //===================================================
  const getData = async () => {
    let data = await PrincingService.getData();
    setCards(data);
  };

  //===================================================
  useEffect(() => {
    getData();
  }, []);

  //===================================================

  // const max_button = styled.div`
  //   max-width: 195px;
  // `;
  return (
    <div className="sub-topbar w-12 grid flex  ">
      <AppHeader title="PREÇO" />
      {cards.map((card, index) => (
        <div
          className="mt-4 col-12 xl:col-4 md:col-6 pb-5 flex justify-content-center"
          v-for="card in cards"
          key={card.id}
          id={card.id.toString()}
        >
          <Card className="w-11 pt-3 pb-2">
            <div className="flex justify-content-center align-items-center">
              <i
                className="pi pi-check-circle text-green m-3"
                style={{ fontSize: "1.5rem" }}
              ></i>
              {card.titulo}
            </div>

            <div
              className="shadow-1 border-round p-3"
              style={{ overflow: "auto", height: "200px" }}
            >
              <p
                dangerouslySetInnerHTML={{ __html: card.conteudo.toString() }}
                className=""
              ></p>

              <ScrollTop
                target="parent"
                threshold={100}
                className="custom-scrolltop"
                icon="pi pi-arrow-up"
              />
            </div>
            <div className="grid col-12 p-2 mt-5 flex justify-content-around">
              <div
                className="
                    col-12
                    xl:col-6
                    lg:col-6
                    md:col-6
                    sm:col-12
                    p-2
                    flex
                    align-items-center
                    justify-content-center
                    flex-column
                  "
              >
                <h5 className="m-0 text-green font-bold mb-3">R$ 1,00/Mês</h5>
                <div className="w-full max_button">
                  <Button
                    className="w-full shadow-2"
                    //   TODO  @click="toSign('1')"
                    label="Semestral"
                  />
                </div>
              </div>
              <div
                className="
                    col-12
                    xl:col-6
                    lg:col-6
                    md:col-6
                    sm:col-12
                    p-2
                    flex
                    align-items-center
                    justify-content-center
                    flex-column
                  "
              >
                <h5 className="m-0 text-green font-bold mb-3">R$ 1,00/Mês</h5>
                <div className="w-full max_button">
                  <Button
                    className="w-full shadow-2"
                    // TODO @click="toSign('2')"
                    label="Anual"
                  />
                </div>
              </div>
            </div>
          </Card>
        </div>
      ))}
    </div>
  );
};

export default PricingPage;
