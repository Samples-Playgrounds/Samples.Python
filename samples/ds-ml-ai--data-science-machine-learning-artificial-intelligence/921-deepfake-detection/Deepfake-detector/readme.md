
https://github.com/saiadupa/Deepfake-detector

pip install deepfake_detector


from deepfake_detector import DeepfakeDetector

# Create a detector object with a custom threshold
detector = DeepfakeDetector(threshold=0.5)

# Detect deepfakes in a video file
detector.detect_from_video('path_to_video.mp4')

# Use webcam (source=0) for live detection
detector.detect_from_video(source=0)




from deepfake_detector import DeepfakeDetector

# Create a detector object with a custom threshold
detector = DeepfakeDetector(threshold=0.5)

# Detect deepfakes in an image
result = detector.detect_from_image('path_to_image.jpg')
print(f'The image is classified as: {"FAKE" if result > 0.5 else "REAL"}')



