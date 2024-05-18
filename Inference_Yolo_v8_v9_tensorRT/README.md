# Yolov8 and V9 TensorRT
---
Yolov8s Tensor RT
![stitched_6292](https://github.com/Deepika-S1708/YoloV8-and-V9-TensorRT/assets/68435141/3e21457d-0855-4c0d-a212-c344f0b088df)


# Prepare the environment

1. Install `CUDA` follow [`CUDA official website`](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#download-the-nvidia-cuda-toolkit).

   🚀 RECOMMENDED `CUDA` >= 12.2

2. Install `TensorRT` follow [`TensorRT official website`](https://developer.nvidia.com/nvidia-tensorrt-8x-download).

   🚀 RECOMMENDED `TensorRT` >= 8.6.1

3. Install [`ultralytics`](https://github.com/ultralytics/ultralytics) package for ONNX export or TensorRT API building.

   ``` shell
    pip install ultralytics==8.0.196

    from IPython import display
    display.clear_output()

    import ultralytics
    ultralytics.checks()

   ```
4. Prepare your own PyTorch weight such as `yolov8s.pt`, `yolo9c.pt`.

***NOTICE:***

Please use the latest `CUDA` and `TensorRT`, so that you can achieve the fastest speed !

If you have to use a lower version of `CUDA` and `TensorRT`, please read the relevant issues carefully !

# Normal Usage

If you get ONNX from origin [`ultralytics`](https://github.com/ultralytics/ultralytics) repo, you should build engine by yourself.

You can only use the `Python` inference code to deserialize the engine and do inference.

5. We have created the **custom dataset ** using 'Roboflow' with annotate tranied images.

6. Make directory as datasets inside the datasets folder import the roboflow api key download the dependencies packages to support.
 ``` shell  
 !mkdir /content/datasets
 %cd /content/datasets
 # Roboflow API Key to import the dataset to colab
 !pip install roboflow


 from roboflow import Roboflow
 rf = Roboflow(api_key="XXXXXXXXXXXXXXXXXXXXX")
 project = rf.workspace("deepika-xxxxxx").project("object-detection")
 version = project.version(1)
 dataset = version.download("yolov8")
 ```
Download the zip files and extract the zip files of datasets.

7. Run the epochs weights with our custom datasets. train, test and validate the finalized two sets one is best.pt and last.pt versions.
``` shell
!yolo task=detect mode=train model=yolov8s.pt imgsz=1920 data="/pathto/data.yaml" epochs=35 batch=2 name=yolov8s_custom
```
we have mentioned 35 epochs and images size 1920 to get a better mean average precision values of each epochs weight and which epochs will provide best values.

# Tensor RT Dependencies
8. Install the tensorrt dependencies 
``` shell
!pip install torch torchvision onnx
!pip install tensorrt
!pip install tensorrt_lean
!pip install tensorrt_dispatch
!pip install onnx onnxsim onnxruntime-gpu
```
Downloading the torch vision, tensorrt and onnx packages are supporting.

9. Check the tensorrt version.
``` shell
import tensorrt
print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())
```
#
# Covert the our custom model best.pt to tensorrt version as best.engine and predict the model to do inference with Tensor RT model.
``` shell
from ultralytics import YOLO
import numpy as np
np.bool = np.bool_


!yolo export model="/path_to_/weights/best.pt" format=engine
# creates 'best.engine'


# Run inference with the exported model
!yolo predict model='/path_to_/weights/best.engine' imgsz=1920 source='/path_to/test_images'
```





