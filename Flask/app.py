from flask import Flask
app=Flask(__name__)


@app.route('/')
def home():
    return '<h1> hello world </h1>'
app.run()


@app.route('/profile/<username>')
def profile(username):
    return '<h1> Hi %s </h1>' % username
app.run()