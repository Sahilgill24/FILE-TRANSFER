from flask import Flask,send_file

app=Flask(__name__)

@app.route('/file/<filename>')
def serve_file(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)