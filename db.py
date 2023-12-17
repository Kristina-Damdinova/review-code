import psycopg2

class DataAccessObject:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.conn = psycopg2.connect(
            host="db",
            user="root",
            password="my_password",
            port="5432",
            dbname="dresses.db",)
        self.tab = self.connect.cursor()
        self.query = '''CREATE TABLE IF NOT EXISTS dresses
                   (model TEXT, price TEXT, description TEXT, url TEXT, picture TEXT)'''
        self.cursor.execute(self.query)
        self.conn.commit()

    def add_information(self, model, price, description, url, picture):
        self.query = '''INSERT INTO dresses VALUES (?, ?, ?, ?, ?)'''
        self.cursor.execute(self.query, (model, price, description, url, picture))
        self.conn.commit()

    def get_information_by_model(self, number):
        # Подключаюсь к базе данных
        conn = psycopg2.connect('dresses.db')
        cursor = conn.cursor()
        # Выбираю строку с заданным порядковым номером
        cursor.execute("SELECT model, price, description, url, picture FROM dresses WHERE rowid=?", (number,))
        row = cursor.fetchone()
        conn.close()

        return f"Модель: {row[0]}, Цена: {row[1]}, {row[2]}"

    def get_models_url(self, number):
        conn = psycopg2.connect('dresses.db')
        cursor = conn.cursor()
        cursor.execute("SELECT model, price, description, url, picture FROM dresses WHERE rowid=?", (number,))
        row = cursor.fetchone()

        return {row[3]}

    def close_database(self):
        self.cursor.close()
        self.conn.close()
