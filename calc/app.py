# Put your app in here.
from flask import Flask, request
import operations as op
app = Flask(__name__)

calcDict = {"add": op.add , "sub": op.sub , "mult": op.mult ,"div": op.div}



@app.route('/<operation>')
def do_a_math(operation):
    
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except:
        return "invalid value for a or b"

    try:
        return f"{calcDict.get(operation)(a,b)}"
    except:
        return "invalid operation. try 'add'"
        


@app.route('/math/<operation>')
def do_the_math(operation):
    
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except:
        return "invalid value for a or b"

    try:
        return f"{calcDict.get(operation)(a,b)}"
    except:
        return "invalid operation. try 'add'"
        