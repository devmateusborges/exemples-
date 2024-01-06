"use client";
import React, { useState, useEffect, useRef } from "react";
import AppHeader from "@components/AppHeader";
import { DataView, DataViewLayoutType } from "primereact/dataview";
import Image from "next/image";
import { CardItemBlog } from "@utils/AppInterfaces";
import useDebounce from "@components/hooks/useDebounce";
import { BlogService } from "@services/BlogService";
import { Button } from "primereact/button";
import { SelectButton } from "primereact/selectbutton";
import { InputText } from "primereact/inputtext";
import Agronegocio from "../../../public/assets/images/agronegocio.svg";
import { Dialog } from "primereact/dialog";
import { Chip } from "primereact/chip";
import { Divider } from "primereact/divider";
import { ScrollTop } from "primereact/scrolltop";
import AppCardCheckList from "@components/AppButtonScrollTop";
import { formatDateTimeColumn } from "@utils/FuncUtil";
import RenderTags from "./TagBlog";
import TagBlog from "./TagBlog";
import GroupBlog from "./GroupBlog";
import SearchBlog from "./SearchBlog";

const BlogPage: React.FC = () => {
  //===================================================
  const { debounce } = useDebounce();
  const [search, setSearch] = useState("");
  const [dataCards, setDataCards] = useState<CardItemBlog[]>();
  const [layout, setLayout] = useState<DataViewLayoutType>("grid");
  const [loading, setLoading] = useState(true);
  const [first, setFirst] = useState(0);
  const rows = useRef(10);
  const [totalRecords, setTotalRecords] = useState(0);
  const [pageIndex, setPageIndex] = useState(1);
  const [displayBasic, setDisplayBasic] = useState<boolean>(false);
  const [cardMoment, SetcardMoment] = useState<any>();
  const [psortOrder, setSortOrder] = useState("");
  const [sortfild, setSortfild] = useState("");

  //===================================================
  const ViewOptions = [
    { name: "Lista", icon: "pi pi-bars", value: "list" },
    { name: "Grade", icon: "pi pi-th-large", value: "grid" },
  ];
  const OrderOptions = [
    { name: "Odenar por data  ", icon: "pi pi-sort", value: "DESCDATE" },
    {
      name: "Odenar por titulo",
      icon: "pi pi-sort-alpha-down-alt",
      value: "DESCTITLE",
    },
  ];

  //===================================================

  useEffect(() => {
    (async () => {
      console.log("DATAAA >>>>>>", sortfild);
      console.log("TITULOO >>>>>", psortOrder);
      if (search) {
        setLoading(true);
        handleSearchData(search, sortfild, psortOrder);
      } else {
        setLoading(true);
        handlePageData(pageIndex, sortfild, psortOrder);
      }
    })();
  }, [pageIndex, search, psortOrder]);

  //===================================================
  // Buscar dados Service api
  //===================================================

  const handleSearchData = async (
    pSearch: string,
    psortfild: any,
    porder: any
  ) => {
    debounce(async () => {
      const result = await BlogService.List(
        pageIndex,
        10,
        pSearch,
        psortfild,
        porder
      );

      setTotalRecords(result.total);
      setDataCards(result.items);
      setPageIndex(1);
      setLoading(false);
    });
  };

  const handlePageData = async (
    ppageIndex: number,
    psortfild: any,
    porder: any
  ) => {
    const result = await BlogService.List(
      ppageIndex,
      10,
      "%",
      psortfild,
      porder
    );
    setTotalRecords(result.total);
    setDataCards(result.items);
    setLoading(false);
  };

  //===================================================
  // Dialog Active
  //===================================================
  const handleClickDialog = (data: any) => {
    setDisplayBasic(true);
    SetcardMoment(data);
  };

  const handleHideDialog = () => {
    setDisplayBasic(false);
  };

  //===================================================
  // Pagination Dataview
  //===================================================

  const handleDataviewPage = (event: any) => {
    setLoading(true);
    const startIndex = event.first;
    setPageIndex(event.page + 1);
    setFirst(startIndex);
    setLoading(false);
  };

  //===================================================
  // Cards Render Dataview
  //===================================================

  const renderGridItem = (data: any) => {
    return (
      <>
        <div className="col-12  md:col-4 ">
          <div className="blog-grid-item card ">
            <div
              className="blog-grid-item-content cursor-pointer"
              onClick={() => handleClickDialog(data)}
            >
              <Image src={Agronegocio} alt="" width={500} height={100} />
              <Divider />
              <div className="blog-name">
                <p className="font-bold ">{data?.titulo}</p>
              </div>
              <div className="blog-corpo text-600 p-1">
                <p className="capitalize   text-base ">
                  {data?.corpo.substring(0, 250) + "..."}
                </p>
              </div>
            </div>
            <Divider />
            <div className="blog-grid-item-top  overflow-hidden">
              <TagBlog tags={data?.cms_post_tag_childs} typeRender="grid" />
              <GroupBlog
                groups={data?.cms_post_grupo_childs}
                typeRender="grid"
              />
            </div>
            <div className="blog-grid-item-Date">
              <div>
                <p className="font-semibold p-date text-600">
                  {data?.sys_user_id_obj.email}
                </p>
              </div>
              <div>
                <p className="font-semibold p-date text-600">
                  {formatDateTimeColumn(new Date(data.log_date_ins))}
                </p>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  };

  const renderListItem = (data: any) => {
    return (
      <div
        className="col-12 cursor-pointer"
        onClick={() => handleClickDialog(data)}
      >
        <div className="blog-list-item ">
          <div className="m2">
            <Image src={Agronegocio} alt="" width={100} height={100} />
          </div>
          <div className="blog-list-detail ml-5">
            <div className="blog-name">
              <p className="font-bold">{data.titulo}</p>
            </div>
            <div className="blog-description ">
              <p className="font-font-semibold text-600 capitalize text-base ">
                {data?.corpo.substring(0, 250) + "..."}
              </p>
            </div>
            <div className="grid  overflow-hidden w-12 ">
              <div className=" flex  flex-column w-12 h-7rem">
                <TagBlog tags={data?.cms_post_tag_childs} typeRender="list" />
                <GroupBlog
                  groups={data?.cms_post_grupo_childs}
                  typeRender="list"
                />
              </div>
            </div>
            <div className="grid">
              <div className="col-5">
                <p className="font-semibold text-base text-600">
                  {data?.sys_user_id_obj.email}
                </p>
              </div>
              <div className="col-5">
                <p className="font-semibold text-base p-date text-600">
                  {formatDateTimeColumn(new Date(data.log_date_ins))}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  const handleGridList = (pcard: any, playout: any) => {
    if (!pcard) {
      return;
    }
    if (playout === "list") return renderListItem(pcard);
    else if (playout === "grid") return renderGridItem(pcard);
  };

  //===================================================
  // Heder Dialog Options
  //===================================================

  const renderHeaderSelectTemplate = (option: any) => {
    return (
      <div className="justify-center align-items-center">
        <i className={option.icon}></i>
        <span className="ml-1">{option.name}</span>
      </div>
    );
  };

  const handleOptSelect = (e: any) => {
    if (e == "DESCDATE") {
      setSortfild("log_date_ins");
      setSortOrder(psortOrder == "desc" ? "asc" : "desc");
      setLayout("grid");
    } else if (e == "DESCTITLE") {
      setSortfild("titulo");
      setSortOrder(psortOrder == "desc" ? "asc" : "desc");
    } else {
      setLayout(e);
    }
  };

  const renderHeaderDataViewTemplate = () => {
    return (
      <div className="grid w-12 align-items-center justify-center">
        <div className="flex flex-column col align-items-center">
          <SelectButton
            value={layout}
            options={ViewOptions}
            onChange={(e) => handleOptSelect(e.target.value)}
            itemTemplate={renderHeaderSelectTemplate}
            optionLabel="value"
          />
        </div>
        <div className="flex flex-column col align-items-center">
          <SelectButton
            value={layout}
            options={OrderOptions}
            onChange={(e) => handleOptSelect(e.target.value)}
            itemTemplate={renderHeaderSelectTemplate}
            optionLabel="value"
          />
        </div>
      </div>
    );
  };

  const header = renderHeaderDataViewTemplate();

  //===================================================

  return (
    <div className="sub-topbar">
      <AppHeader title="BLOG" />
      <SearchBlog items={dataCards} onChangeAction={(e) => setSearch(e)} />

      <div className="card">
        <DataView
          value={dataCards}
          layout={layout == "DESC" ? "grid" : layout}
          header={header}
          itemTemplate={handleGridList}
          lazy
          paginator
          paginatorPosition={"both"}
          rows={rows.current}
          totalRecords={totalRecords}
          first={first}
          onPage={handleDataviewPage}
          loading={loading}
          emptyMessage={"Nenhum registro encontrado"}
        />
      </div>

      <Dialog
        header={
          <div className="">
            <p className="font-bold text-center">{cardMoment?.titulo}</p>
          </div>
        }
        visible={displayBasic}
        className="sm:h-40rem sm:w-12 xl:w-12 blog_dialog"
        onHide={() => handleHideDialog()}
      >
        <div className="flex flex-column align-items-center justify-center w-12">
          <div className="w-9 col-12 justify-center align-items-center overflow-hidden bg-red h-19rem border-round-2xl">
            <Image src={Agronegocio} alt={"Imagem"} width={970} />
          </div>

          <Divider align="center">
            {cardMoment?.cms_post_tag_childs.map((tag: any, index: any) => (
              <Chip
                className={`${
                  tag.cms_tag_id_obj.color ? "white" : "text-color-secondary"
                }`}
                style={{
                  border: `${
                    tag.cms_tag_id_obj.color
                      ? "0.2px solid " + tag.cms_tag_id_obj.color
                      : "none"
                  }`,
                }}
                key={tag + index}
                label={tag.cms_tag_id_obj.sigla_tag}
                icon="pi pi-hashtag"
              />
            ))}
          </Divider>
          <div className="col-12 sm:p-3 lx:p-8">
            <p className="capitalize   text-base ">{cardMoment?.corpo}</p>
          </div>
          <Divider align="center">
            <span className="p-tag">Detalhes da Puplicação</span>
          </Divider>
          <div className="flex blog_dialog_footer  w-12">
            <div className="flex  w-5 ">
              <span className="pi pi-user text-4xl"></span>
              <p className="ml-2">{cardMoment?.sys_user_id_obj.name}</p>
            </div>
            <div className="flex  w-5">
              <span className="pi pi-envelope text-4xl"></span>
              <p className="ml-2">{cardMoment?.sys_user_id_obj.email}</p>
            </div>
            <div className="flex  w-5 ">
              <span className="pi pi-calendar-minus text-4xl "></span>
              <p className="ml-2">
                {formatDateTimeColumn(new Date(cardMoment?.log_date_ins))}
              </p>
            </div>
          </div>
        </div>
        <ScrollTop
          target="parent"
          threshold={100}
          className="custom-scrolltop"
          icon="pi pi-arrow-up"
        />
      </Dialog>

      <AppCardCheckList />
    </div>
  );
};

export default BlogPage;
