#import torch
#from PIL import Image
#import cv2

# Load the custom YOLOv9 model
#model_path = '/content/Custom-Yolo-detector.pt'
#model = torch.hub.load('ultralytics/yolov9', 'custom', path_or_model=model_path)
#model = YOLO('/content/Custom-Yolo-detector.pt')

import yolov9
import argparse

# Function to perform inference and classify the image
def main(args):

    # Load the image
    #img = Image.open(image_path)
    # load pretrained or custom model
    model = yolov9.load(
        args.model_path, device= args.device
    )

    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.classes = None  # (optional list) filter by class

    # set image/video
    imgs = args.source_path

    #set threshold
    th = args.threshold

    # perform inference
    #results = model(imgs)

    # inference with larger input size and test time augmentation
    results = model(imgs, size=640)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    confidences = predictions[:, 4]
    categories = predictions[:, 5]

    # show detection bounding boxes on image
    results.show()

    # Analyze the inference results
    scores = 0
    max_conf = 0
    for *xyxy, conf, cls in predictions.tolist():
        max_conf = max(max_conf, conf)
        if cls == 0:  # Assuming 'go' class is labeled as 0
            scores += conf
        elif cls == 1:  # Assuming 'stop' class is labeled as 1
            scores -= conf

    # Classify based on total scores
    classification = 'go' if scores > th else 'stop'

    if len(predictions)==0:
      classification = 'null'
    
    print(f"The image is classified as: {classification}")

    if(args.get_info):
        print(f"bounding box: {boxes[confidences.index(max_conf)]}", f"confidence: {max_conf}")


if __name__== "__main__":
    parser = argparse.ArgumentParser()

    # paths
    parser.add_argument("--source_path", default="/content/sample.png", type =str)
    parser.add_argument("--model_path", default= "/content/Custom-Yolo-detector.pt", type =str)
    parser.add_argument("--device", default="cpu", type =str)

    # hyperparameters
    parser.add_argument("--conf", default= 0.25, type =float)
    parser.add_argument("--iou", default= 0.45, type= float)
    parser.add_argument("--get_info", action="store_false")
    parser.add_argument("--threshold", default = 0.0, type = float)

    print(parser.parse_args())
    main(parser.parse_args())