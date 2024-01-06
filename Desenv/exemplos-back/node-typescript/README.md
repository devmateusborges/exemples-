# TYPEORM

    typeorm migration:run -c test
    typeorm migration:run -c development
    typeorm migration:create -c development -n CreateUserBlaBla
    typeorm migration:generate -c development -n SyncBlaBla
    typeorm migration:run -c production