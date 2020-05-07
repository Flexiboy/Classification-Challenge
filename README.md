# Classification-Challenge

> Authors Julien MARTIN-PRIN ([@Flexiboy](https://github.com/Flexiboy))

*This project is made within the Datascience and IA course in Year 3 of Engineering @ESILV*

## Project description

The classification challenge goal is to test our own implementation of the K-nn algorithm on a pre-selected dataset. The dataset used to train the K-nn is the file called `data.csv`. The data to test our algorithm is stored in the file `preTest.csv`. We have 4 input variable and a label to guess. There is 10 different labels.
> PS: All the data is located in the data folder, which also contains the initial subject (instructions in the pdf)

## Code explanation

**Loading the data:**

```python
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
```

Here, we are loading the data from a specified path. The data is also fromated to be much more easy to read in the future part of our programm.


**Calculating the euclidian distance:**

```python
def distance(reference, test_subject):
	dist = []
	for i in range(4):
		dist.append(float(abs(reference[i] - test_subject[i])))
	dist.append(reference[4])
	return dist
```

In this function, we are calculating the euclidian distance between a testing subject (a subject which we want to determine its label) and the a reference subject (a subject in our dataset).

> This can be resumed as calculating the euclidian distance between two subjects and associate the distance array with a label (here `reference[4]`)


**Getting the summ:**

```python
def summ(distlist):
	dist_summ = 0
	for i in distlist:
		if isinstance(i, float):
			dist_summ += i
	return dist_summ
```

In this section, we are summing each distance of a specified array (here distlist) to be able to better sort the distances array (matrix of distance arrays)


**Getting the top-k:**

```python
def distance_list(dataset, test_subject, k):
	distlist = []
	for i in dataset:
		distlist.append(distance(i, test_subject))
	final = sorted(distlist, key=lambda dist: summ(dist))
	return final[:k]
```

This is one of the two programm's core (the other one being the association). Here we are getting the distances from a specified subject (here `test_subject`) to all the subject in the dataset.
> In each iterations, we are getting the distance from the testing subject to a different subject in the dataset, each iteration representing a distinct subject.
Because we only want to sort the array with the distances parameters, we are appling a lambda function wich calculates the sum of the distances. 
> So, in fact, we are sorting the sum of distances, not distances
At the end, we only need the top-k distances (the closest distances from the testing subject if you prefer) so we only return the k-first row of the sorted array


**Counting the elements:**

```python
def element_count(array, index, to_find):
	number = 0
	for i in array:
		if i[index] == to_find:
			number += 1
	return number
```

This is the part where we count the labels (understand, we are counting the number of 'A' or 'B' or 'C' etc...). The first parameter refers to our top-k list, the second paramter is where to find what we are searching in each row and the last one is what we are searching ('A', 'B', 'C', etc...)


**The association:**

```python
def associate(evl, test_subject):
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
```

This is the second programm's core. This function associates a subject to a label. At first, we count the occurence number of each label and then we are associating a subject to the label that has the maximum occurence.


**Getting an output:**

```python
def show(data):
	for i in data:
		print(i)
```

This function only print an array.


**The main:**

```python
def main():
	data = load('data/data.csv')
	evaluate = load('data/preTest.csv')
	k = 20
	final = []

	for i in evaluate:
		final.append(associate(distance_list(data, i, k), i))
	show(final)

	with open('result.csv', "w") as out:
		for i in final:
			out.write(f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]}\n")
```

This is the main. We are just running the programm here and setting the k (so the limit for the top-k distances). We are also sending the output to a file called `result.csv`
