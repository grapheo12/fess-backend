from flask import Blueprint, request, render_template, session, redirect, url_for, make_response
from flask_restplus import Api, Resource

rest = Blueprint('rest', __name__)
api = Api(rest, doc='/swagger')

@api.route("/query")
class Query(Resource):
    def post(self):
        from models import db, Post
        post = Post()
        post.user = str(request.remote_addr)
        post.post = request.form["confession"]
        post.relief = True if request.form["relief"] == "true" else False

        db.session.add(post)
        db.session.commit()
        
        return "Query Done"

    def get(self):
        if 'admin_login' in session and session['admin_login'] == 'Shar_mistha1':
            from models import Post
            resp = make_response(render_template("list.html", posts=Post.query.all()))
            resp.headers["Content-type"] = "text/html"
            return resp
        else:
            resp = make_response(render_template("list.html", posts=None))
            resp.headers["Content-type"] = "text/html"
            return resp     

@api.route("/login")
class Admin(Resource):
    def post(self):
        pin = request.form["pin"]
        if pin == "Shar_mistha1":
            session['admin_login'] = pin
        return "Done"

    def delete(self):
        session['admin_login'] = ''
        return "Logged Out"


@api.route("/view")
class View(Resource):
    def get(self):
        from models import Post
        return str(len(Post.query.all()))