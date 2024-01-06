# Define permissoes de leitura e gravacao para o diretorio
`chown -R postgres /usr/local/bkp/`
`chmod 0777 /usr/local/bkp/`

#Exclui backups mais antigos que 5 dias
find /usr/local/bkp/* -mtime +5 -delete

aws s3 cp /usr/local/bkp/$t s3://bkp-dados.resultfacil.com.br/ --recursive
