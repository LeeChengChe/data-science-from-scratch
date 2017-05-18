from sklearn import datasets
iris = datasets.load_iris()
print iris.data
print iris.target
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
print clf
clf.fit(iris.data[:-10], iris.target[:-10])
result=clf.predict(iris.data[-10:])
print ("predict:")
print result
print ("actual")
print (iris.data[-10:])
print (iris.target[-10:])
digits = datasets.load_digits()
clf.fit(digits.data[:-1],digits.target[:-1])
print(digits.data[-1])
print(digits.target[0:5])
print(len(digits.data))
import matplotlib.pyplot as plot
plot.figure(1, figsize=(3,3))
plot.imshow(digits.images[0], cmap=plot.cm.gray_r, interpolation='nearest')
plot.show()
result=clf.predict(digits.data[0])
print result
print (digits.target[0])