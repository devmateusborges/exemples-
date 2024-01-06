export default [
  {
    "name": "test",
    "type": "postgres",
    "host": "localhost",
    "port": 5432,
    "username": "postgres",
    "password": "postgres",
    "database": "postgres",
    "entities": ["*/models/*.entity{.ts,.js}"],
    "synchronize": false,
    "migrationsTableName": "migrations",
    "migrations": ["src/migrations/*"],
    "cli": {
      "entitiesDir": "src/models",
      "migrationsDir": "src/migrations"
    },
    "logging": true
  },
  {
    "name": "development",
    "type": "postgres",
    "host": "localhost",
    "port": 5432,
    "username": "postgres",
    "password": "postgres",
    "database": "nodets",
    "entities": ["*/models/*.entity{.ts,.js}"],
    "synchronize": false,
    "migrationsTableName": "migrations",
    "migrations": ["src/migrations/*"],
    "cli": {
      "entitiesDir": "src/models",
      "migrationsDir": "src/migrations"
    },
    "logging": true
  },
  {
    "name": "production",
    "type": "postgres",
    "host": "localhost",
    "port": 5432,
    "username": "postgres",
    "password": "postgres",
    "database": "nodets",
    "entities": ["*/entities/*.entity{.js}"],
    "synchronize": false,
    "migrationsTableName": "migrations",
    "migrations": ["*/migration/*{.js}"],
    "cli": {
      "entitiesDir": "models",
      "migrationsDir": "migrations"
    },
    "logging": false
  }
]

  