from Prediction2DUnet import PredictionSample
import numpy as np

# original pixels are 16 bits
array16 = np.array([0, 0, 0, 0, 0, 0, 0, 1000, 1500, 900, 800, 0, 0, 100, 200, 500, 650, 0, 0, 2000, 750,
                    150, 256, 0, 0, 1150, 50, 1300, 1800, 0, 0, 0, 0, 0, 0, 0],
                   dtype=np.uint16)
print "array16 type: ", type(array16[0])
print "array16 shape: ", array16.shape

# malibu provides data as 8 bits array: requires conversion
array8 = np.frombuffer(array16, dtype=np.uint8)
print "array8 type: ", type(array8[0])
print "array8 shape: ", array8.shape

prediction_class = PredictionSample("my_model.xml", 1, 4, 16, 1)
result = prediction_class.evaluate(array8, 6, 6, 16)

print "results: "
idx = 0
for pred in result:
    print idx, " : ", pred
    idx += 1
