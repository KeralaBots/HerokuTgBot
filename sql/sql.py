import threading

from sqlalchemy import Column, Integer, UnicodeText, String, ForeignKey, UniqueConstraint, func

from sql.base import BASE, SESSION

class Heroku(BASE):
    __tablename__ = "heroku"
    user_id = Column(Integer, primary_key=True)
    heroku = Column(String(32), default=True)

    def __init__(self, user_id, true):
        self.user_id = user_id
        self.heroku = heroku


Heroku.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def heroku(user_id, true):
    with INSERTION_LOCK:
        time = SESSION.query(Heroku).filter(Heroku.user_id == user_id)
        if not time:
            time = Heroku(user_id, true)
            SESSION.add(time)
            SESSION.flush()
        #addtime = Time(user_id, true)
        #SESSION.add(addtime)
        SESSION.commit()

def get_key(user_id):
    time = SESSION.query(Heroku.heroku).filter(Heroku.user_id == user_id)
    SESSION.close()
    return time
