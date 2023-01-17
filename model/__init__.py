import bcrypt
from sqlalchemy import event
from .bookmark import Bookmark
from .user import User
from .database import db


@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(
        User(username='jedsada', password=bcrypt.hashpw('3841'.encode('utf-8'), bcrypt.gensalt(10)),
             email='jedsada_kampen@hotmail.com'))
    db.session.add(
        User(username='jame', password=bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt(10)),
             email='jame@hotmail.com')),
    db.session.commit()