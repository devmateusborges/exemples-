import store from "../../../store";
import { authProgramFavoriteAction } from "../../../store/AuthStore";
import { api } from "../../../utils/ApiUtil";
import { AuthService } from "../../AuthService";
import BaseService from "../../GenericService";

export default class SysProgramFavoriteService extends BaseService {
  constructor() {
    super("sys/sysprogramfavorite/");
  }
  // ==============================
  async list(params: any): Promise<any> {
    let resultAux = [];
    const { programFavorite } = await store.getState().auth;

    if (programFavorite?.total > 0 && params.cache) {
      resultAux = await programFavorite.items;

      // console.log("authListProgramFavorite-com-store");
    } else {
      const result = await api.get<any>(`${this.resource}getbyuserlogin/`, {
        params,
      });
      store.dispatch(authProgramFavoriteAction(result.data));

      resultAux = await result.data.items;

      // console.log("authListProgramFavorite-sem-store");
    }
    return resultAux;
  }

  // ==============================
  async favorite(sysProgramId: any, favorite: any): Promise<any> {
    const { user } = await store.getState().auth.auth;

    const result = await api.post<any>(`${this.resource}favorite/`, {
      sys_program_id: sysProgramId,
      sys_user_id: user.id,
      favorite,
    });

    if (result.status == 200) {
      const filterAux = {
        filter: {
          and: { login: user.login },
        },
      };

      // Atualiza store para atualizar menus
      this.list({ pfilters: filterAux });
      AuthService.authListProgram({ pfilters: filterAux, saveCache: true });
    }
    return result.data;
  }
}
