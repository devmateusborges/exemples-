import useApi from "@components/hooks/useApi";

export default class VideosService {
  getData = async () => {
    const { getApi } = useApi();
    const result = await getApi("assets/data/data-videos.json", {
      cache: "no-store",
    });
    return (await result.json())?.data;
  };
}
