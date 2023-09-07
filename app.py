from flask import Flask,send_file,send_from_directory

app=Flask(__name__)

@app.route('/server/<file_name>')
def serve_file(file_name):
    print(file_name)
    
    return send_from_directory("server",file_name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)