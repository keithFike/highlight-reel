#! /usr/bin/python3

import ffmpeg
import json

from activity_finder import findActivity
from frame_collector import getFrames

def cutLocator(frames_to_keep_dict):
    out_cut = frames_to_keep_dict[1][0]
    previous_frame = 0

    for frame in frames_to_keep_dict:
        if int(frame) - previous_frame > 30 and int(frame) - previous_frame != int(frame):
            print(int(frame), previous_frame)
            print(int(frame) - previous_frame)
            out_cut = frames_to_keep_dict[frame][0]
            print(out_cut)
            print(previous_frame)
            break

        previous_frame += 1
    
    in_cut = frames_to_keep_dict[1][0]

    return in_cut, out_cut

def cutVideo(in_cut, out_cut):
    (ffmpeg
     .input('test.mp4', ss=in_cut, to=out_cut)
     .output('test2.mp4', c='copy')
     .run(overwrite_output=True))

def mergeVideo(list_of_videos):
    for video in list_of_videos:
        (ffmpeg
         .input(video)
         .output(stitched_video) #TODO: this
         .run(overwrite_output=True))

if __name__ == "__main__":
    frames_dict = getFrames("test.mp4")
    frames_to_keep_dict = findActivity(frames_dict)
    print(cutLocator(frames_to_keep_dict))
    #print(json.dumps(frames_to_keep_dict))
    #print("next\n\n\n")
    cutVideo(*cutLocator(frames_to_keep_dict))
    #print(frames_to_keep_dict)
