import xml.etree.ElementTree as ET
import threading

def Partition(array,low,high):
	if low < high:
		i = low
		pivot = i
		j = high
		while i<j:
			while array[pivot] >= array[i] and i < high:
				i = i +1
			while array[pivot] < array[j]:
				j = j -1
			if i<j:
				array[i],array[j] = array[j],array[i]
		array[pivot],array[j] = array[j],array[pivot]
	return j
	
def QuickSort(array, low, high):
	if low < high:
		partitionNumber = Partition(array,low,high)
		# QuickSort(array,low,partitionNumber-1)
		# QuickSort(array,partitionNumber+1,high)
		thread1=threading.Thread(target=QuickSort,args=(array,low,partitionNumber-1))
		thread2=threading.Thread(target=QuickSort,args=(array,partitionNumber+1,high))
		thread1.start()
		thread2.start()
		thread1.join()
		print (thread1.getName())
		thread2.join()
		print (thread2.getName())

def GetData():
	tree = ET.parse('QuickSortDataSet.xml')
	root = tree.getroot()
	#Converting xml inputs to integer data-
	arraySize = len(root)
	index = 0
	newArray = [0 for j in range(0,arraySize)]
	for child in root.findall('Weather'):
		number = child.find('number').text
		newArray[index] = (int) (number)
		index = index + 1
	#function call
	QuickSort(newArray,0,arraySize-1)

	print("Sorted array is")
	print(newArray)
 
GetData()
	 
