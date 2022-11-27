from flask import Flask, jsonify,render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/additionOne/<int a>/<int b>')
# def additionOne(a,b):
#     c = a+b
#     return str(c)

@app.route('/addition')
def addition():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    return str(n1+n2)

@app.route('/multiply')
def multiply():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    return str(n1*n2)

@app.route('/subtraction')
def subtraction():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    return str(n1-n2)

if __name__ == "__main__":
    app.run(debug=True,port=80)
