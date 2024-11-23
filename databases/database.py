import sqlite3  # Imports the sqlite3 module


class Database:
    def __init__(self, path):
        """
        Initialize the database class with a default path.
        Automatically sets up the required tables.
        """
        self.path = path
        self._setup_tables()

    def connect(self):
        """
        Establish and return a new connection to the database.
        """
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row  # Returns results as dictionaries
        return con

    def _setup_tables(self):
        """
        Create the students table if it doesn't exist.
        """
        with self.connect() as con:
            cursor = con.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    years_on_school INTEGER NOT NULL,
                    dob TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            con.commit()
