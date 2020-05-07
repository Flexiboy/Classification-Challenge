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
		dist.append(float(abs(reference[i] - test_subject[i])))
	dist.append(reference[4])
	return dist

def summ(distlist):
	dist_summ = 0
	for i in distlist:
		if isinstance(i, float):
			dist_summ += i
	return dist_summ

def distance_list(dataset, test_subject, k):
	distlist = []
	for i in dataset:
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
	count = [a, b, c, d, e, f, g, h, i, j]
	
	if max(count) == a:
		test_subject.append('A')
	elif max(count) == b:
		test_subject.append('B')
	elif max(count) == c:
		test_subject.append('C')
	elif max(count) == d:
		test_subject.append('D')
	elif max(count) == e:
		test_subject.append('E')
	elif max(count) == f:
		test_subject.append('F')
	elif max(count) == g:
		test_subject.append('G')
	elif max(count) == h:
		test_subject.append('H')
	elif max(count) == i:
		test_subject.append('I')
	elif max(count) == j:
		test_subject.append('J')

	return test_subject

def show(data):
	for i in data:
		print(i)

def main():
	data = load('data.csv')
	evaluate = load('preTest.csv')
	k = 20
	final = []
	for i in evaluate:
		final.append(associate(distance_list(data, i, k), i))
	show(final)

if __name__ == '__main__':
	main()
