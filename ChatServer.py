from flask import *
app = Flask(__name__)

messages =[]

@app.route('/')
def student():
   return render_template('index.html',messages=messages)

@app.route('/chat',methods = ['POST', 'GET'])
def chat():
   if request.method == 'POST':
      message = request.form['message']
      messages.append(message)
      return redirect('http://127.0.0.1:5000/')

if __name__ == '__main__':
   app.run(debug = True)