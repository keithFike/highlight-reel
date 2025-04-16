#! /usr/bin/python3

import ffmpeg

from activity_finder import findActivity
from bitrate_graph import getFrames

def cutLocator(frames_dict):
    for frame in frames_dict:
        if frames_dict[frame][3] != 0:
            print(frames_dict[frame][0])
    #return in_cut, out_cut

def cutVideo(in_cut, out_cut):
    (ffmpeg
     .input('test.mp4', ss=in_cut, to=out_cut)
     .output('cut2.mp4', c='copy')
     .run())

if __name__ == "__main__":
    frames_dict = getFrames("test.mp4")
    findActivity(frames_dict)
    cutLocator(frames_dict)
    #cutVideo(in_cut, out_cut)
