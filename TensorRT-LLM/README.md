# Meta-Llama3-optimization-TensoRT-LLM
Turbocharging Meta Llama 3 Performance with NVIDIA TensorRT-LLM

# TensorRT LLM -  Meta Llama -3

# Getting started with installation
1. Install the dependencies needed for installing TensorRT-LLM inside the container from open-source library.
   
   ``` shell
   git clone -b v0.8.0 https://github.com/NVIDIA/TensorRT-LLM.git
   cd TensorRT-LLM
   ```
# Retrieving the model weights
2. Pull the weights (and tokenizer files) for the instruction-tuned variant of the 8-billion-parameter Llama 3 model from the Hugging Face Hub.

   ``` shell
   git lfs install
   git clone https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
   ```
Note that using this model is subject to a particular license. Agree to the terms and authenticate with HuggingFace to download the necessary files. 

# Running the TensorRT-LLM container
3.  We’ll launch a base docker container and install the dependencies required by TensorRT-LLM.
``` shell
# Obtain and start the basic docker image environment.
docker run --rm --runtime=nvidia --gpus all --volume ${PWD}:/TensorRT-LLM --entrypoint /bin/bash -it --workdir /TensorRT-LLM nvidia/cuda:12.1.0-devel-ubuntu22.04

# Install dependencies, TensorRT-LLM requires Python 3.10
apt-get update && apt-get -y install python3.10 python3-pip openmpi-bin libopenmpi-dev

# Install the stable version (corresponding to the cloned branch) of TensorRT-LLM.
pip3 install tensorrt_llm==0.8.0 -U --extra-index-url https://pypi.nvidia.com
```

# Compiling the model
4. The next step in the process is compiling the model into a TensorRT engine with model weights and a model definition written in the TensorRT-LLM Python API. 
``` shell
# Log in to huggingface-cli
# You can get your token from huggingface.co/settings/token
huggingface-cli login --token *****

# Build the Llama 8B model using a single GPU and BF16.
python3 examples/llama/convert_checkpoint.py --model_dir ./Meta-Llama-3-8B-Instruct \
            --output_dir ./tllm_checkpoint_1gpu_bf16 \
            --dtype bfloat16

trtllm-build --checkpoint_dir ./tllm_checkpoint_1gpu_bf16 \
            --output_dir ./tmp/llama/8B/trt_engines/bf16/1-gpu \
            --gpt_attention_plugin bfloat16 \
            --gemm_plugin bfloat16
```

When we finish running the build script, we should expect to see the following three files in the /tmp/llama/8B/trt_engines/bf16/1-gpu folder:

rank0.engine is the main output of our build script, containing the executable graph of operations with the model weights embedded. 
config.json includes detailed information about the model, like its general structure and precision, as well as information about which plug-ins were incorporated into the engine. 

# Running the model

To run the model locally, we can execute the following command:
``` shell
python3 examples/run.py --engine_dir=./tmp/llama/8B/trt_engines/bf16/1-gpu --max_output_len 100 --tokenizer_dir ./Meta-Llama-3-8B-Instruct --input_text "How do I count to nine in French?"
```
