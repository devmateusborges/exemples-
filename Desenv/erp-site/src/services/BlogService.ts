import useApi from "@components/hooks/useApi";

let url_api = process.env.NEXT_PUBLIC_API_URL + "cms/cmspost";
export const List = async (
  ppage: number = 1,
  pper_page: number = 10,
  pterm: string = "%",
  Psortfild: string = "titulo",
  Psorttitle: string = "ASC"
): Promise<any> => {
  const { getApi } = useApi();
  const filter = `{"filter" : {"or" : {"titulo":{"like" : "%${pterm}%"},"corpo":{"like" : "%${pterm}%"}}},"sort" :{ "${Psortfild}" : "${Psorttitle}" }}`;
  console.log(
    "BlogService",
    `${url_api}?ppage=${ppage}&pper_page=${pper_page}&pfilters=${filter}`
  );
  const result = await getApi(
    `${url_api}?ppage=${ppage}&pper_page=${pper_page}&pfilters=${filter}`,
    { cache: "no-store" }
  );

  return await result.json();
};

export const BlogService = { List };
