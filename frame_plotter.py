#! /usr/bin/python3

import matplotlib.pylab as plt

from frame_collector import getFrames

#for plotting frame dictionary with matplot
def plotFrames(frame_dict):
    plot_x = []
    plot_y = []

    for j in frame_dict:
        if frame_dict[j][2] != 1:
            plot_x.append(int(j))
            plot_y.append(int(frame_dict[j][1]))

    print(plot_x, plot_y)

    plt.plot(plot_x, plot_y)
    plt.show()

if __name__ == "__main__":
   frame_dict = getFrames("test.mp4") 
   plotFrames(frame_dict)
