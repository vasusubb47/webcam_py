from webcam import Webcam
import cv2
from datetime import datetime
import numpy as np
from numpy.typing import NDArray

def main():
    # Define a simple webcam object that will get video stream from webcam (src=0),
    #  with a frame width of 640 (auto setting heigth to keep original aspect ratio)
    webcam = Webcam(src=0)
    print(f"Frame size: {webcam.w} x {webcam.h}")

    web = webcam

    for frame in webcam:
        # Show the frames in a cv2 window
        cv2.imshow('Webcam Frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        # Break the loop if the user presses the 'q' key

        if cv2.waitKey(1) & 0xFF == ord('q'):
            for _ in range(0, 3):
                frame = web.read_next_frame()
                save_frame(frame)

            break

def save_frame(frame: NDArray[np.int8]):
    # Convert the frame to RGB format before saving it, as OpenCV uses BGR format by default
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frameTime = datetime.now()
    imageName = f"frame_{frameTime.year}{frameTime.month}{frameTime.day}_{frameTime.hour}{frameTime.minute}{frameTime.second}_{frameTime.microsecond}.png"

    # Save the frame to a file
    cv2.imwrite(imageName, frame)

if __name__ == "__main__":
    main()

