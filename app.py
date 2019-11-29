from urllib.parse import urljoin

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

from config import endpoint
from oss import OSS

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method != 'POST':
        return "use post method"

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
