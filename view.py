from app import app
from flask import Flask, render_template, url_for, request, flash
import connect


@app.route('/index')
@app.route('/')
def hello_world():
    print(url_for('hello_world'))
    data = {}
    return render_template('index.html')

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