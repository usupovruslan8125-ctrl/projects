from data import db_session
from data.users import User

db_name = input()
db_session.global_init(db_name)
db_sess = db_session.create_session()
db_sess.query(User).filter(User.address == "module_1", User.age < 21).update(
    {"address": "module_3"}
)
db_sess.commit()
for user in db_sess.query(User).filter(User.address == "module_3"):
    print(user)