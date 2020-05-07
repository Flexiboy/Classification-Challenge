# Classification-Challenge

> Authors Julien MARTIN-PRIN ([@Flexiboy](https://github.com/Flexiboy])

*This project is made within the Datascience and IA course in Year 3 of Engineering @ESILV*

## Project description

The classification challenge goal is to test our own implementation of the K-nn algorithm on a pre-selected dataset. The dataset used to train the K-nn is the file called `data.csv`. The data to test our algorithm is stored in the file `preTest.csv`. We have 4 input variable and a label to guess. There is 10 different labels.

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

```python
def distance(reference, test_subject):
	dist = []
	for i in range(4):
		dist.append(float(abs(reference[i] - test_subject[i])))
	dist.append(reference[4])
	return dist
```

```python
def summ(distlist):
	dist_summ = 0
	for i in distlist:
		if isinstance(i, float):
			dist_summ += i
	return dist_summ
```

```python
def distance_list(dataset, test_subject, k):
	distlist = []
	for i in dataset:
		distlist.append(distance(i, test_subject))
	final = sorted(distlist, key=lambda dist: summ(dist))
	return final[:k]
```

```python
def element_count(array, index, to_find):
	number = 0
	for i in array:
		if i[index] == to_find:
			number += 1
	return number
```

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

```python
def show(data):
	for i in data:
		print(i)
```

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
