
from config import DB_FILE
from database.database import Base, engine
from database.models import BotMessage

if __name__ == "__main__":

    if DB_FILE.exists():
        try:
            BotMessage.__table__.drop(engine)
        except:
            pass

    Base.metadata.create_all(engine)
