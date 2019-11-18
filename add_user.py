import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)


def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():
    print("Заполните анкету.")
    first_name = input("Введите имя: ")
    last_name = input("Введит фамилию: ")
    gender = input("Укажите пол (Male/Female): ")
    email = input("Введите ваш е-мэйл: ")
    birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
    height = float(input("Введите свой рост в метрах: "))

    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    return user
    

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены!")


if __name__ == "__main__":
    main()