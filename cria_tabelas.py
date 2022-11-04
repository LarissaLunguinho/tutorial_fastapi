#isso nao é ideal, é uma gambiarra
import sqlalchemy
from config import DATABASE_URL, metadata
from models.papel import Papel

def config_banco(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == '__main__':
    config_banco()

    #https://www.youtube.com/watch?v=OPISTCOCvZc&list=PLstjCH2DwkBnKO9PdHc5NO1JOwbJdcq22&index=7