import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str):
        self._connection = sqlite3.connect(db_name)
        self.table_name = table_name

    def create(self, first_name: str, last_name: str):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO actors"
            " (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        cursor = self._connection.cursor()
        rows = cursor.execute(
            f"SELECT id, first_name,"
            f" last_name FROM {self.table_name}"
        ).fetchall()
        return [
            Actor(id=row[0],
                  first_name=row[1],
                  last_name=row[2]
                  ) for row in rows]

    def update(self, pk: int, new_first_name: str, new_last_name: str):
        cursor = self._connection.cursor()
        cursor.execute(
            f"UPDATE {self.table_name}"
            f" SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int):
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (pk,))
        self._connection.commit()
