#because we parse json
import json

global N
N = 8
#forget this and it will throw NameError: global name 'board' is not defined
board = [[0 for x in range(8)] for x in range(8)]

def isPlaced(board,row,col):
	# traverse on row, or it will add all the queens to board[row++][0]
	for i in range(row):
		if(board[i][col] ==1):
			return True
	#returns true if queen is preset at board[i,col]	
	i = row - 1
	j = col - 1
	# decrements are used to traverse upper left diagonal of the board
	while((i>=0) and (j>=0)):
		if(board[i][j] == 1):
			return True
		i = i - 1
		j = j - 1
	i = row - 1
	j = col + 1
	#decrement and increment are used to traverse lower left diagonal if the board
	while((i>=0) and (j<8)):
		if(board[i][j] == 1):
			return True
		i = i - 1
		j = j + 1
	# if safe position if found
	return False
	



def NQueenSolver(board,row):
	#solves N Queen Poblem, Backtracking	
	i = 0
	while(i<N):
		#if isPlaced returns false i.e. safe position is found
		if(not isPlaced(board,row,i)):
			board[row][i] = 1
			if(row == 7):
				return True
			else:
		#else queen is placed on next row
				if(NQueenSolver(board,row+1)):
					return True
				else:
					board[row][i] = 0
		i = i + 1
	if( i == 8 ):
		return False

def PrintBoard(board):
	for i in range(N):
		print(board[i])
			


def main():
	#creating store for input data
	data = []
	with open('input.json') as inputFile:
		data = json.load(inputFile)

	if(data["start"] < 0 or data["start"] > 7):
		print("Invalid Json Input!")
		exit()
	#positioning first queen at start th coloumn
	board[0][data["start"]] = 1
	#calling Solver 
	if(NQueenSolver(board,1)):
		print("Solution:")
		PrintBoard(board)
	else:
		print("No Solution Found!")

#calls main method
main()
