import useApi from "@components/hooks/useApi";

export default class PricingService {
  getData = async () => {
    const { getApi } = useApi();
    const result = await getApi("assets/data/data-pricing.json", {
      cache: "no-store",
    });
    return (await result.json())?.data;
  };
}
