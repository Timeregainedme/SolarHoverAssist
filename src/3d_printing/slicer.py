def slice_model(model_file, layer_height):
    print(f"Slicing {model_file} with layer height {layer_height}mm.")
    # 示例代码：模拟切片逻辑
    return f"Sliced model with {int(10/layer_height)} layers."

if __name__ == "__main__":
    result = slice_model("model.stl", 0.2)
    print(result)
