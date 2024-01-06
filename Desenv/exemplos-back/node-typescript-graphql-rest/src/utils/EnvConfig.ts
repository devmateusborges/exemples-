import dotenv from 'dotenv'
import { config as configDotenv } from 'dotenv'
import { resolve } from 'path'

console.log(`>>>Environment is ${process.env.NODE_ENV}`)

let pathenv: string

if (process.env.NODE_ENV == 'development') {
  pathenv = resolve(__dirname, '../../.env.development')
} else if (process.env.NODE_ENV == 'test') {
  pathenv = resolve(__dirname, '../../.env.test')
} else if (process.env.NODE_ENV == 'production') {
  pathenv = resolve(__dirname, '../../.env.production')
} else {
  throw new Error(`'NODE_ENV' ${process.env.NODE_ENV} is not handled!`)
}
console.log('>>>Environment Path:' + pathenv)
dotenv.config({ path: pathenv })
