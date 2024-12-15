from vectors import query
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return "OK"


@app.route('/query-vectors', methods=['POST'])
def query_vectors():
    try:
        data = request.get_json()
        text = data.get("text")
        results = query(text)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)