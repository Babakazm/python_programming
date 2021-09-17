import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', name="Babak")
    
@app.route('/review', methods=['get','POST'])
def receive_form():
    conn = sqlite3.connect('reviews.sqlite')
    cursor = conn.cursor()
    bookname = flask.request.form['bookname']
    commentary = flask.request.form['comments']
    cursor.execute("INSERT INTO reviews (name_of_book, comment) VALUES (?, ?)",
                    [bookname, commentary])
    conn.commit()
    cursor.close()
    conn.close()
    return flask.render_template('index.html', name="Babak")

# Create custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return flask.render_template("500.html"), 500

if __name__ == '__main__':
    app.run()

print("form")