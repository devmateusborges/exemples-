import { Key } from "react";

export interface AppProps {
  id?: string;
  style?: object;
  className?: string;
  children?: React.ReactNode;
}

//=============================================================

//FOOTER BAR

//============================================================

export interface DataSocial {
  id?: Key;
  img: string;
  url: string;
}

export interface DataContact {
  endereco?: string;
  suporte?: string;
  nome?: string;
  numero?: string;
  email?: string;
}

//=============================================================

//CARD ITEM

//============================================================
export interface CardItem {
  id?: Key;
  titulo?: string;
  corpo: string;
  img?: string;
  assinar?: Boolean;
}
//=============================================================

//CARD POST Blog

//============================================================
export interface CardItemBlog {
  id?: Key;
  titulo?: string;
  corpo: string;
  img?: string;
  cms_post_tag_childs: [{ cms_tag_id_obj: { sigla_tag: any } }];
  cms_post_grupo_childs: [{ cms_grupo_id_obj: { sigla_grupo: any } }];
}

//=============================================================

//HOME SECTION 03

//============================================================
export interface DataEstatistic {
  id?: Key;
  numeroclientes?: string;
  numerohectares?: string;
  numerousuarios?: string;
}

export interface DataDepositions {
  id?: Key;
  cidade: string;
  img: string;
  nome: string;
  text: string;
  titulo: string;
}

//=============================================================

//HOME SECTION 04

//============================================================

export interface DataVideos {
  id: Key;
  titulo: string;
  name: string;
}

//=============================================================

//APPCONTATO Formulario

//============================================================

export interface DataForm {
  Nome?: string;
  Email?: string;
  Telephone?: string;
  Conteudo?: string;
  Dropdown?: string;
}
