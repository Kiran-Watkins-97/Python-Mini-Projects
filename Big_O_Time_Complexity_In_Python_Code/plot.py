import matplotlib.pyplot as plt


def plot (xarr, yarr):
    plt.plot(xarr,yarr)
    plt.xlabel('n - array size')
    plt.ylabel('iteration - repeat count')
    plt.title('Plot of Size vs Iterations')
    plt.show()