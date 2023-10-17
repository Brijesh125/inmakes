from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)

@app.route('/books')
def book():
    books=[{'name':'book1','author':'abc1','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'},
           {'name':'book2','author':'abc2','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'},
           {'name':'book3','author':'abc3','cover':'https://assets.visme.co/templates/banners/thumbnails/i_Fiction-Book-Cover_full.jpg'}]
    return render_template('books.html',books=books)

app.run(debug=True)