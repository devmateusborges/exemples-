import store from "src/store";
import { loading } from "@store/UtilStore";

const useApi = () => {
  const getApi = async (url: string, option: any) => {
    store.dispatch(loading(true));

    const result = await fetch(url, option);

    store.dispatch(loading(false));

    return result;
  };

  return { getApi };
};

export default useApi;
