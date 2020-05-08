#!bin/python3
# -*- coding: utf-8 -*-
# Authors: @Flexiboy

import matplotlib.pyplot as plt

def load(path):
	"""
	Loading a file from a path
	:param path: path of the file
	:return: array containing the data
	"""
	data = []
	temp = []
	with open(path, "r") as inp:
		for i in inp:
			for j in range(5):
				if j == 4:
					temp.append((i.split(';')[j]).split('\n')[0])
				else:
					temp.append(float(i.split(';')[j]))
			data.append(temp)
			temp = []
	return data

def split(data, index, char):
	"""
	Spliting the data in order to plot it
	:param data: the dataset
	:param index: where to search the char
	:param char: the searched label
	:return: array of the specified label
	"""
	array = []
	for i in data:
		if i[4] == char:
			array.append(i[index])
	return array

def main():
	data = load('data/data.csv')
	a0 = split(data, 0, 'A')
	b0 = split(data, 0, 'B')
	c0 = split(data, 0, 'C')
	d0 = split(data, 0, 'D')
	e0 = split(data, 0, 'E')
	f0 = split(data, 0, 'F')
	g0 = split(data, 0, 'G')
	h0 = split(data, 0, 'H')
	i0 = split(data, 0, 'I')
	j0 = split(data, 0, 'J')

	a1 = split(data, 1, 'A')
	b1 = split(data, 1, 'B')
	c1 = split(data, 1, 'C')
	d1 = split(data, 1, 'D')
	e1 = split(data, 1, 'E')
	f1 = split(data, 1, 'F')
	g1 = split(data, 1, 'G')
	h1 = split(data, 1, 'H')
	i1 = split(data, 1, 'I')
	j1 = split(data, 1, 'J')
	
	a2 = split(data, 2, 'A')
	b2 = split(data, 2, 'B')
	c2 = split(data, 2, 'C')
	d2 = split(data, 2, 'D')
	e2 = split(data, 2, 'E')
	f2 = split(data, 2, 'F')
	g2 = split(data, 2, 'G')
	h2 = split(data, 2, 'H')
	i2 = split(data, 2, 'I')
	j2 = split(data, 2, 'J')
	
	a3 = split(data, 3, 'A')
	b3 = split(data, 3, 'B')
	c3 = split(data, 3, 'C')
	d3 = split(data, 3, 'D')
	e3 = split(data, 3, 'E')
	f3 = split(data, 3, 'F')
	g3 = split(data, 3, 'G')
	h3 = split(data, 3, 'H')
	i3 = split(data, 3, 'I')
	j3 = split(data, 3, 'J')
	
	plt.plot([1 for i in range(len(a0))], a0, 'ro', label = "A", color = '#ff0000')
	plt.plot([2 for i in range(len(b0))], b0, 'ro', label = "B", color = '#00cc00')
	plt.plot([3 for i in range(len(c0))], c0, 'ro', label = "C", color = '#0000ff')
	plt.plot([4 for i in range(len(d0))], d0, 'ro', label = "D", color = '#ffff00')
	plt.plot([5 for i in range(len(e0))], e0, 'ro', label = "E", color = '#6600cc')
	plt.plot([6 for i in range(len(f0))], f0, 'ro', label = "F", color = '#ff00ff')
	plt.plot([7 for i in range(len(g0))], g0, 'ro', label = "G", color = '#663300')
	plt.plot([8 for i in range(len(h0))], h0, 'ro', label = "H", color = '#00ffff')
	plt.plot([9 for i in range(len(i0))], i0, 'ro', label = "I", color = '#666699')
	plt.plot([10 for i in range(len(j0))], j0, 'ro', label = "J", color = '#003366')
	plt.legend()
	plt.title('First variable of dataset')
	plt.show()

	plt.plot([1 for i in range(len(a1))], a0, 'ro', label = "A", color = '#ff0000')
	plt.plot([2 for i in range(len(b1))], b0, 'ro', label = "B", color = '#00cc00')
	plt.plot([3 for i in range(len(c1))], c0, 'ro', label = "C", color = '#0000ff')
	plt.plot([4 for i in range(len(d1))], d0, 'ro', label = "D", color = '#ffff00')
	plt.plot([5 for i in range(len(e1))], e0, 'ro', label = "E", color = '#6600cc')
	plt.plot([6 for i in range(len(f1))], f0, 'ro', label = "F", color = '#ff00ff')
	plt.plot([7 for i in range(len(g1))], g0, 'ro', label = "G", color = '#663300')
	plt.plot([8 for i in range(len(h1))], h0, 'ro', label = "H", color = '#00ffff')
	plt.plot([9 for i in range(len(i1))], i0, 'ro', label = "I", color = '#666699')
	plt.plot([10 for i in range(len(j1))], j0, 'ro', label = "J", color = '#003366')
	plt.legend()
	plt.title('Second variable of dataset')
	plt.show()

	plt.plot([1 for i in range(len(a2))], a0, 'ro', label = "A", color = '#ff0000')
	plt.plot([2 for i in range(len(b2))], b0, 'ro', label = "B", color = '#00cc00')
	plt.plot([3 for i in range(len(c2))], c0, 'ro', label = "C", color = '#0000ff')
	plt.plot([4 for i in range(len(d2))], d0, 'ro', label = "D", color = '#ffff00')
	plt.plot([5 for i in range(len(e2))], e0, 'ro', label = "E", color = '#6600cc')
	plt.plot([6 for i in range(len(f2))], f0, 'ro', label = "F", color = '#ff00ff')
	plt.plot([7 for i in range(len(g2))], g0, 'ro', label = "G", color = '#663300')
	plt.plot([8 for i in range(len(h2))], h0, 'ro', label = "H", color = '#00ffff')
	plt.plot([9 for i in range(len(i2))], i0, 'ro', label = "I", color = '#666699')
	plt.plot([10 for i in range(len(j2))], j0, 'ro', label = "J", color = '#003366')
	plt.legend()
	plt.title('Third variable of dataset')
	plt.show()

	plt.plot([1 for i in range(len(a3))], a0, 'ro', label = "A", color = '#ff0000')
	plt.plot([2 for i in range(len(b3))], b0, 'ro', label = "B", color = '#00cc00')
	plt.plot([3 for i in range(len(c3))], c0, 'ro', label = "C", color = '#0000ff')
	plt.plot([4 for i in range(len(d3))], d0, 'ro', label = "D", color = '#ffff00')
	plt.plot([5 for i in range(len(e3))], e0, 'ro', label = "E", color = '#6600cc')
	plt.plot([6 for i in range(len(f3))], f0, 'ro', label = "F", color = '#ff00ff')
	plt.plot([7 for i in range(len(g3))], g0, 'ro', label = "G", color = '#663300')
	plt.plot([8 for i in range(len(h3))], h0, 'ro', label = "H", color = '#00ffff')
	plt.plot([9 for i in range(len(i3))], i0, 'ro', label = "I", color = '#666699')
	plt.plot([10 for i in range(len(j3))], j0, 'ro', label = "J", color = '#003366')
	plt.legend()
	plt.title('Fourth variable of dataset')
	plt.show()

if __name__ == '__main__':
	main()
