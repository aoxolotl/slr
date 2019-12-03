import os
import sys
import argparse
import webvtt
import ffmpeg
import hashlib
import time
import subprocess


def parse_cc(filename):
    """
    Parse VTT formatted subtitles.
    :param filename:
    :return:
    """
    if filename.split('.')[-1] != 'vtt':
        print("Only VTT file format supported for now")
        return -1

    return [(caption.start, caption.end, ) for caption in webvtt.read(filename)]


def add_buffer_time(timestamps, btime):
    return [[t[0] - btime, t[1] + btime] for t in timestamps]


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Dump video frames corresponding to caption time")
    parser.add_argument('-f', '--file', help="input video file name")

    args = parser.parse_args()

    filename = args.file
    dirname = os.path.dirname(filename)
    newdir = os.path.splitext(filename)[0]
    newdir = newdir.replace("Training", "Training/frames", 1)
    os.mkdir(newdir)

    subname = os.path.splitext(filename)[0] + '.en.vtt'
    for caption in webvtt.read(subname):
        md5 = hashlib.md5(caption.text.encode('utf-8')).hexdigest()
        subprocess.run(['/usr/bin/ffmpeg', '-ss', caption.start, '-t', caption.end, \
                        '-i', repr(filename), '-filter:v', "\"crop=740:720:500:0\"", \
                        repr(os.path.join(newdir, caption.start + md5[1:10] + '_out%6d.png'))])
        with open(os.path.join(newdir, md5) + '.txt', 'w') as cc:
            cc.write(caption.text)
        # Cut video frame
        # Naming? 1. md5 of caption .
        # match to subtitle
