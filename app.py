from urllib.parse import urljoin

from flask import Flask, jsonify, request

from config import endpoint
from downloader import download
from oss import OSS

app = Flask(__name__)


@app.route('/oss', methods=["GET", "POST"])
def oss():
    if request.method != "POST":
        return

    img_url = request.form.get("img_url")
    bucket_name = request.form.get("bucket_name")

    img_path, filename = download(img_url)

    o = OSS()
    status = o.put(img_path, bucket_name=bucket_name)
    bucket_domain = f"https://{bucket_name}.{endpoint}"
    url = urljoin(bucket_domain, filename)
    return jsonify({"status": status, "url": url})


if __name__ == '__main__':
    app.run()
