import numpy as np

context = engine.create_execution_context()
input_shape = (1, 1)
output_shape = (1, model.config.vocab_size)
d_input = cuda.mem_alloc(1 * np.prod(input_shape) * np.dtype('float16').itemsize)
d_output = cuda.mem_alloc(1 * np.prod(output_shape) * np.dtype('float16').itemsize)
bindings = [int(d_input), int(d_output)]

def infer(input_data):
    cuda.memcpy_htod(d_input, input_data)
    context.execute_v2(bindings)
    output_data = np.empty(output_shape, dtype=np.float16)
    cuda.memcpy_dtoh(output_data, d_output)
    return output_data

input_data = np.zeros(input_shape, dtype=np.float16)
output_data = infer(input_data)
