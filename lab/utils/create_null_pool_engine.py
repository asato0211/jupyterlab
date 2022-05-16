import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

def create_null_pool_engine():
    db_url = os.getenv("DB_URL", "")
    engine = create_engine(db_url, poolclass=NullPool)
    return engine
