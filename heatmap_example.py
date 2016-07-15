# Adapted from https://gist.github.com/teechap/9c066a9ab054cc322877 by Travis Chapman
'''
Most heatmap tutorials I found online use pyplot.pcolormesh with random sets of
data from Numpy; I just needed to plot x, y, z values stored in lists--without
all the Numpy mumbo jumbo. Here I have code to plot intensity on a 2D array, and
I only use Numpy where I need to (pcolormesh expects Numpy arrays as inputs).
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cb

# Import x,y coordinate data
x,y = [], []
fp = open("test-data.txt")
with open("test-data.txt") as fp:
    for i, line in enumerate(fp):
       if i == 1:
            # Take out the newline case
            # List looks like: [..., ' 0.235', ' 0.34\n']
            x_list = line.split(',')
            x_list.pop(-1)
            for j, item in enumerate(x_list):
                x_list[j] = float(item)

            x.extend(x_list)
       if i == 3:
            y_list = line.split(',')
            y_list.pop(-1)
            for j, item in enumerate(y_list):
                y_list[j] = float(item)
                
            y.extend(y_list)
fp.close()

print "X:", x
print "Y:", y
imageFile = cb.get_sample_data('./Contact Center.png')
image = plt.imread(imageFile)

plt.imshow(image, aspect='auto')
plt.plot(x, y, 'ro')
plt.show()
