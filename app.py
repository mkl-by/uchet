import configg
from flask import Flask, render_template, url_for, request, flash, g
import connect

app = Flask(__name__)
app.config.from_object(configg)


@app.route('/index')
@app.route('/')
def hello_world():
    db = connect.get_db()
    return render_template('index.html', name=db)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()
        print('выкл')

# int, float, path
@app.route("/profile/<cifra>")
def prof(cifra):
    return f'sdfsfsd {cifra}'


@app.route('/page1')
def hello_world1():
    print(url_for('hello_world1'))
    return render_template('form.html', title='AAAAAAAAA')

@app.route('/con', methods=['POST'])
def forma():

    if request.method == "POST":
        print(request.form)

    if len(request.form['username']) >= 2:
        flash('Cообщение отправлено')
    else:
        flash('Повторите ввод')
    connect.create_db()
    return render_template('form.html', title='AAAAAAAAA')



# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('prof', cifra='1212'))
#     print(url_for("hello_world1"))


if __name__ == '__main__':
    app.run()
