import numpy as np

# dictionary for number of bytes allocated to np type
bits_alloc_to_np_type = {16: np.uint16,
                         8: np.uint8,
                         }


class PredictionSample:
    """
    PredictionSample is faking a tensorflow script. shape of arrays are transformed as the original TF script.
    """
    def __init__(self, model_path, channels, n_class, layers, features_root):
        # define network
        self.n_class = n_class
        # This is commented out as for unit testing tf is not available on Windows.
        self.model_path = model_path
        self.channels = channels
        self.layers = layers
        self.features_root = features_root
        self.offset = 2
        print "Prediction2DUnet ctor - channels: ", self.channels, ", n_class: ", self.n_class, ", layers: ", self.layers, ", features_root: ", self.features_root
        # This is just sample code to check that the script is actually doing something
        self.thresholds = [200, 600, 1200]
        print ">> Thresholds: "
        for threshold in self.thresholds:
            print threshold

    def get_offset(self):
        return self.offset

    def evaluate(self, raw_data, num_rows, num_columns, bits_allocated):
        print "Prediction2DUnet evaluate - num_rows: ", num_rows, ", num_columns: ", num_columns

        # transform byte array to 16 bits pixels
        np_type = bits_alloc_to_np_type.get(bits_allocated)
        pixels = np.frombuffer(raw_data, dtype=np.uint16 if np_type is None else np_type)
        print "Pixels shape: ", pixels.shape

        # padding is currently magic number. it shall be returned by the real 2DUnet evaluation
        # padding is calculated but not used as Malibu expect the same array dimensions per class.
        padding = self.offset / 2
        pred_rows = num_rows - 2 * padding  # 472 with the real data
        pred_cols = num_columns - 2 * padding  # 472 with the real data

        # we fill the prediction array without considering the padding as this is a dummy test.
        prediction = np.zeros([num_rows * num_columns, self.n_class], dtype = np.uint8)

        if self.model_path is not None:
            # x_test is not used as this is for tf only.
            x_test = np.reshape(pixels[0: num_rows * num_columns], [1, num_rows, num_columns, 1])

            class_count = [0] * self.n_class
            it = np.nditer(pixels)

            index = 0

            for pixel in it:
                #print "Pixel value: ", pixel
                classif = self.n_class - 1

                for t_index in range(0, self.n_class - 1):
                    threshold = self.thresholds[t_index]
                    if pixel < threshold:
                        classif = t_index
                        break

                prediction[index, classif] = 100
                class_count[classif] += 1
                index += 1

            for index in range(0, self.n_class):
                print "Class: ", index, ": number of pixels: ", class_count[index]

            print "Prediction2DUnet evaluate - run successfully"

        else:
            print "Prediction2DUnet evaluate - error: model path is null"

        # reshape  here to what the real 2D unet would return
        prediction = np.reshape(prediction, [1, num_rows, num_columns, self.n_class])
        # reshape to what is expected by malibu
        prediction = np.reshape(prediction[:], [num_rows * num_columns * self.n_class])
        print "Prediction shape: ", prediction.shape

        return prediction.tolist()
