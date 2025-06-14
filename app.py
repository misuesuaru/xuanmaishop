from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = "misuesuaru/xuanmaishop"

@app.route("/load", methods=["GET"])
def load_data():
    file_path = request.args.get("file", "data.txt")
    url = f"https://api.github.com/repos/{REPO}/contents/{file_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    res = requests.get(url, headers=headers)
    if res.ok:
        data = res.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        return jsonify({"status": "ok", "content": content})
    else:
        return jsonify({"status": "error", "message": res.text}), res.status_code

@app.route("/")
def root():
    return "🟢 Server đang chạy."

