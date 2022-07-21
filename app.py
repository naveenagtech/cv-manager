import imghdr
import os
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from cv_manager.main import process_cv
from flask_paginate import Pagination, get_page_args

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
    files = os.listdir(app.config["UPLOAD_PATH"])
    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    total = len(files)
    pagination_users = get_users(files, offset, per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template("index.html", files=pagination_users, page=page, per_page=per_page, pagination=pagination)


@app.route("/", methods=["POST"])
def upload_files():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return "Invalid File", 400
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
        process_cv()
        return redirect("/")
    return "", 204


@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


if __name__ == "__main__":
    app.run(debug=True)
