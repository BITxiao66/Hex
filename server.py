import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/ajax1', methods=['GET'])
def ajax1():
    return render_template('ajax_test.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/xuda', methods=['GET'])
def fun1():
    return render_template('data/1.txt')

@app.route('/json_ini', methods=['GET'])
def fun2():
    return render_template('json.html')

@app.route('/json_get', methods=['GET'])
def fun3():
    info = dict()
    info['name'] = "xuda"
    info['street'] = "ZhongguanCun South Avenue"
    info['age'] = "19"
    info['phone'] = '12345678'
    return jsonify(info)

@app.route('/list/<list_id>', methods=['GET','POST'])
def fun4(list_id):
    return '%s is gay' % list_id

@app.route('/test', methods=['GET'])
def fun5():
    return render_template('test.html')


if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0')