import { api } from "../../../utils/ApiUtil";
import BaseService from "../../GenericService";

const url_api = "tst/test1/";

export default class Test1Service extends BaseService {
  constructor() {
    super(url_api);
  }
}
