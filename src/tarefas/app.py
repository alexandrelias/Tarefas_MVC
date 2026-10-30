from tarefas.models.database import init_db

from flask import Flask, render_template

app = Flask(__name__)
with app.app_context():
    init_db()
@app.route('/test')
def test():
    return "Servidor Online!"
@app.route('/')
def home():
    return render_template('base.html', titulo='Home')
if __name__ == "__main__":
    app.run()