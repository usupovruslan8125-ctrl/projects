from db_session import global_init, create_session
from users import User

db_name_1 = input()
db_name_2 = input()

global_init(db_name_1)
db_sess = create_session()
db_sess.query(User).filter(User.address == "module_1", User.age < 21).update(
    {"address": "module_3"}
)
db_sess.commit()

global_init(db_name_2)
db_sess = create_session()
for user in db_sess.query(User).filter(User.address == "module_3"):
    print(user)
