const config = {
    user:"mongodb",
    host:"18.230.73.37",
    database:"conndev",
    password:"AwsDb123",
    port:"27017"
 }

 module.exports ={config: 'mongodb://'+config.user+':'+config.password+'@'+config.host+':'+config.port+'/'+config.database  }

