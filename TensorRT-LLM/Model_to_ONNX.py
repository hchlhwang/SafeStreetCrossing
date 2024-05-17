import torch
from transformers import LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained('huggingface/llama3')
dummy_input = torch.zeros(1, 1, dtype=torch.long)

torch.onnx.export(model, dummy_input, 'llama3.onnx', opset_version=13, input_names=['input'], output_names=['output'])
