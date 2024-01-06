#!/bin/sh

# Define permissoes de leitura e gravacao para o diretorio
`chown -R mongodb /usr/local/bkp/`
`chmod 0777 /usr/local/bkp/`

# Formata data para adicionar ao nome dos arquivos
t=$(date +%Y%m%d%H%Mmongo.backup)

# Gera Bkp
`mongodump -h localhost:27017 --authenticationDatabase conndev -u mongodb -p AwsDb123 --gzip -o /usr/local/bkp/$t`



echo "Bkp mongo finalizado"

