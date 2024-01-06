//TODO http quando dev e https quando produção, ver forma de saber quando esta em produção

const args = process.argv
console.log(args)
let http
if (args[2] == 'https') {
    http = require('https')
} else {
    http = require('http')
}

var fs = require('fs');
require('dotenv').config()
console.log('==============================')
console.log('Init create file translate')
//==============================
const serverApi = process.env.REACT_APP_API_URL

//==============================
function getHttp(url, callback) {
    http.get(url, response => {
        data = ''
        response.on('data', chunk => {
            data += chunk
        })
        response.on('end', () => {
            callback(data)
        })
    })

}
//==============================
getHttp(`${serverApi}/auth/i18nlang`, data => {
    let langs = JSON.parse(data).items
    let locales = {}

    for (let lang of langs) {
        let langId = lang.id
        console.log('==============================')
        console.log('Init create file translate lang code [' + lang.code + ']')

        getHttp(`${serverApi}/auth/i18ntranslate/${langId}`, langTranslate => {
            locales[lang.code] = { translation: JSON.parse(langTranslate) }

            fs.promises.writeFile(`./src/assets/i18n/locales.json`, JSON.stringify(locales))
            console.log('==============================')
            console.debug(`File translate [${lang.code}] succesfully update`)
        })
    }


})

