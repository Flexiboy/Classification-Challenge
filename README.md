# Classification-Challenge

> Authors Julien MARTIN-PRIN ([@Flexiboy](https://github.com/Flexiboy])

*This project is made within the Datascience and IA course in Year 3 of Engineering @ESILV*

## Project description

The classification challenge goal is to test our own implementation of the K-nn algorithm on a pre-selected dataset. The dataset used to train the K-nn is the file called `data.csv`. The data to test our algorithm is stored in the file `preTest.csv`. We have 4 input variable and a label to guess. There is 10 different labels.

## Code explanation

**Loading the data:**

```
5 def load(path):
6         data = []
7         temp = []
8         temp2 = []
9         with open(path, "r") as inp:
10                 for i in inp:
11                         for j in range(5):
12                                 if j == 4:
13                                         temp.append((i.split(';')[j]).split('\n')[0])
14                                 else:
15                                         temp.append(i.split(';')[j])
16                         data.append(temp)
17                         temp = []
18         return data
```

Here, we are loading the data from a specified path. The data is also fromated to be much more easy to read in the future part of our programm.

