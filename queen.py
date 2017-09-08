"""N_queen problem class

The purpose of this class is to populate a n sized board
with n queens in random columns in each row.

This class can print a board and see how many queens can take
other queens
"""

import random

class Queen:
	"""Class definition for the n queen problem

	This class creates a random nxn board where the board is represented as
	a list containing integers, where the index is the row and the  number
	inside the list is the column it is in. This can be called with self.board

	The size of the board is in self.size

	This class randomizes placement of pieces upon initialization, can see
	how many queens can take other queens, and can print the board state

	Attributes:
		board (list of ints): The current board state where the indexes are
			the rows and the columns are inside the list
		size (int): The size of the board (len of list)
		valid_queens (int): The number of queens that are in valid positions
			on the board

	"""
	def __init__(self, n):
		"""Initializes the board

		Initialize the board with random pieces in each row. Find the number
		of queens that are in valid positions on the board in this state.

		Args:
			n (int): The size of the board and the number of queens
		"""
		self.board = []
		self.size = n

		for i in range(n):
			self.board.append(random.randrange(n))

		self.valid_queens = self.valid_queens_count()

	def update_valid_queens(self):
		"""Helper function to update the valid_queens attribute

		This is a helper function to update the number of valid queens
		from outside the class.
		"""
		self.valid_queens = self.valid_queens_count()

	def valid_queens_count(self):
		"""Computes the number of valid queens

		Find the number of valid queens in the current board state.

		Returns:
			(int) The number of valid queens
		"""
		
		conflict = set()
		temp_board = self.board

		# Same column
		for i in range(self.size):
			for j in range(self.size):
				if i !=j and self.board[i] == self.board[j]:
					conflict.add(i)
					conflict.add(j)

		# Same diagonal
		for i in range(self.size):
			for j in range(self.size):
				if i == j:
					continue
				distance = abs(j - i)
				if self.board[j] == self.board[i] + distance or self.board[j] == self.board[i] - distance:
					conflict.add(i)
					conflict.add(j)

		return self.size - len(conflict)

	def print_board(self):
		"""Prints the board
		"""
		for i in range(self.size):
			for j in range(self.size):
				if self.board[i] == j:
					print("| Q ", end='')
				else:
					print("|   ", end='')
				if j == self.size - 1:
					print("|")
			for j in range(self.size):
				print("----", end='')
				if j == self.size - 1:
					print()
		print()

	def __lt__(self, other):
		"""Defines < for class

		Less than is defined as who has fewer valid queen states

		"""
		return self.valid_queens < other.valid_queens