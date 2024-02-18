import gzip
import struct
import numpy as np
 
def load_dataset(dataset_path):
def unpack_mnist_data(filename: str, label=False):
with gzip.open(filename) as gz:
struct.unpack('I', gz.read(4))
n_items = struct.unpack('>I', gz.read(4))
if not label:
n_rows = struct.unpack('>I', gz.read(4))[0]
n_cols = struct.unpack('>I', gz.read(4))[0]
res = np.frombuffer(gz.read(n_items[0] * n_rows * n_cols), dtype=np.uint8)
res = res.reshape(n_items[0], n_rows * n_cols) / 255.0
else:
res = np.frombuffer(gz.read(n_items[0]), dtype=np.uint8)
res = res.reshape(-1)
return res
 
X_train = unpack_mnist_data(os.path.join(dataset_path, 'train-images.gz'), False)
y_train = unpack_mnist_data(os.path.join(dataset_path, 'train-labels.gz'), True)
X_test = unpack_mnist_data(os.path.join(dataset_path, 'test-images.gz'), False)
y_test = unpack_mnist_data(os.path.join(dataset_path, 'test-labels.gz'), True)
 
return X_train.reshape(-1,28,28,1), y_train, X_test.reshape(-1,28,28,1), y_test