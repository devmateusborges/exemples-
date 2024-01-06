"use client";

import { AppProps } from "@utils/AppInterfaces";
import { Chip } from "primereact/chip";
import { useEffect, useState } from "react";

interface TagBlogProps extends AppProps {
  tags: any;
  typeRender: "grid" | "list";
}

const TagBlog: React.FC<TagBlogProps> = (props) => {
  const [classPrincipal, setClassPrincipal] = useState("");
  const [classScroll, setClassScroll] = useState("overflow-hidden");

  useEffect(() => {
    if (props.typeRender == "grid") {
      if (props.tags.length >= 6) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_min ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.tags.length >= 3) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_med ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.tags.length >= 1) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("h-1rem  style_font_max font-semibold ");
      }
    } else {
      if (props.tags.length >= 10) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_min ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.tags.length >= 7) {
        setClassPrincipal("");
        setClassScroll("h-6rem");
        setClassPrincipal("style_font_med ml-1");
        setClassScroll("h-6rem overflow-scroll scroll_blog");
      } else if (props.tags.length >= 1) {
        setClassPrincipal("");
        setClassScroll("");
        setClassPrincipal(" style_font_max font-semibold");
      }
    }
  }, []);

  return (
    <div className={`grid  ${classScroll} `}>
      {props.tags?.map((tag: any, index: any) => (
        <div className={`col-auto m-1`} key={tag + index}>
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
            template={
              <div className={`col-auto justify-center align-items-center`}>
                <span
                  style={{ color: tag.cms_tag_id_obj.color }}
                  className={`${classPrincipal} mr-1 pi pi-hashtag `}
                ></span>
                <span
                  style={{ color: tag.cms_tag_id_obj.color }}
                  className={`${classPrincipal}`}
                >
                  {tag.cms_tag_id_obj.sigla_tag}
                </span>
              </div>
            }
          />
        </div>
      ))}
    </div>
  );
};

export default TagBlog;
