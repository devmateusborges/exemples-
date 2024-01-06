#!/bin/sh


# Define permissoes de leitura e gravacao para o diretorio
`chown -R postgres /usr/local/bkp/`
`chmod 0777 /usr/local/bkp/`

# Formata data para adicionar ao nome dos arquivos
t=$(date +%Y%m%d%H%M.backup)

# Gera Bkp
$(PGPASSWORD="AwsDb123#" pg_dump -h localhost -p 5432 -U postgres -F c -b -v -f "/usr/local/bkp/$t" rfdadosdev)


echo "Bkp postgres finalizado"

