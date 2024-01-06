import { createConnection } from 'typeorm';


export const conn = createConnection(process.env.NODE_ENV);

