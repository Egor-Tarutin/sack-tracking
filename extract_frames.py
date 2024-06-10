import math

import cv2

# Path to the video file
videoFile = "./task.mp4"
# Folder where you want to save the frames
imagesFolder = "./data"

# Open the video
cap = cv2.VideoCapture(videoFile)
# Get the frame rate of the video
frameRate = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    # Get the current frame number
    frameId = cap.get(cv2.CAP_PROP_POS_FRAMES)
    ret, frame = cap.read()
    if not ret:
        break
    # Check if the current frame is the one you want to extract
    if frameId % math.floor(frameRate) == 0:
        # Create a filename for each frame
        filename = imagesFolder + "/frame_" + str(int(frameId)) + ".jpg"
        # Save the frame as a JPEG file
        cv2.imwrite(filename, frame)

# Release the video capture object
cap.release()
print("Done!")
