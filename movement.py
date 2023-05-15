import cv2
import os

# Capture video from the webcam
cap = cv2.VideoCapture(0)  # Argument 0 indicates that the first available camera will be used
i = 0
# Read the first frame
ret, frame_prev = cap.read()

os.system('mkdir frames')
# Convert the frame to grayscale
prev_gray = cv2.cvtColor(frame_prev, cv2.COLOR_BGR2GRAY)

# Create a window to display the result
cv2.namedWindow('Motion Detection', cv2.WINDOW_NORMAL)

while True:
    # Read each frame of the video
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the current and previous frames
    frame_diff = cv2.absdiff(gray, prev_gray)

    # Apply a threshold to highlight the differences
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    num_white = cv2.countNonZero(thresh)

    if num_white > 100:
        frame[thresh == 255] = (0, 0, 255)
        cv2.putText(frame, 'Motion Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imwrite('frames/' + str(i) + '_frame.jpg', frame)
        i += 1
    # Show the resulting frame with highlighted differences
    cv2.imshow('Motion Detection', frame)

    # Update the previous frame
    prev_gray = gray.copy()

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close the window
cap.release()
cv2.destroyAllWindows()

# Create a video from the frames
video_out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
# Iterate through the images and write them to the video

for file in sorted(os.listdir('frames/'), key=lambda x: int(x.split('_')[0])):
    print(file)
    image_path = os.path.join('frames/', file)
    image = cv2.imread(image_path)
    video_out.write(image)

# Release resources
video_out.release()

os.system('rm -r frames/')
