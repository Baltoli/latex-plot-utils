import matplotlib.pyplot as plt

SMALL_SIZE = 6
MEDIUM_SIZE = 8
BIGGER_SIZE = 10

plt.rc('font', size=SMALL_SIZE)                 # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)            # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)           # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)           # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)           # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)           # legend fontsize
plt.rc('legend', title_fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)         # fontsize of the figure title
