import app from './app';
import 'reflect-metadata';
import '@config/db';

app.listen(process.env.PORT, () => {
  console.log('>>>Running Server in port '+process.env.PORT);
});
