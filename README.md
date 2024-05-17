<<<<<<< HEAD
# SafeStreetCrossing

SafeStreetCrossing is a project that uses vision-language models, specifically MiniGPT-v2 and Llama3, to provide scene descriptions for street crossing scenarios. The goal of this project is to enhance the safety of blind and low-vision (BLV) individuals by leveraging vision-language models to support safe decision-making for street crossing.

## Todo

- [ ] VLM inference test
- [ ] Human evaluation
- [ ] TensorRT-LLM
- [ ] TensorRT-LLM for VLM weights
- [ ] Scene graph
- [ ] Scene graph-VLM connection

## Features

- Scene description generation using vision-language models: MiniGPT-v2 powered by Llama3
- Vision-based models with scene graph understanding to predict street crossing decisions
- Potential applications in assistive technologies for BLV people

## Installation & setup

To set up the SafeStreetCrossing project, follow these steps:

1. Clone the repository:

  ```bash
  git clone https://github.com/your-username/SafeStreetCrossing.git
  cd SafeStreetCrossing
  ```
2. Install the MiniGPT-4 dependencies
  ```bash
  cd MiniGPT-4
  pip install -r requ.txt
  ```
3. Install the Llama3 weights into the MiniGPT-4/models/Meta-Llama-3-8B-Instruct directory:
  ```bash
  cd MiniGPT-4
  git clone https://github.com/meta-llama/llama3.git
  cd llama3
  bash download.sh
  ```
4. Create a models directory and download the checkpoint:
  ```bash
  cd MiniGPT-4
  mkdir models
  cd models
  # Download the checkpoint from here and place it in the models directory.
  ```

## Training

1. Fine-tune the model (MiniGPT-v2 with Llama3)
  ```bash
  torchrun --nproc-per-node 1 train.py --cfg-path multimodal_685/minigptv2_finetune_llama3.yml
  ```

## Acknowledgments
We would like to express our gratitude to the researchers behind the MiniGPT-4 and Llama3 models, as well as the open-source community for their valuable contributions. We also extend our sincere thanks to the following individuals for their contributions to this project, which is part of the Advanced Natural Language Processing course and the Guide Dog Robot project:
- [Hochul Hwang](https://hchlhwang.github.io), [Karthik Ravichandran](https://www.linkedin.com/in/karthik-ravichandran-181173a9/), [Parth Goel](https://www.linkedin.com/in/parth-goel-03/), [Deepika S Velu](https://www.linkedin.com/in/deepu17), [Aishwarya Sahoo](https://www.linkedin.com/in/aishwarya-sahoo-x/)

## Publications

Please take a look at our previous paper related to SafeStreetCrossing:

```bibtex
@article{hwang2024safe,
  title={Is it safe to cross? Interpretable Risk Assessment with GPT-4V for Safety-Aware Street Crossing},
  author={Hwang, Hochul and Kwon, Sunjae and Kim, Yekyung and Kim, Donghyun},
  journal={arXiv preprint arXiv:2402.06794},
  year={2024}
}
=======
# Yolov8 and V9 TensorRT
Yolo_ Model compare with inference regarding better performance and predictions.


YoloV8_Model - Single View
![Picture11](https://github.com/Deepika-S1708/YoloV8-and-V9-TensorRT/assets/68435141/e1917dee-2c2b-473e-a16d-72d7695f24f5)
YoloV9_Model - Multi View
![Picture23](https://github.com/Deepika-S1708/YoloV8-and-V9-TensorRT/assets/68435141/91312da5-57ec-43c3-8ce0-ff45f593f586)

YoloV8_Model Custom Dataset (Tensor RT) - Multiview

![3_06-usps-stitched_15710_jpg rf 2fa5159713956d3031586c1ef81ca4d0](https://github.com/Deepika-S1708/YoloV8-and-V9-TensorRT/assets/68435141/3bbed834-017d-4942-b821-2d9275d73658)


![3_04-milkcow-stitched_1210_jpg rf 5c42677f327fc7c9fea1f77d24738066](https://github.com/Deepika-S1708/YoloV8-and-V9-TensorRT/assets/68435141/ef963230-90e7-4161-91a9-9a669d78ae96)


>>>>>>> origin/master
