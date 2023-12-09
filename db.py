import sqlite3

class DataAccessObject:
    def __init__(self):
        self.conn = sqlite3.connect("dresses.db")
        self.cursor = self.conn.cursor()
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
        conn = sqlite3.connect('dresses.db')
        cursor = conn.cursor()
        # Выбираю строку с заданным порядковым номером
        cursor.execute("SELECT model, price, description, url, picture FROM dresses WHERE rowid=?", (number,))
        row = cursor.fetchone()
        conn.close()

        return f"Модель: {row[0]}, Цена: {row[1]}, {row[2]}"

    def get_models_url(self, number):
        conn = sqlite3.connect('dresses.db')
        cursor = conn.cursor()
        cursor.execute("SELECT model, price, description, url, picture FROM dresses WHERE rowid=?", (number,))
        row = cursor.fetchone()

        return {row[3]}

    def close_database(self):
        self.cursor.close()
        self.conn.close()
