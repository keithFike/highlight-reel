#! /usr/bin/python3

import json

from frame_collector import getFrames

def findActivity(frames_dict):
    PKT_SIZE_THRESHOLD = 100
    
    #append 1 to frame's data list if below packet size threshold
    for frame in frames_dict:
        if int(frames_dict[frame][1]) < PKT_SIZE_THRESHOLD:
            frames_dict[frame].append(1)
        else:
            frames_dict[frame].append(0)

if __name__ == "__main__":
    frames_dict = getFrames("test.mp4")

    frames_dict = findActivity(frames_dict)

    print(json.dumps(frames_dict))
