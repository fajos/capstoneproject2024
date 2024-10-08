import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, pool
from logging.config import fileConfig
from alembic import context

# Load environment variables from .env file
load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your models' MetaData object here
from app.models import Base  # Import your SQLAlchemy models
target_metadata = Base.metadata

# Ensure DATABASE_URL is set, otherwise raise an error
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

# Set the sqlalchemy.url option in the config
config.set_main_option('sqlalchemy.url', database_url)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        connect_args={"check_same_thread": False}
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()