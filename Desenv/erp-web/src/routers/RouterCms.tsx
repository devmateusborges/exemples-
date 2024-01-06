import CmsGrupo from "../pages/modules/cms/CmsGrupo";
import CmsGrupoForm from "../pages/modules/cms/CmsGrupoForm";
import CmsPost from "../pages/modules/cms/CmsPost";
import CmsPostForm from "../pages/modules/cms/CmsPostForm";
import CmsTag from "../pages/modules/cms/CmsTag";
import CmsTagForm from "../pages/modules/cms/CmsTagForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cCmsgrupoId,
    path: "cms/cmsgrupo",
    element: <CmsGrupo />,
  },
  {
    programId: ConstProgramUtil.cCmsgrupoId,
    path: "cms/cmsgrupoform/:id",
    element: <CmsGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCmspostId,
    path: "cms/cmspost",
    element: <CmsPost />,
  },
  {
    programId: ConstProgramUtil.cCmspostId,
    path: "cms/cmspostform/:id",
    element: <CmsPostForm />,
  },
  {
    programId: ConstProgramUtil.cCmstagId,
    path: "cms/cmstag",
    element: <CmsTag />,
  },
  {
    programId: ConstProgramUtil.cCmstagId,
    path: "cms/cmstagform/:id",
    element: <CmsTagForm />,
  },
];
