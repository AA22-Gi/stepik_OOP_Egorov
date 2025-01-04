"""
Создайте абстрактный класс Database, в котором имеются следующие абстрактные методы:
    -   connect
    -   disconnect
    -   execute

Создайте классы MySQLDatabase и PostgreSQLDatabase,
которые будут наследовать абстрактный класс Database и реализовывать его абстрактные методы.
В каждом классе должны быть реализованы метод connect для подключения к соответствующей базе данных,
метод disconnect для отключения от базы данных,
а также метод execute, который должен выполнять запрос к соответствующей базе данных.

Внутри класса MySQLDatabase:
    -   Метод connect должен печатать на экран сообщение Connecting to MySQL database...
    -   Метод  disconnect должен печатать на экран сообщение Disconnecting from MySQL database...
    -   Метод  execute должен принимать запрос к базе данных в виде строки и печатать на экран сообщение
        Executing query '{query}' in MySQL database...

Внутри класса PostgreSQLDatabase:

    -   Метод connect должен печатать на экран сообщение Connecting to PostgreSQL database...
    -   Метод  disconnect должен печатать на экран сообщение Disconnecting from PostgreSQL database...
    -   Метод  execute должен принимать запрос к базе данных в виде строки и печатать на экран сообщение
        Executing query '{query}' in PostgreSQL database...
"""
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def disconnect(self): ...

    @abstractmethod
    def execute(self, query): ...


class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")


if __name__ == '__main__':
    mysql_db = MySQLDatabase()
    postgresql_db = PostgreSQLDatabase()

    mysql_db.connect()
    mysql_db.execute(
        "SELECT * FROM customers;")
    mysql_db.disconnect()

    postgresql_db.connect()
    postgresql_db.execute(
        "SELECT * FROM customers;")
    postgresql_db.disconnect()
