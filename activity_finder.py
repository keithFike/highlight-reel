#! /usr/bin/python3

import json

from frame_collector import getFrames

def findActivity(frames_dict):
    PKT_SIZE_THRESHOLD = 100

    frames_to_keep_dict = {}
    
    for frame in frames_dict:
        key_num = int(frame)
        if int(frames_dict[frame][1]) > PKT_SIZE_THRESHOLD:
            frames_to_keep_dict.update({key_num: frames_dict[frame]})
    
    return frames_to_keep_dict

if __name__ == "__main__":
    frames_dict = getFrames("test.mp4")

    frames_to_keep_dict = findActivity(frames_dict)

    print(json.dumps(frames_to_keep_dict))
