import copy
import threading


class FunctionThread(threading.Thread):
	def __init__(self, funct):
		threading.Thread.__init__(self)
		self.result = None
		self.funct = funct

	def run(self):
		self.result = self.funct()

	def _stop(self):
		if self.isAlive():
			threading.Thread._Thread__stop(self)

class Solution(object):
	def __init__(self, ingrid):
		self.ingrid = ingrid
		self.grid_size = 81
		self.grid = copy.deepcopy(self.ingrid)
		self.is_solution = False

	def is_full(self):
		return self.grid.count('.') == 0

	def get_trailcelli(self):
		for i in xrange(self.grid_size):
			if self.grid[i] == '.':
				return i

	def is_legal(self, tri, trailcelli):
		cols = 0
		for each_square in xrange(9):
			trisquare = [x+cols for x in xrange(3)] + [x+9+cols for x in xrange(3)] + [x+18+cols for x in xrange(3)]
			cols +=3
			if cols in [9, 36]:
				cols +=18
			if trailcelli in trisquare:
				for i in trisquare:
					if self.grid[i] != '.':
						if tri == int(self.grid[i]):
							return False

		for earow in xrange(9):
			trirow = [ x+(9*earow) for x in xrange (9) ]
			if trailcelli in trirow:
				for i in trirow:
					if self.grid[i] != '.':
						if tri == int(self.grid[i]):
							return False

		for eacol in xrange(9):
			triacol = [ (9*x)+eacol for x in xrange (9) ]
			if trailcelli in triacol:
				for i in triacol:
					if self.grid[i] != '.':
						if tri == int(self.grid[i]):
							return False
		return True

	def set_cell(self, tri, trailcelli):
		self.grid[trailcelli] = tri
		return self.grid

	def clcell(self, trailcelli ):
		self.grid[trailcelli] = '.'
		return self.grid

	def havesolution(self):
		if self.is_full():
			return True
		else:
			trailcelli = self.get_trailcelli()
			tri = 1
			solfound = False
			while (solfound != True) and (tri < 10):
				if self.is_legal(tri, trailcelli):
					self.grid = self.set_cell(tri, trailcelli)
					if self.havesolution() == True:
						solfound = True
						self.is_solution = solfound
						return True
					else:
						self.clcell( trailcelli )
				tri += 1
			self.is_solution = solfound
			return solfound



	def rgrid(self=None):
		if not self.havesolution():
			return False
		i = 0
		solgrid = []
		solution_row = []
		for val in self.grid:
			solution_row.append(int(val))
			i +=1
			if i in [ (x*9) for x in xrange(10)]:
				solgrid.append(solution_row)
				solution_row = []

		return solgrid
