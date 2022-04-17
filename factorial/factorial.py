from flask import Flask
from flask import request, jsonify, json, render_template
from flask_cors import CORS, cross_origin
from functools import wraps
from math import factorial as math_fact
from werkzeug.exceptions import abort
from multiprocessing import Pool
import psutil
import time

app = Flask(__name__)

def limit_content_length(max_length):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cl = request.content_length
            print("Received request length: ", cl)
            if cl is not None and cl > max_length:
                abort(413)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/test', methods=['GET', 'POST'])
@limit_content_length(40)
@cross_origin()
def cpu_test():
    processes = psutil.cpu_count()
    print ('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    pool.map(f, range(processes))
    return 'Done'
    # try:
    #     print(request.json)
    #     minutes = int(request.form['mn'])
       
    # except ValueError:
    #     return ('Please enter a number!')

@app.route('/factorial', methods=['GET', 'POST'])
def factorial():
    try:
        fbase = int(request.json['fbase'])
    except ValueError:
        return ('Please enter a number!')
    if fbase < 50:
        return str(math_fact(fbase))

@app.route('/')
def index():
    return render_template('index.html')

# def math_fact(fbase):
#     fact = 1
#     for i in range(1, fbase+1):
#         fact *= i
#     return fact

def f(x):
    set_time = 5
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break


if __name__ == '__main__':
    app.run(debug=True)
