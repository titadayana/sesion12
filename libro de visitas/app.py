from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def crear_tabla():
    conn = sqlite3.connect('libro_visitas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            mensaje TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

crear_tabla()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = request.form['mensaje']
        conn = sqlite3.connect('libro_visitas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mensajes (nombre, mensaje) VALUES (?, ?)', (nombre, mensaje))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('libro_visitas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM mensajes')
        mensajes = cursor.fetchall()
        conn.close()
        return render_template('index.html', mensajes=mensajes)

if __name__ == '__main__':
    app.run(debug=True)
