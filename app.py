from urllib.parse import urljoin

from flask import Flask, request, jsonify

from config import bucket_domain
from downloader import download
from oss import OSS

app = Flask(__name__)


@app.route('/oss', methods=["GET", "POST"])
def oss():
    img_url = request.form.get("img_url")

    img_path, filename = download(img_url)

    o = OSS()
    status = o.put(img_path)

    url = urljoin(bucket_domain, filename)
    return jsonify({"status": status, "url": url})


if __name__ == '__main__':
    app.run()
