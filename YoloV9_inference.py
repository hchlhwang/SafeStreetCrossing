from ultralytics import YOLO

# Load the YOLOv9 model
model = YOLO('yolov9c.pt')

# Run predictions
results = model.predict('/content/sample_data/stitched_1.jpg')

for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    result.show()
    result.save(filename='result1.jpg')