#! /usr/bin/python3

import json
import ffmpeg

def getFrames(video_to_probe):
    frame_dict = {}
    frame_count = 0

    video_probe = ffmpeg.probe(video_to_probe, 
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

if __name__ == "__main__":
    print(json.dumps(getFrames("test.mp4")))

