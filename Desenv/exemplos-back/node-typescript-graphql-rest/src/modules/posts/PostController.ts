import { Request, Response } from 'express'
import { container } from 'tsyringe'
import { PostService } from './PostService'

class PostController {
  async getPostsByUser(request: Request, response: Response) {
    const { id } = request.params

    const postService = container.resolve(PostService)
    const all = await postService.getPostByUser(id)
    return response.json(all)
  }
}

export { PostController }
