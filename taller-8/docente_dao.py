class DocenteDAO:
    def __init__(self, db):
        self.db = db

    def crear_tabla(self):
        self.db.cursor.execute('''
            CREATE TABLE IF NOT EXISTS docente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT,
                telefono TEXT,
                correo TEXT
            )
        ''')
    def insertar(self, docente):
        self.db.cursor.execute('''
            INSERT INTO docente (nombre, direccio
            VALUES (?, ?, ?)
        ''', (docente.nombre, docente.direccion, 
        self.db.conn.commit()
        return self.db.cursor.lastrowid
