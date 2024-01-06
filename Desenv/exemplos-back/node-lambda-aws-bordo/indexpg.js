'use strict';

const db = require('./config/dbpg');

module.exports.input = async (event) => {
  console.log('input', 'Iniciando');
  var data = null;
  try {
    data = JSON.parse(event.body);
  } catch (error) {
    data = event.body;
  }

  try {
    const pool = await db.pool.connect();

    console.log('input', 'Antes inserir');

    const insert = await pool.query('INSERT INTO test (name) VALUES ($1)', [
      data.name,
    ]);

    console.log('input', 'Depois inserir');

    pool.release();

    return {
      statusCode: 200,
      body: JSON.stringify(data),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify(error),
    };
  }
};
