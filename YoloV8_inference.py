from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.pt")

results = model(['/content/drive/MyDrive/crosswalk-sample/crosswalk-sample/single-view/raw/0'])  # return a list of Results objects

for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    result.show()
    result.save(filename='resultv829590.jpg')