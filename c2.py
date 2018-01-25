#-*- encoding=UTF-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'
@app.route('/profile/<int:uid>',methods=['get'])
def profile(uid):
    return 'profile:'+str(uid)
if __name__ == '__main__':
    app.run(debug=True)
