import imghdr
import os
import json
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from cv_manager.main import process_cv
from flask_paginate import Pagination, get_page_args
from db_manager.create_table import create_user_table, create_skill_table, create_category_table
from db_manager.fetch_profile import fetch_user
from db_manager.delete_profile import delete_user
from db_manager.update_profile import update_user
from flask import send_file
from dashboard.stats import stats, get_pie

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [
    ".jpg",
    ".png",
    ".gif",
    ".docs",
    ".pdf",
    ".xlsx",
    ".docx",
    ".doc",
]
app.config["UPLOAD_PATH"] = "uploads"


def get_users(users, offset=0, per_page=10):

    return users[offset : offset + per_page]


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return "." + (format if format != "jpeg" else "jpg")


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route("/")
def index():
    # files = os.listdir(app.config["UPLOAD_PATH"])
    users = fetch_user()
    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    total = len(users)
    pagination_users = get_users(users, offset, per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    dashboard = stats()
    pie_data, pie_label = get_pie()

    return render_template(
        "index.html",
        users=pagination_users,
        page=page,
        per_page=per_page,
        pagination=pagination,
        dashboard=dashboard,
        pie_data=pie_data,
        pie_label=pie_label
    )


@app.route("/", methods=["POST"])
def upload_files():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return "Invalid File", 400
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
        try:
            process_cv()
        except Exception as e:
            return "Unable to process this file" + str(e) + filename
        return redirect("/")
    return "", 204


@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)

@app.route("/edit-user", methods=["POST"])
def edit_user():
    data = dict(request.form)
    update_user(data)
    if "skills" in data:
        data.update({
            "skills": json.dumps(data['skills'])
        })
    print(data)
    return redirect("/")

@app.route("/get-file")
def get_file():
    path = request.args.get('path')
    abs_path = os.path.join(os.getcwd(), "uploads", *path.split("/"))
    if os.path.exists(abs_path):
        return send_file(abs_path)
    else:
        return("Error while downloading the file, File not found")


@app.route("/delete-file")
def delete_file():
    path = request.args.get('path')
    id = request.args.get('id')
    abs_path = os.path.join(os.getcwd(), "uploads", *path.split("/"))
    if os.path.exists(abs_path):
        os.remove(abs_path)
        delete_user(id)
        return redirect("/")
    else:
        return("Error while deleting the file")

def setup_db():
    create_user_table()
    create_skill_table()
    create_category_table()
    print("DB Setup is done")

if __name__ == "__main__":
    setup_db()
    app.run(debug=True)
