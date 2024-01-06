var pg = require("pg");

const config = {
    user:"postgres",
    host:"18.230.73.37",
    database:"rfdadosdev",
    password:"AwsDb123#",
    port:"5432"
 }

const pool = new pg.Pool(config);

module.exports ={pool: pool}

