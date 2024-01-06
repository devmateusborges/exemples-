const express = require('express');
const cors = require('cors');
const indexPgLambda = require('./indexpg');
const indexMgLambda = require('./indexmg');

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.json({ type: 'application/vnd.api+json' }));
app.use(cors());

const inputPostPg = (request, response) => {
  indexPgLambda.input(request).then((r) => {
    if (r.statusCode == 200) {
        response.status(200).send(r);
    } else {
        response.status(500).send(r.body);   
    }
  }).catch((e)=>{
  })
};

const inputPostMg = (request, response) => {
  indexMgLambda.input(request).then((r) => {
    if (r.statusCode == 200) {
        response.status(200).send(r);
    } else {
        response.status(500).send(r.body);   
    }
  }).catch((e)=>{
  })
};

app.route('/inputpg').post(inputPostPg);
app.route('/inputmg').post(inputPostMg);


app.listen(process.env.PORT || 3000, () => {
  console.log(`Servidor iniciado`);
});
