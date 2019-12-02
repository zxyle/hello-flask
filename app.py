#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc:

from urllib.parse import urljoin

from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

from config import endpoint
from oss import OSS
from user import user_blue

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# 注册蓝图
app.register_blueprint(user_blue, url_prefix='/user')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 钩子函数
@app.before_request
def before_request():
    print('before_request')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method != 'POST':
        return render_template("upload.html")

    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    bucket_name = request.form.get("bucket_name")
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # 直接上传bytes，而不需保存到本地再上传
        # file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # file.save(file_path)
        o = OSS()
        status = o.put(filename, file.stream.read(), bucket_name=bucket_name)
        bucket_domain = f"https://{bucket_name}.{endpoint}"
        url = urljoin(bucket_domain, filename)
        return jsonify({"status": status, "url": url})


if __name__ == '__main__':
    app.run()
