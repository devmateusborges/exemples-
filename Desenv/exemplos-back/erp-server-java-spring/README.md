# 1 - Execução em desenvolvimento

LINUX: ```mvn spring-boot:run -Dspring-boot.run.profiles=dev```

WIN: ```mvnw spring-boot:run -Dspring-boot.run.profiles=dev```

# 2 - Execução migration com liquibase

LINUX: ```mvn liquibase:update -Pdev```

WIN: ```mvnw liquibase:update -Pdev```

