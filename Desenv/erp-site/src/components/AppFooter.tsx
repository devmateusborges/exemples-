"use client";
import React, { useEffect, useState } from "react";
import ContactService from "../services/ContactService";
import SocialService from "../services/SocialService";
import { DataSocial, DataContact, AppProps } from "../utils/AppInterfaces";
import Link from "next/link";
import Image from "next/image";
import { useSelector, useDispatch } from "react-redux";
import { contatoOrigin } from "../store/UtilStore";
import moment from "moment";

interface AppFooterProps extends AppProps {}

const contactservice = new ContactService();
const socialService = new SocialService();

const AppFooter: React.FC<AppFooterProps> = (props) => {
  const utilDispatch = useDispatch();

  const [dataContact, setDataContact] = useState<DataContact[]>([{}]);
  const [dataSociais, setDataSociais] = useState<DataSocial[]>([]);
  const [yearRegister, setYearRegister] = useState("");
  const [versionBuild, setVersionBuild] = useState("");

  useEffect(() => {
    contactservice.getData().then((data: any) => setDataContact(data));
    socialService.getData().then((data: any) => setDataSociais(data));
    setYearRegister(moment().format("YYYY"));
    setVersionBuild(process.env.NEXT_PUBLIC_VERSION_BUILD || "");
  }, []);

  return (
    <div className="grid Appfooter-footer pb-5 pl-8 pr-8 pt-5 border-top-1 border-200">
      <div className="col-12 Appfooter-footer-card">
        <div className="footer-card-item justify-content-center align-content-center">
          <div className="grid flex footer-card-item-div align-content-center">
            <div className="col-12 sm:col-6 md:col-4 lg:col-4 xl:col-3">
              <ul className="Appfooter-ul-items">
                <li className="Appfooter-li-items font-bold">RESULTFACIL</li>
                <li className="Appfooter-li-items">
                  <Link href="/PrivacyPolicy" className="Appfooter-a">
                    Políticas de Privacidade
                  </Link>
                </li>
                <li className="Appfooter-li-items">
                  <Link href="/TermsUse" className="Appfooter-a">
                    Termos de Uso
                  </Link>
                </li>
              </ul>
            </div>
            <div className="col-12 sm:col-6 md:col-4 lg:col-4 xl:col-3">
              <ul className="Appfooter-ul-items">
                <li className="Appfooter-li-items font-bold">PRODUTOS</li>
                <li className="Appfooter-li-items">
                  <Link href="/Pricing" className="Appfooter-a">
                    Preço
                  </Link>
                </li>
              </ul>
            </div>
            <div className="col-12 sm:col-6 md:col-4 lg:col-4 xl:col-3">
              <ul className="Appfooter-ul-items">
                <li className="Appfooter-li-items font-bold">CONTEUDO</li>
                <li className="Appfooter-li-items">
                  <Link href="/Blog" className="Appfooter-a">
                    Blog
                  </Link>
                </li>
                <li className="Appfooter-li-items">
                  <Link href="/Training" className="Appfooter-a">
                    Treinamentos
                  </Link>
                </li>
                <li className="Appfooter-li-items">
                  <Link href="/HelpCenter" className="Appfooter-a">
                    Central de Ajuda
                  </Link>
                </li>
              </ul>
            </div>
            <div className="col-12 sm:col-6 md:col-4 lg:col-3 xl:col-3">
              <ul className="Appfooter-ul-items">
                <li className="Appfooter-li-items font-bold">FALE CONOSCO</li>

                <li className="Appfooter-li-items"> {dataContact[0].numero}</li>
                <li className="Appfooter-li-items"> {dataContact[0].email} </li>

                <li className="Appfooter-li-items">
                  <Link className="Appfooter-a" href={"/Contact"}>
                    Trabalhe Conosco
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div className="grid Appfooter-footer">
        <div className="col-12 Appfooter-footer-card">
          <div className="grid footer-card-item flex justify-content-center">
            <div
              className="
              col-12
              sm:col-12
              md:col-4
              lg:col-4
              footer-card-item-div
              justify-content-center
              lg:justify-content-end
              align-center
            "
            >
              <Link href="/">
                <Image
                  style={{ width: "140px" }}
                  className="cursor-pointer"
                  src="assets/images/resultfacil_branco.svg"
                  alt={""}
                  width={140}
                  height={140}
                />
              </Link>
            </div>
            <div
              className="
              col-12
              sm:col-12
              md:col-4
              lg:col-4
              footer-card-item-div
              justify-content-center
              align-items-center
            "
            >
              <Link href="https://play.google.com/store/apps/details?id=br.com.resultfacil">
                <Image
                  style={{ opacity: "1", width: "130px" }}
                  src="assets/images/google-play-badge.svg"
                  alt={""}
                  width={130}
                  height={130}
                />
              </Link>
              <Link href="https://play.google.com/store/apps/details?id=br.com.resultfacil">
                <Image
                  style={{ opacity: "1", width: "100px" }}
                  src="assets/images/AppStore.svg"
                  alt={""}
                  width={100}
                  height={100}
                />
              </Link>
            </div>
            <div
              className="
                          col-12
                          sm:col-12
                          md:col-12
                          lg:col-4
                          justify-content-center
                          lg:justify-content-start
                          footer-card-item-div
                          align-items-center
                          "
            >
              <div className="white border-round p-1">
                {dataSociais.map((media, index) => (
                  <Link
                    key={media.id}
                    target="_blank"
                    href={media.url}
                    rel="noreferrer"
                  >
                    <Image
                      key={media.id}
                      className="Appfooter-img-icon"
                      src={`assets/images-icons/${media.img}`}
                      alt={""}
                      height={100}
                      width={100}
                    />
                  </Link>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="grid Appfooter-footer pt-5">
        <div className="col-12 Appfooter-footer-card">
          <div className="grid footer-card-item">
            <div className="col-12 sm:col-4 md:col-4 lg:col-4 text-center mb-2">
              <span style={{ color: "#fff" }}>
                Copyright 2014 – {yearRegister} RESULTFACIL. Todos os direitos
                reservados.
              </span>
            </div>
            <div className="col-12 sm:col-4 md:col-4 lg:col-4 text-center">
              <span style={{ color: "#fff" }}> {dataContact[0].endereco} </span>
            </div>
            <div className="col-12 sm:col-4 md:col-4 lg:col-4 text-center">
              <span style={{ color: "#fff" }}> Build: {versionBuild} </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AppFooter;
