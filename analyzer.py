import cv2
import time
import sys
import math 
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


base_options = mp.tasks.BaseOptions(model_asset_path = "./pose-landmarker/pose_landmarker_heavy.task")

pose = mp.solutions.pose.Pose()

cap = cv2.VideoCapture('./source-videos/IMG_8139.mp4')

while cap.isOpened():
    # read frame
     ret, frame = cap.read()
     if not ret:
          break
    
     # process the frame
     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

     # # process the frame for pose detection
     # # Uncomment the line where pose_results is defined
     pose_results = pose.process(frame_rgb)

     # # draw skeleton on the frame
     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

     mp.solutions.drawing_utils.draw_landmarks(frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

     # display the frame
     cv2.imshow('Output', frame)

     if cv2.waitKey(1) == ord('q'):
          break

          
cap.release()
cv2.destroyAllWindows()

