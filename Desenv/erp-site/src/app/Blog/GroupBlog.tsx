"use client";
import { AppProps } from "@utils/AppInterfaces";
import { Chip } from "primereact/chip";
import { useEffect, useState } from "react";
interface GroupBlogProps extends AppProps {
  groups: any;
  typeRender: "grid" | "list";
}

const GroupBlog: React.FC<GroupBlogProps> = (props) => {
  const [classPrincipal, setClassPrincipal] = useState("");
  const [classScroll, setClassScroll] = useState("overflow-hidden");

  useEffect(() => {
    if (props.typeRender == "grid") {
      if (props.groups.length >= 6) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_min ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
        console.log("AQUi ");
      } else if (props.groups.length >= 3) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_med ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog font-semibold");
      } else if (props.groups.length >= 1) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("h-1rem  style_font_max p-1 font-semibold");
      }
    } else {
      if (props.groups.length >= 10) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_min ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.groups.length >= 8) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_med ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.groups.length >= 1) {
        setClassPrincipal("");
        setClassScroll("");
        setClassPrincipal(" style_font_max font-semibold");
      }
    }
  }, []);

  return (
    <div className={`grid  ${classScroll}`}>
      {props.groups?.map((group: any, index: any) => (
        <div className={`col-auto m-1 align-items-center `} key={group + index}>
          <Chip
            className={`${
              group.cms_grupo_id_obj.color ? "white" : "text-color-secondary"
            }`}
            style={{
              border: `${
                group.cms_grupo_id_obj.color
                  ? "0.2px solid " + group.cms_grupo_id_obj.color
                  : "none"
              }`,
            }}
            template={
              <div
                style={{ color: group.cms_grupo_id_obj.color }}
                className={` col-auto justify-center align-items-center `}
              >
                <span className={` ${classPrincipal} mr-1 pi pi-tag`}></span>
                <span className={`${classPrincipal}`}>
                  {group.cms_grupo_id_obj.sigla_grupo}
                </span>
              </div>
            }
          />
        </div>
      ))}
    </div>
  );
};

export default GroupBlog;
