from flask import Flask, render_template, redirect, url_for, request, jsonify, flash 
import sqlite3
#werkzeug error codes custom

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('pokemon.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        new_name = request.form["name"],
        new_type = request.form["type"],
        new_level = request.form["level"]
        
        print(new_name[0], new_type[0], new_level)

        conn = get_db_connection()
        new_row = conn.execute("INSERT INTO pokemon (name, type, level) VALUES (?, ?, ?)", (new_name[0], new_type[0], new_level,))
        conn.commit()
        conn.close()

        return render_template('home.html', title='POKEMON', pokelist=show_pokedex())    
    else:
        return render_template('home.html', title='POKEMON', pokelist=show_pokedex())


@app.route('/delete/<int:pokemon_id>')
def delete(pokemon_id):
        try:
            print('DELETE DELETE')
            print(pokemon_id)
            conn = get_db_connection()
            del_row = conn.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))
            conn.commit()
            print("Record deleted successfully ")
            conn.close()
            return redirect(url_for("index"))
        except:
            print('lol nope')
            return 'there was a problem deleting that task'

def show_pokedex():
    conn = get_db_connection()
    pokelist = conn.execute('SELECT * FROM pokemon')
    rows = pokelist.fetchall()
    pokedex = []
    for row in rows:
        pokedex.append([ row [ 'id' ], row [ 'name' ]  ,  row [ 'type' ]  ,  row [ 'level' ]])
    print(type(pokedex))
    print(pokedex)
    return pokedex

    


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'your secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

