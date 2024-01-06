export class ResultDTO {
  status: string
  data: string
  error: string

  public constructor(status, data, error) {
    this.status = status
    this.data = data
    this.error = error
  }
}
