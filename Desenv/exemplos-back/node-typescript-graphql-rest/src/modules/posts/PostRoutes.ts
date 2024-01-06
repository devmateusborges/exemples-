import { PostController } from '@modules/posts/PostController'
import { Router } from 'express'

const PostRoutes = Router()

const postController = new PostController()

PostRoutes.get('/posts/user/:id', postController.getPostsByUser)

export { PostRoutes }
