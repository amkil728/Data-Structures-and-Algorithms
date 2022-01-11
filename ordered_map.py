# ordered_map.py

class OrderedMap:
	def __init__(self):
		self.keys, self.vals = list(), list()
		self.size = 0

	def empty(self):
		return self.size == 0

	def rank(self, key):
		'''number of keys less than key'''
		lo, hi = 0, self.size - 1
		while lo <= hi:
			mid = (lo + hi) // 2
			
			if key == self.keys[mid]:
				return mid
			elif key < self.keys[mid]:
				hi = mid - 1
			else:
				lo = mid + 1
		return lo

	def select(self, rk):
		if rk < self.size:
			return self.keys[rk]
	
	def get(self, key):
		rk = self.rank(key)
		if rk < self.size and self.keys[rk] == key:
			return self.vals[rk]
		else:
			return None

	def put(self, key, val):
		rk = self.rank(key)
		if rk < self.size and self.keys[rk] == key:
			if val:
				self.vals[rk] = val
		else:
			self.keys.insert(rk, key)
			self.vals.insert(rk, val)
			self.size += 1
				
	def delete(self, key):
		rk = self.rank(key)
		if rk < self.size and self.keys[rk] == key:
			self.keys.pop(rk)
			self.vals.pop(rk)
			self.size -= 1

	def contains(self, key):
		rk = self.rank[key]
		return rk < len(keys) and self.keys[rk] == key

	def min_key(self):
		return self.keys[0]

	def max_key(self):
		return self.keys[self.size - 1]

	def ceil(self, key):
		return self.keys[self.rank(key)]

	def floor(self, key):
		rk = self.rank(key)
		if self.keys[rk] == key:
			return key
		else:
			return self.keys[rk - 1]

	def delete_min(self):
		self.delete(self.min_key())

	def delete_max(self):
		self.delete(self.max_key())

	def range_len(self, lo, hi):
		if hi < lo:
			return 0
		elif self.contains(hi):
			return self.rank(hi) - self.rank(lo) + 1
		else:
			return self.rank(hi) - self.rank(lo)
