import useApi from "@components/hooks/useApi";

export default class TrainingService {
  getData = async () => {
    const { getApi } = useApi();
    const result = await getApi("assets/data/data-training.json", {
      cache: "no-store",
    });
    return (await result.json())?.data;
  };
}
