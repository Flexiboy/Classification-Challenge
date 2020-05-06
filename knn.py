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
					temp.append(i.split(';')[j])
			data.append(temp)
			temp = []
	return data

def show(data):
	for i in data:
		print(i)

def main():
	data = load('data.csv')
	show(data)

if __name__ == '__main__':
	main()
