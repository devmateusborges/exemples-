import { api } from "../../../utils/ApiUtil";
import BaseService from "../../GenericService";

const url_api = "tst/test1fk/";

export default class Test1FkService extends BaseService {
  constructor() {
    super(url_api);
  }
}
