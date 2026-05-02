from db_session import global_init, create_session
from users import User

db_name = input()
global_init(db_name)
db_sess = create_session()
for user in db_sess.query(User).filter(
    (User.position.like("%chief%")) | (User.position.like("%middle%"))
):
    print(f"{user} {user.position}")