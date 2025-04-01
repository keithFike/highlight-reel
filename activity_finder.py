#! /usr/bin/python3

import json

from bitrate_graph import getFrames

def findActivity(frames_dict):
    PKT_SIZE_THRESHOLD = 100

    for frame in frames_dict:
        if int(frames_dict[frame][1]) < PKT_SIZE_THRESHOLD:
            frames_dict[frame].append(1)
        else:
            frames_dict[frame].append(0)

if __name__ == "__main__":
    frames_dict = getFrames()

    findActivity(frames_dict)

    print(json.dumps(frames_dict))
