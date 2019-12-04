#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 

from urllib.parse import urljoin

from flask import jsonify, render_template, request
from werkzeug.utils import secure_filename

from app.config import endpoint
from app.oss import oss_blue
from app.oss.sdk import OSS

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@oss_blue.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method != 'POST':
        return render_template("transfer.html")

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
