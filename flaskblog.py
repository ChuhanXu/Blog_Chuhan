from flask import Flask,render_template, url_for
app = Flask(__name__)


blog_list = [{
    "author":"Chuhan",
    "title":"blog1",
    "content":"first_blog",
    "date_posted":"Jun 22"
},{
    "author": "Xiaoyu",
    "title": "blog2",
    "content": "second_blog",
    "date_posted": "Jun 22"
}]
#decorator @app
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',blog_list=blog_list,title="Chuhan")


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)