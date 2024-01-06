import 'reflect-metadata'

import express, { NextFunction, Request, Response } from 'express'
import 'express-async-errors'
import mongoose from 'mongoose'
import { graphqlHTTP } from 'express-graphql'
import { makeExecutableSchema } from 'graphql-tools'
import { container } from 'tsyringe'

import resolvers from './resolvers'
import typeDefs from './schemas'
import { PostRoutes, UserRoutes } from 'routes'
import { ResultDTO } from './utils/ResultDTO'

import './utils/EnvConfig'

import { DbOrmConfigService } from 'utils/DbOrmConfigService'
const dbOrmConfigService = container.resolve(DbOrmConfigService)
console.log('>>>Database: ' + dbOrmConfigService.getOrmConfig('database'))

mongoose.connect('mongodb://localhost:27017/code_drops', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

const app = express()

app.use(express.json())

app.use(PostRoutes)
app.use(UserRoutes)

const schema = makeExecutableSchema({
  resolvers,
  typeDefs
})

app.use(
  '/graphql',
  graphqlHTTP({
    schema,
    graphiql: true
  })
)

app.use(
  (error: Error, request: Request, response: Response, next: NextFunction) => {
    if (error instanceof Error) {
      return response
        .status(400)
        .json(new ResultDTO(false, null, error.message))
    }

    return response.status(500).json(error)
  }
)

const port = process.env['PORT']

app.listen(port, () => console.log(`>>>Server is running port: ${port}`))
