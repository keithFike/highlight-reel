#! /usr/bin/python3

import ffmpeg

from activity_finder import findActivity
from bitrate_graph import getFrames

def cutLocator(frames_dict):
   pass 

def cutVideo(in_cut, out_cut):
    (ffmpeg
     .input('test.mp4', ss=in_cut, to=out_cut)
     .output('cut2.mp4', c='copy')
     .run())

if __name__ == "__main__":
    frames_dict = findActivity(getFrames())
    cutVideo(in_cut, out_cut)
