"""
This is an attempt to create an animated gif snippet from a video
using the 'cv2' and 'imageio' python modules.

References:
- https://theailearner.com/2021/05/29/creating-gif-from-video-using-opencv-and-imageio/
- https://note.nkmk.me/en/python-opencv-video-to-still-image/
"""


import os
import sys

import cv2
import imageio


def create_animated_gif_from_video(
    video_path: str,
    output_path: str,
    number_of_images: int,
    duration_of_each_frame: int,  # in miliseconds
    loop: int,  # should the snippet loop
) -> None:
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    number_of_images_needed = number_of_images * 5
    if length < number_of_images_needed:
        raise ValueError(f"the video length is {length} and is less than {number_of_images_needed} frames long")
    skip_frames = int(float(length) / float(number_of_images))
    pos = 0
    image_list = []
    for _ in range(number_of_images):
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
        ret, frame = cap.read()
        assert ret is not None
        # we need this conversin to RGB for the animated gif to look right
        resized_frame = cv2.resize(frame, (200,100))
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        image_list.append(rgb_frame)
        pos += skip_frames
    cap.release()
    imageio.mimsave(output_path, image_list, loop=loop, duration=duration_of_each_frame)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        video = sys.argv[1]
        snippet = sys.argv[2]
    else:
        video = "data/make_video_snippet/hitler_uses_git.mp4"
        snippet = "data/make_video_snippet/hitler_uses_git_snippet_gif.gif"
    if os.path.isfile(snippet):
        os.unlink(snippet)
    create_animated_gif_from_video(
        video,
        snippet,
        number_of_images=10,
        duration_of_each_frame=1000,
        loop=0,
    )
