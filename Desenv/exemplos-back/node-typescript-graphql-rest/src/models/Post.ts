import mongoose, { Schema, Document } from 'mongoose'

type Post = Document & {
  content: string
  author: string
}

const PostSchema = new Schema({
  content: String,
  createdAt: {
    type: 'Date',
    default: Date.now
  },
  author: {
    type: Schema.Types.ObjectId,
    ref: 'User'
  }
})

export default mongoose.model<Post>('Post', PostSchema)
