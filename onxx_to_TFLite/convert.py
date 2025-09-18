import onnx

onnx_model = onnx.load("fomo96p01.onnx")
print(onnx_model.graph.input[0].type.tensor_type.shape)

onnx_model.graph.input[0].name = "input_1"

for node in onnx_model.graph.node:
    for i, input_name in enumerate(node.input):
        if input_name == "input.1":
            node.input[i] = "input_1"

onnx.save(onnx_model, "renamed_model96p01.onnx")
