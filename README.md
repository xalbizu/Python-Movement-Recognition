# Python-Movement-Recognition
Motion Detection using Webcam

This Python script utilizes computer vision techniques to perform motion detection using a webcam. It captures real-time video from the webcam, detects motion, and saves the frames with motion to a folder. Additionally, it combines the saved frames into a video file.
Requirements

    Python 3.x
    OpenCV (cv2) library

**Installation**

Make sure you have Python 3.x installed on your system. If not, download and install it from the official Python website (https://www.python.org).

Install the OpenCV library by running the following command:

    pip install opencv-python

**Usage**

Connect your webcam to the computer.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using the following command:

    python3 motion_detection.py

The webcam will start capturing video, and the motion detection process will begin. The video window will show the live feed with motion highlights.

If there is significant motion detected (adjustable threshold), the frames with motion will be saved in the "frames" folder. After the script finishes, a video file named "video.mp4" will be generated by combining the saved frames.

    Press the 'q' key to exit the script and stop the video capture.

**Customization**

You can adjust the motion detection sensitivity by modifying the threshold value in the script (30 in the example script). Higher values will require more significant motion to be detected.

The frame size and frame rate of the output video can be modified by changing the respective parameters in the script ((640, 480) and 30 in the example script).
