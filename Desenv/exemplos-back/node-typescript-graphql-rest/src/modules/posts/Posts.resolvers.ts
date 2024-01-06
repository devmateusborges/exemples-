import { container } from 'tsyringe'
import { PostService } from './PostService'

const postsResolvers = {
  Mutation: {
    createPost(_, { input }) {
      const postService = container.resolve(PostService)
      const post = postService.create(input)
      return post
    }
  },
  Query: {
    getPostByUser(_, { idUser }) {
      const postService = container.resolve(PostService)
      const posts = postService.getPostByUser(idUser)
      return posts
    }
  }
}

export default postsResolvers
