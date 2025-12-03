from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/verify-hash', methods=['POST'])
def verify_hash():
    data = request.json
    text = data.get('text', '')
    hash_type = data.get('hash_type', 'sha256')
    target_hash = data.get('target_hash', '')

    try:
        h = hashlib.new(hash_type)
        h.update(text.encode())
        hash_result = h.hexdigest()
        return jsonify({
            "result": hash_result == target_hash,
            "your_hash": hash_result,
            "target_hash": target_hash
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()