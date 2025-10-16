from decouple import config

ADMIN_ID = config("ADMIN_ID")
TOEKN = config("TOKEN")


TORTOISE_ORM = {
    "connections": {
        "default": {
            # PostgreSQL uchun
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": config("DB_HOST", default="localhost"),
                "port": config("DB_PORT", default=5432, cast=int),
                "user": config("DB_USER", default="postgres"),
                "password": config("DB_PASSWORD"),
                "database": config("DB_NAME"),
            },
        }
    },
    "apps": {
        "models": {
            "models": ["database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
