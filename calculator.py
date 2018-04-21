from flask import *
from math import *
#Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/currency',methods = ['POST', 'GET'])
def currency():
   if request.method == 'POST':
        curr = request.form['currency']
        operation = request.form['op']
        result = CurrencyConverter(curr,operation)
        return render_template('index.html',currencyResult = result)

@app.route('/calculate',methods = ['POST', 'GET'])
def bootstrap():
   if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        if(num1 ==""):
            num1 = 0
        if(num2 == ""):
            num2 = 0
        operation = request.form['op']
        result = calculate(num1,num2,operation)
        return render_template('index.html',result = result)
        
def calculate(num1,num2,operation):
    if(operation == '+'):
        return int(num1) + int(num2)
    elif(operation == '-'):
        return int(num1) - int(num2)
    elif(operation == '*'):
        return int(num1) * int(num2)
    elif(operation == '/'):
        return int(num1) / int(num2)
    elif(operation=='sqrt'):
        return sqrt(int(num1))  
    elif(operation == 'sine'):
        return sin(int(num1))
    elif(operation == 'cos'):
        return cos(int(num1))  

def CurrencyConverter(curr,operation):
    if(operation == 'uti'):
        return int(curr) * 65
    elif(operation == 'itu'):
        return int(curr) / 65
    elif(operation == 'pti'):
        return int(curr) * 85
    elif(operation == 'itp'):
        return int(curr) / 85        

if __name__ == '__main__':
   app.run(debug = True)