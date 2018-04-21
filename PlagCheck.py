import os
from flask import *
import string as string

#issue with multiple copies of similar words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def FileHandler(text):
    #storedFileContent contains file contents with eliminated new line characters
    storedFileContent = ' '.join(' '.join(open('store.txt','r+').read().split('\n')).split('.')).split()
    #Reading data sent by user
    text = str.replace(text,'\r','')
    # text = str.replace(text,'.',' ') 
    # shit syntax but works 
    # you can use severel times replace statement   
    submittedText = ' '.join(' '.join(text.split('\n')).split('.')).split()


    print(submittedText)
    plagCount = 0
    print(len(storedFileContent))
    for storedWord in storedFileContent:
        for word in submittedText:
            if word in storedWord:
                if plagCount < len(storedFileContent):
                    print(word)
                    plagCount = plagCount + 1 
                else:
                    return((plagCount/len(storedFileContent))*100)
    return (plagCount/len(storedFileContent))*100 

@app.route('/check',methods = ['POST', 'GET'])
def check():
   if request.method == 'POST':
        text = request.form['text']        
        plagarism=FileHandler(text)
        print(plagarism)
        return render_template('index.html',plagarism=plagarism)


if __name__ == '__main__':
   app.run(debug = True)