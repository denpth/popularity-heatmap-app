from sqlalchemy import create_engine, orm, declarative_base
import os
engine=create_engine(os.getenv("DATABASE_URL","sqlite:///tmp.db"))
SessionLocal=orm.sessionmaker(bind=engine)
Base=declarative_base()
