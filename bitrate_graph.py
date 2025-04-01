#! /usr/bin/python3

import json
import ffmpeg

import matplotlib.pylab as plt

def getFrames():
    frame_dict = {}
    frame_count = 0

    video_probe = ffmpeg.probe("test.mp4", 
                               cmd='ffprobe', 
                               show_frames=None)

    for i in video_probe:
        if i == "frames":
            for d in video_probe[i]:
                frame_dict.update({frame_count: [
                                    float(d["best_effort_timestamp_time"]), 
                                    int(d["pkt_size"]), 
                                    d["key_frame"]]})
                frame_count += 1
    
    return frame_dict

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
    print(json.dumps(getFrames()))
