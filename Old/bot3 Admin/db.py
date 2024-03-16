import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def admin_exists(self, admin_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `admin_id` = ?", (admin_id,)).fetchall()
            return bool(len(result))

    def add_admin(self, admin_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`admin_id`) VALUES (?)", (admin_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def add_theme(self, user_id, theme):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `theme` = ? WHERE `user_id` = ?", (theme, user_id,))