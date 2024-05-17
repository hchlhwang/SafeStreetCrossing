import tensorrt as trt

TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
builder = trt.Builder(TRT_LOGGER)
network = builder.create_network(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
parser = trt.OnnxParser(network, TRT_LOGGER)

with open('llama3.onnx', 'rb') as model_file:
    parser.parse(model_file.read())

config = builder.create_builder_config()
config.max_workspace_size = 1 << 30  # 1 GB
config.set_flag(trt.BuilderFlag.FP16)

engine = builder.build_engine(network, config)
