import Post from '@models/Post'
import { injectable } from 'tsyringe'

interface IPostRequest {
  content: string
  author: string
}

@injectable()
class PostService {
  async create(data: IPostRequest) {
    const post = await Post.create(data)
    return post
  }

  async getPostByUser(id: string) {
    const posts = await Post.find({
      author: id
    })
      .populate('author')
      .exec()
    return posts
  }
}

export { PostService }
