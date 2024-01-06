# ERP-WEB

## Tradução

1. Atualizando arquivo na pasta `src/assets/i18n/locales.json` com comando abaixo a tradução será requisitada do ERP-SERVER duvidas analizar arquivo na raís deste projeto `translate.js`

   ```
   npm run translate-update-local
   ```

## Build

1. Gerando build para teste
   ```
   npm run build
   ```
2. Após a geração do build iremos instalar um servidor local simples para servir os arquivos de build
   ```
   npm install -g serve@13.0.4
   ```
   ```
   serve -s build
   ```
   - Lemprado que para o build funcionar o ERP-SERVER deverá estar ativo
