import os
from vectors import query, get_indexing_status
from index import index
from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return "OK"


@app.route('/index-website', methods=['POST'])
def index_website():
    try:
        data = request.get_json()
        url = data.get("url")

        # check if url is already indexed
        result = get_indexing_status(url)
        if len(result) > 0 and result[0][2]["status"] == 'COMPLETED':
            return jsonify({
                "status": True,
                "already_indexed": True,
                "message": "Website already indexed",
            })

        thread = Thread(target=index, args=(url,))
        thread.start()

        return jsonify({"status": True, "already_indexed": False, "message": "Indexing started"})
    except Exception as e:
        print(e)
        return jsonify({"status": False, "message": str(e)})


@app.route('/index-status', methods=['GET'])
def index_status():
    try:
        data = request.get_json()
        url = data.get("url")

        indexed = False
        result = get_indexing_status(url)
        if len(result) > 0 and result[0][2]["status"] == 'COMPLETED':
            indexed = True
        return jsonify({"status": True, "indexed": indexed})
    except Exception as e:
        return jsonify({"status": False, "message": str(e)})


@app.route('/query-vectors', methods=['POST'])
def query_vectors():
    try:
        data = request.get_json()
        text = data.get("text")
        url = data.get("url")

        base_url = url.split('/')[2]
        filters = {"base_url": {"$eq": base_url}}
        results = query(text, filters)
        return jsonify({"status": True, "data": results})
    except Exception as e:
        return jsonify({"status": False, "message": str(e)})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
