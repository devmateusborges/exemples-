import useApi from "@components/hooks/useApi";

export default class ContactService {
  getData = async () => {
    const { getApi } = useApi();

    const result = await getApi("assets/data/data-assistant.json", {
      cache: "no-store",
    });
    return (await result.json())?.data;
  };
}
