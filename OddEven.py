from flask import *
#Flask, redirect, url_for, request
app = Flask(__name__)

def oddEvenSort(arr, n):
    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
    return

@app.route('/sort',methods = ['POST', 'GET'])
def sort():
   if request.method == 'POST':
        numbers = request.form['array']
        if numbers =="":
            return render_template('index.html',array = "Invalid Input")
        dataset_array = []
        num = []
        for item in numbers.split(','): # comma, or other
            dataset_array.append(item)
        for number in dataset_array:
            num.append(int(number))
        oddEvenSort(num,len(num))
        return render_template('index.html',array = num)
        #("<html>%s</html>"%(str(num)))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)