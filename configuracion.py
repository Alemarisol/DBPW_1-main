from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///DBPW_001.db")
Session = sessionmaker(bind=engine)
