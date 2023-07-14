import sys
import cv2


if len(sys.argv) != 3:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [IMAGE] [VIDEO]")
    sys.exit(1)

image = sys.argv[1]
video = sys.argv[2]

images = [image]
frame = cv2.imread(image)
height, width, layers = frame.shape

video_writer = cv2.VideoWriter(video, 0, 1, (width,height))

for image in images:
    video_writer.write(cv2.imread(image))

cv2.destroyAllWindows()
video_writer.release()
