from ultralytics import YOLO

# lOAD Model
model = YOLO('Modelos/prueba.pt')

# EXPORT
model.export(format = 'onnx')