from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from src.config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
from src.menu.models import Models


config = context.config
section = config.config_ini_section
config.set_section_option(section, 'POSTGRES_HOST', POSTGRES_HOST)
config.set_section_option(section, 'POSTGRES_PORT', POSTGRES_PORT)
config.set_section_option(section, 'POSTGRES_DB', POSTGRES_DB)
config.set_section_option(section, 'POSTGRES_USER', POSTGRES_USER)
config.set_section_option(section, 'POSTGRES_PASSWORD', POSTGRES_PASSWORD)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Models.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
