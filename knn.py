#!bin/python3
# -*- coding: utf-8 -*-
# Authors: @Flexiboy

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def load(path):
	"""
	Loading a file from a path
	:param path: path of the file
	:return: array containg the data
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

def distance(reference, test_subject):
	"""
	Calculating the distance between two subjects
	:param reference: the reference subject
	:param test_subject: the subject to test
	:return: an array containing distances at first and a label in the end
	"""
	dist = []
	for i in range(4):
		dist.append(float(abs(reference[i] - test_subject[i])))
	dist.append(reference[4])
	return dist

def summ(distlist):
	"""
	Adding all the array content
	:param distlist: the array to summ
	:return: summ of all the array content
	"""
	dist_summ = 0
	for i in distlist:
		if isinstance(i, float):
			dist_summ += i
	return dist_summ

def mink(distlist):
	"""
	Calculating the distances with the minkwoski algorithm
	:param distlist: the array that contains the distances between the reference and the test subject
	:return: minkwoski distance
	"""
	mink_dist = 0
	for i in distlist:
		if isinstance(i, float):
			mink_dist += i ** 4
	return mink_dist ** 0.25

def distance_list(dataset, test_subject, k):
	"""
	Getting an array of all distances from between a testing subject and the dataset
	:param dataset: the array containing the dataset
	:param test_subject: the testing subject
	:param k: the number of items to return
	:return: the top-k distances
	"""
	distlist = []
	for i in dataset:
		distlist.append(distance(i, test_subject))
	final = sorted(distlist, key=lambda dist: mink(dist))
	return final[:k]

def element_count(array, index, to_find):
	"""
	Counting the occurence of the element to_find in an array
	:param array: the input array
	:param index: the index where to search
	:param to_find: the element to find in the array
	:return: the number of occurence of the element to find in the array
	"""
	number = 0
	for i in array:
		if i[index] == to_find:
			number += 1
	return number

def associate(evl, test_subject): 
	"""
	Associating the testing subject to a label
	:param evl: the distance list
	:param test_subject: the testing subject
	:return: the testing subject with its associated label
	"""
	array = []
	a = element_count(evl, 4, 'A')
	b = element_count(evl, 4, 'B')
	c = element_count(evl, 4, 'C')
	d = element_count(evl, 4, 'D')
	e = element_count(evl, 4, 'E')
	f = element_count(evl, 4, 'F')
	g = element_count(evl, 4, 'G')
	h = element_count(evl, 4, 'H')
	i = element_count(evl, 4, 'I')
	j = element_count(evl, 4, 'J')
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
	"""
	Printing the array in the console
	:param data: the array to print
	:return: nothing
	"""
	for i in data:
		print(i)

def confusion_mat(data, first_index):
	"""
	This creates a confusion matrix and a report about the results
	:param data: the array of the results
	:param first_index: the first index where the labels start (actual then predicted)
	:return: nothing
	"""
	actual = []
	predicted = []
	for i in data:
		actual.append(i[first_index])
		predicted.append(i[first_index + 1])
	
	results = confusion_matrix(actual, predicted)
	results_normalized = results.astype('float') / results.sum(axis=1)[:, np.newaxis]
	print(f'Accuracy score: {accuracy_score(actual, predicted)}')
	print('Report:')
	print(classification_report(actual, predicted))
	
	df_cm = pd.DataFrame(results, index = [i for i in "ABCDEFGHIJ"], columns = [i for i in "ABCDEFGHIJ"])
	df_cm.index.name = 'Actual'
	df_cm.columns.name = 'Predicted'
	plt.figure(figsize = (10, 7))
	plt.title('Confusion matrix, without normalization')
	sn.heatmap(df_cm, cmap=plt.cm.Blues, annot=True)
	
	df_cm_nm = pd.DataFrame(results_normalized, index = [i for i in "ABCDEFGHIJ"], columns = [i for i in "ABCDEFGHIJ"])
	df_cm_nm.index.name = 'Actual'
	df_cm_nm.columns.name = 'Predicted'
	plt.figure(figsize = (10, 7))
	plt.title('Confusion matrix, normalized')
	sn.heatmap(df_cm_nm, cmap=plt.cm.Blues, annot=True)
	
	with open("results/classification_report.txt", "w") as out:
		for i in classification_report(actual, predicted):
			out.write(i)
	plt.show()	

def main():
	"""
	The main function
	:return: nothing
	"""
	t0 = time.perf_counter()
	data = load('data/data.csv')
	evaluate = load('data/preTest.csv')
	k = 5
	final = []

	for i in evaluate:
		final.append(associate(distance_list(data, i, k), i))

	with open('results/result.csv', "w") as out:
		for i in final:
			out.write(f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]}\n")
	t1 = time.perf_counter()
	print(f'time elapsed: {t1 - t0}')
	confusion_mat(final, 4)

if __name__ == '__main__':
	main()
