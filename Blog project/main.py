from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()
post_list = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(post)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_list)


@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
