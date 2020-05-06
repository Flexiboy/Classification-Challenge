#!bin/python3
# -*- coding: utf-8 -*-
# Authors: @Flexiboy

def load(path):
	data = []
	temp = []
	temp2 = []
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

def distance(reference, test_subject):
	dist = []
	for i in range(4):
		dist.append(abs(reference[i] - test_subject[i]))
	dist.append(reference[4])
	return dist

def summ(distlist):
	dist_summ = 0
	for i in distlist:
		if isinstance(i, float):
		dist_summ += i
	return dist_summ

def distanceList(dataset, test_subject, k):
	distlist = []
	for i in test_subject:
		distlist.append(distance(i, test_subject))

	for i in range(len(distlist)):
		for j in range(len(distlist) - 1):
			if summ(distlist[j - 1]) > summ(distlist[j]):
				temp = distlist[j - 1]
				distlist[j - 1] = distlist[j]
				distlist[j] = temp
	return distlist[:k]

def associate(evl, test_subject): 
	array = []
	a = evl.count('A')
	b = evl.count('B')
	c = evl.count('C')
	d = evl.count('D')
	e = evl.count('E')
	f = evl.count('F')
	g = evl.count('G')
	h = evl.count('H')
	i = evl.count('I')
	j = evl.count('J')

def show(data):
	for i in data:
		print(i)

def main():
	data = load('data.csv')
	show(data)

if __name__ == '__main__':
	main()
