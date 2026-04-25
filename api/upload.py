from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Backend is running"})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"success": False, "error": "No file selected"}), 400
        
        # 简单的响应
        return jsonify({
            "success": True, 
            "notes": ["测试知识点1", "测试知识点2"],
            "fileName": file.filename
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Vercel需要这个导出
handler = app
