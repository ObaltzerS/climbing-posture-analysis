import cv2
import numpy as np
import mediapipe as mp




class analyzer:

     def __init__(self):
          # self.base_options = mp.tasks.BaseOptions(model_asset_path = "./pose-landmarker/pose_landmarker_heavy.task")
          self.pose = mp.solutions.pose.Pose()
          self.video = None

     def getFile(self, path):
          self.video = cv2.VideoCapture(path) #get video from file path
     
     def processFrame(self, frame):
          """
          This method will process one frame from the video
          """
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # grab rbg of frame
          pose_results = self.pose.process(frame_rgb) # process frame with pose detection
          mp.solutions.drawing_utils.draw_landmarks(frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS) # draw pose on frame
          return frame # return frame with pose

     def processVideo(self):
          """
          This method will process the video
          """
          while self.video.isOpened():
               # read frame
               ret, frame = self.video.read()
               if not ret:
                    break
               # process the frame
               frame = self.processFrame(frame)
               # display the frame
               cv2.imshow('Output', frame)
               if cv2.waitKey(1) == ord('q'):
                    break

          self.video.release()
          cv2.destroyAllWindows()

     def calculate_arm_angle(a,b,c):
          a = np.array(a) # First
          b = np.array(b) # Mid
          c = np.array(c) # End
    
          radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
          angle = np.abs(radians*180.0/np.pi)
          
          if angle >180.0:
               angle = 360-angle
        
          return angle 

# cap = cv2.VideoCapture('./source-videos/IMG_5925.mov')

# while cap.isOpened():
#     # read frame
#      ret, frame = cap.read()
#      if not ret:
#           break
    
#      # process the frame
#      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#      # # process the frame for pose detection
#      # # Uncomment the line where pose_results is defined
#      pose_results = pose.process(frame_rgb)

#      # # draw skeleton on the frame
#      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#      mp.solutions.drawing_utils.draw_landmarks(frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
#      print(pose_results.pose_landmarks)
#      # display the frame
#      cv2.imshow('Output', frame)

#      if cv2.waitKey(1) == ord('q'):
#           break

          
# cap.release()
# cv2.destroyAllWindows()

