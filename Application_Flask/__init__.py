from flask import Flask
from flask import g

app = Flask(__name__)
app.debug = True

#Application Context - 공용
#Session Context - 개인
@app.before_request
def before_request():
    print("before_request")
    g.str = "한글" #모든 사람을 컨트롤 하고 싶을 때 g

@app.route("/gg")
def helloworld2():
    return "Hello world" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Rose!"
