import numpy

logged_values = numpy.array([
    [0, 0, 0, 0, 0],
    [300, 0, 0, 0, 1],
    [0, 300, 0, 0, 2],
    [0, 0, 300, 0, 3],
    [0, 0, 0, 300, 4]
])

features = logged_values[:, 0:4]
labels = logged_values[:, 4].T
