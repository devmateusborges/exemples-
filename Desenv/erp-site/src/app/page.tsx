"use client";
import React from "react";

import { Card } from "primereact/card";
import { Button } from "primereact/button";
import AppContact from "@components/AppContact";
import AppButtonScrollTop from "@components/AppButtonScrollTop";
import AppCardSolutions from "@components/AppCardSolutions";
import Image from "next/image";
import AppCardDemonstration from "@components/AppDemonstration";
import { AppProps, DataVideos } from "@utils/AppInterfaces";
import { useEffect, useState } from "react";
import AppCardCheckList from "@components/AppCardCheckList";
import { Divider } from "primereact/divider";
import { SpeedDial } from "primereact/speeddial";
import { event } from "nextjs-google-analytics";
import VideosService from "@services/VideosService";

const HomePage: React.FC = () => {
  const videosService = new VideosService();
  const [dataVideos, setDataVideos] = useState<DataVideos[]>([]);

  useEffect(() => {
    videosService.getData().then((data: any) => setDataVideos(data));
  }, []);

  return (
    <>
      <div className=" sub-topbar ">
        <AppButtonScrollTop />

        <div className="grid ">
          <div
            className="
            col-12
            lg:col-8
            xl:col-8
            md:col-8
            
            flex flex-column
            align-items-center  
            
            h-full
            pb-5
            
          "
          >
            <div className="flex flex-column  justify-content-start align-items-center w-full   md:h-15rem lg:h-20rem xl:h-20rem  teste-bc "></div>

            <div className="flex flex-column  align-items-center lg:w-full xl:w-full mb-3 mt-3  ">
              <div className="flex  justify-content-center lg:flex lg:justify-content-center xl:flex xl:justify-content-center w-full ">
                <Image
                  src="/assets/images/resultagro.svg"
                  className=" w-3 md:w-4 lg:w-2 xl:w-2 lg:m-3 xl:m-3"
                  alt={""}
                  width={100}
                  height={100}
                />
                <Image
                  src="/assets/images/resultbordo.svg"
                  className=" w-3 md:w-4 lg:w-2 xl:w-2 lg:m-3 xl:m-3"
                  alt={""}
                  width={100}
                  height={100}
                />
                <Image
                  src="/assets/images/resultbov.svg"
                  className=" w-3 md:w-4 lg:w-2 xl:w-2 lg:m-3 xl:m-3"
                  alt={""}
                  width={100}
                  height={100}
                />
              </div>
            </div>

            <div className="flex flex-column justify-content-center align-items-center w-full scalein animation-duration-1000 animation-iteration-infinite ">
              <div>
                <Button
                  className="p-button-outlined w-auto font-bold lg:h-3rem xl:h-3rem lg:text-3xl xl:text-3xl border-round"
                  label="TESTE GRÁTIS"
                  onClick={() => {
                    event("click_test_free", {
                      category: "AppCardDemonstration",
                      label: "Click test free",
                    });
                    window.open("/web/#/signup", "_blank");
                  }}
                >
                  <i className="pi pi-heart  ml-2 text-3xl"></i>
                </Button>
              </div>
              <div className="mt-2">
                <label className="text-600 font-bold  xl:text-md lg:text-md">
                  Sem cartão de credito
                </label>
              </div>
            </div>
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-4
          flex
          align-items-center
          flex-column
          lg:justify-content-start
          justify-content-center
          border-left-1
          border-400
        "
          >
            <div className="flex blue w-full align-items-center justify-content-center p-3 mb-4 ">
              <i className="pi pi-comments text-50 text-6xl"></i>
              <a className="text-center text-xl text-50 ml-5">
                <strong>SOLICITE </strong>
                <br />
                Demonstração <strong>GRATUITA</strong> do software
              </a>
            </div>

            <AppContact option={1} />
          </div>
        </div>

        <div className="grid white">
          <AppCardDemonstration
            text1="O QUE OFERECEMOS?"
            text2="Abaixo detalhamos todos nossos modulos"
          />
          <div className="col-12 lg:col-4 xl:col-4 md:col-6  flex flex-column p-5">
            <AppCardCheckList
              checklist={[
                "Controle de múltiplas contas bancárias",
                "Fluxo de caixa e extrato",
                "Conciliação bancária",
                "Contas apagar e a receber",
                "Apropriação de custos",
                "Gestão de estoque",
                "Gestão da produção e armazenamento",
                "Controle de vendas",
                "Emissão de nota fiscal eletrônica de venda e remessa de produção",
              ]}
              title={"Gestão Financeira e Comercialização"}
            />
          </div>

          <div className="col-12 lg:col-4 xl:col-4 md:col-6  flex flex-column p-5">
            <AppCardCheckList
              checklist={[
                "Mapeamento dostalhões",
                "Planejamento da safra",
                "Planejamento e realização de atividades",
                "Controle dos custos da safra e dos talhões",
                "Resultados da safra e dos talhões",
              ]}
              title={"Operações Agrícolas"}
            />
          </div>
          <div
            className="
              col-12
              lg:col-4
              xl:col-4
              md:col-12
              flex flex-column
              p-5
            "
          >
            <AppCardCheckList
              checklist={[
                "Controle de combustível e peças",
                "Indicadores de desempenho",
                "Manutenções preventivas",
                "Histórico de atividades",
              ]}
              title={"Gestão de Patrimônio e Máquinas"}
            />
          </div>
        </div>

        <div className="grid">
          <AppCardDemonstration
            text1="QUEM SOMOS NÓS ?"
            text2="Nossa PLATAFORMA se adapta perfeitamente à rotina das fazendas e vai
                  te ajudar a economizar tempo e melhorar sua comunicação com os
                  produtores."
          />
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          hidden
          lg:flex
          md:flex
          xl:flex
          align-items-center
          flex-column
          justify-content-center
          p-5
          white
        "
          >
            <div className="img-interview mt-5"></div>
          </div>

          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
          white
        "
            id="consultor_agronomico"
          >
            <Card className="AppBase">
              <h1 className=" xl:text-left sm:text-center md:text-left text-blue">
                Uma PLATAFORMA de gestão agrícola
              </h1>

              <h2 className="xl:text-left sm:text-center md:text-left text-green font-bold">
                <i className="pi pi-check-circle text-4xl text-green mr-2"></i>
                Simple e Objetivo
              </h2>

              <p className="text-secondary xl:text-left sm:text-center md:text-left">
                Você trabalha com todo o processo produtivo documentado e tem
                acesso simplificado às informações da fazenda.
              </p>
            </Card>
          </div>
        </div>
        <div className="grid white">
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          justify-content-center
          flex flex-column
          p-5
        "
          >
            <AppCardSolutions
              title="Planejamento de safra"
              content="Monte o calendário de atividades agrícolas, definindo as
              aplicações que serão feitas em cada talhão."
              comingSoon={false}
            />
          </div>

          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Controle pelo seu celular"
              content="Acesse a PLATAFORMA pelo seu celular e faça registros diretamente do campo, mesmo sem internet."
              comingSoon={false}
            />
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Relatórios em um clique"
              content="Verifique a evolução do cultivo por relatórios e faça
                recomendações assertivas ao produtor."
              comingSoon={false}
            />
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Monitoramento de pragas e doenças"
              content="Controle focos de infestação na lavoura. Assim, você economiza
              custos com aplicações e tem uma melhor gestão de defensivos
              agrícolas."
              comingSoon={false}
            />
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Mapas NDVI"
              content="Monitore a plantação por imagens de satélite e poupe tempo na
              detecção de anomalias, focando o manejo onde é mais necessário."
              comingSoon={true}
            />
          </div>
          <AppCardDemonstration
            text1="ASSISTA NOSSOS VÍDEOS"
            text2="Você entendera oque é a nossa PLATAFORMA"
          />
        </div>
        <div className="grid white">
          <div className="grid flex justify-content-center w-full ">
            {dataVideos.map((video, index) => (
              <div
                key={video.name}
                className="
            col-12
            
            md:col-8
            lg:col-6
            lg:p-5
            xl:p-5
            flex
            align-items-center
            justify-content-center
          "
              >
                <video
                  className="div-video"
                  controls
                  poster="/assets/images/resultfacil-frame.svg"
                  style={{ borderRadius: "25px" }}
                >
                  <source
                    src={`/assets/videos/${video.name}`}
                    type="video/mp4"
                  />
                </video>
              </div>
            ))}
          </div>
        </div>
        <AppCardDemonstration
          text1="SEJA NOSSA PARCEIRO"
          text2="Sendo nosso parceiro, você poderá ampliar suas soluções para sesus clientes com qualidade e agilidade"
        />

        <div className="grid white">
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          hidden
          lg:flex
          md:flex
          xl:flex
          justify-content-center
          align-items-center
          flex-column
          p-5
        "
          >
            <div className="img-space mt-5"></div>
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <Card className="AppBase">
              <h1 className=" xl:text-left sm:text-center text-blue">
                Benefícios de ser uma consultoria parceira
              </h1>

              <h2 className=" xl:text-left sm:text-center text-green font-bold">
                <i className="pi pi-check-circle text-4xl text-green mr-2"></i>
                Proporcionamos mais visibilidade aos nossos parceiros.
              </h2>

              <p className="text-secondary xl:text-left sm:text-center">
                A sua consultoria ganha um espaço de divulgação no nosso
                <label className=""> Portal de Consultores</label>. Criamos este
                site para facilitar o acesso de produtores rurais aos seus
                serviços. Potenciais clientes da sua região podem te encontrar
                com uma busca rápida e entrar em contato por e-mail ou WhatsApp.
              </p>
            </Card>
          </div>
        </div>

        <div className="grid white">
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Ofereça inovação"
              content="       Aliando um software de gestão agrícola à sua expertise, você pode
              expandir seu catálogo de serviços e aumentar a sua entrega de
              valor aos produtores."
            />
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Marketing"
              content="       Participe de eventos em nível nacional e diversifique os seus
              canais de comunicação. Conte com um time de especialistas para te
              ajudar a posicionar a sua marca no mercado."
            />
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Vendas"
              content="       Realize treinamentos de venda e receba apoio para o fechamento de
              negócios. Vamos te ajudar a contornar objeções e a destacar o
              impacto do seu serviço na lucratividade das propriedades."
            />
          </div>
          <div
            className="
          col-12
          lg:col-6
          xl:col-6
          md:col-6
          
          justify-content-center
          flex flex-column
          p-5
        "
          >
            <AppCardSolutions
              title="Expanda seu negócio"
              content="        Vamos te ajudar a economizar tempo, aumentando seu potencial de
              atendimento. Reduza o trabalho operacional e dedique-se a expandir
              sua carteira de clientes."
            />
          </div>
        </div>
        <AppCardDemonstration
        // TODO :whatzapp="whatzapp"
        />

        <div className="grid">
          <div
            className="
          col-12
          lg:col-12
          xl:col-12
          md:col-12
          
          justify-content-center
          flex
          align-items-center
          flex-column
          p-5
          white
        "
          >
            <Card className="AppBase">
              <h1 className=" xl:text-left sm:text-center md:text-left text-blue">
                Soluções integradas ao RESULTFACIL
              </h1>
            </Card>
          </div>
        </div>

        <div className="grid white">
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          justify-content-center
          flex flex-column
          p-5
        "
          >
            <AppCardSolutions
              title="Monitoramento de Pragas e Doenças"
              comingSoon={false}
            />
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          justify-content-center
          flex flex-column
          p-5
        "
          >
            <AppCardSolutions
              title="Imagens de Satélite e Análises NDVI"
              comingSoon={true}
            />
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Livro Caixa Digital do Produtor Rural"
              comingSoon={false}
            />
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Integração com Climatempo"
              comingSoon={true}
            />
          </div>
          <div
            className="
          col-12
          lg:col-4
          xl:col-4
          md:col-6
          
          flex
          align-items-center
          flex-column
          justify-content-center
          p-5
        "
          >
            <AppCardSolutions
              title="Integração com Climate FieldView™"
              comingSoon={true}
            />
          </div>
        </div>
        <AppCardDemonstration />
      </div>
    </>
  );
};

export default HomePage;
