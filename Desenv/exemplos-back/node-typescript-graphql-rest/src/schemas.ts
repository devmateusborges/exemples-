import { loadFilesSync, mergeTypeDefs } from 'graphql-tools'
import path from 'path'

const mergePath = loadFilesSync(path.join(__dirname, 'modules/**/*.gql'))

const schemas = mergeTypeDefs(mergePath)

export default schemas
