#给数据库读入数据
from app import User, Movie, db
user = User(name='wenyou')
m1 = Movie(title='Leon', year='1994')
m2 = Movie(title='Mahjong', year='1996')
db.session.add(user)
db.session.add(m1)
db.session.add(m2)
db.session.commit()


