'use strict';

const mongoose = require('mongoose');
const Promise = require('bluebird');
const db = require('./config/dbmg');

mongoose.Promise = Promise;

const BorMovModel = mongoose.model('bordo', {
  name: {
    type: String
  }
});


module.exports.input = async (event) => {
  console.log('input', 'Iniciando');
  var data = null;
  try {
    data = JSON.parse(event.body);
  } catch (error) {
    data = event.body;
  }

  try {
    
    const borMov = new BorMovModel({
      name: data.name
    });

    console.log('input', 'Antes inserir');
    
    await mongoose.connect(db.config,{ useNewUrlParser: true, useUnifiedTopology: true }); 
    const insert = await borMov.save();

    console.log('input', 'Depois inserir');

    return {
      statusCode: 200,
      body: JSON.stringify(insert),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify(error),
    };
  }
};
