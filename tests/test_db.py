from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='username', email='useremail@gmail.com', password='userpass'
    )
    session.add(user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'username'))

    assert user.username == 'username'
    assert user.email == 'useremail@gmail.com'
    assert user.id is not None
