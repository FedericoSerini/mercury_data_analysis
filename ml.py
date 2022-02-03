import numpy as np
import pandas as pd
import tensorflow.keras as keras
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Sequential


def train_cnn(training_df, test_datafr, parameters):
    """Trains and evaluates CNN on the given train and test data, respectively."""

    print("Training is starting ...")
    train_images = training_df.iloc[:, 2:].values
    train_labels = training_df.iloc[:, 0]
    train_prices = training_df.iloc[:, 1]

    test_images = test_datafr.iloc[:, 2:].values
    test_label = test_datafr.iloc[:, 0]
    test_price = test_datafr.iloc[:, 1]

    test_label = keras.utils.to_categorical(test_label, parameters["num_classes"])
    train_labels = keras.utils.to_categorical(train_labels, parameters["num_classes"])

    train_images = train_images.reshape(train_images.shape[0], parameters["input_w"], parameters["input_h"], 1)
    test_images = test_images.reshape(test_images.shape[0], parameters["input_w"], parameters["input_h"], 1)

    # CNN model
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(parameters["input_w"], parameters["input_h"], 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(parameters["num_classes"], activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy', 'mae', 'mse'])

    # metrics.accuracy_score, metrics.recall_score, metrics.average_precision_score, metrics.confusion_matrix
    train_data_size = train_images.shape[0]
    test_data_size = test_images.shape[0]

    print("model will be trained with {} and be tested with {} sample".format(train_data_size, test_data_size))
    # fit the model to the training data
    print("Fitting model to the training data...")
    print("")
    model.fit(train_images, train_labels, batch_size=parameters["batch_size"], epochs=parameters["epochs"], verbose=1,
              validation_data=None)

    prediction = model.predict(test_images, batch_size=parameters["batch_size"], verbose=1)
    print(model.evaluate(test_images, test_label, batch_size=parameters["batch_size"], verbose=1))

    print("Train conf matrix: ", confusion_matrix(np.array(reverse_one_hot(train_labels)),
                                                  np.array(reverse_one_hot(model.predict(train_images, batch_size=
                                                  parameters["batch_size"], verbose=1)))))

    print("Test conf matrix: ",  confusion_matrix(np.array(reverse_one_hot(test_label)),
                                                  np.array(reverse_one_hot(prediction))))

    model.save("my_model.h5")
    return prediction, test_label, test_price


def reverse_one_hot(prediction):
    reversed_x = []
    for x in prediction:
        reversed_x.append(np.argmax(np.array(x)))
    return reversed_x


df = pd.read_csv("./data/res.csv", header=None, index_col=None, delimiter=',')

train_df, test_df = train_test_split(df, test_size=0.20)



# drop nan values
train_df = train_df.dropna(axis=0)
test_df = test_df.dropna(axis=0)

# drop first 15 row
train_df = train_df.iloc[15:, :]
test_df = test_df.iloc[15:, :]

l0_train = train_df.loc[train_df[0] == 0]
l1_train = train_df.loc[train_df[0] == 1]
l2_train = train_df.loc[train_df[0] == 2]
l0_size = l0_train.shape[0]
l1_size = l1_train.shape[0]
l2_size = l2_train.shape[0]

l0_l1_ratio = (l0_size//l1_size)
l0_l2_ratio = (l0_size//l2_size)
print("Before")
print("l0_size:", l0_size, "l1_size:", l1_size, "l2_size:", l2_size)
print("l0_l1_ratio:", l0_l1_ratio, "l0_l2_ratio:", l0_l2_ratio)

l1_new = pd.DataFrame()
l2_new = pd.DataFrame()
for idx, row in train_df.iterrows():
    if row[0] == 1:
        for i in range(l0_l1_ratio):
            l1_new = l1_new.append(row)
    if row[0] == 2:
        for i in range(l0_l2_ratio):
            l2_new = l2_new.append(row)

train_df = train_df.append(l1_new)
train_df = train_df.append(l2_new)

# shuffle
train_df = shuffle(train_df)

########################################################
l0_train = train_df.loc[train_df[0] == 0]
l1_train = train_df.loc[train_df[0] == 1]
l2_train = train_df.loc[train_df[0] == 2]
l0_size = l0_train.shape[0]
l1_size = l1_train.shape[0]
l2_size = l2_train.shape[0]


l0_l1_ratio = (l0_size//l1_size)
l0_l2_ratio = (l0_size//l2_size)
print("After")
print("l0_size:", l0_size, "l1_size:", l1_size, "l2_size:", l2_size)
print("l0_l1_ratio:", l0_l1_ratio, "l0_l2_ratio:", l0_l2_ratio)


######################################################


train_df.reset_index(drop=True, inplace=True)
test_df.reset_index(drop=True, inplace=True)

print("train_df size: ", train_df.shape)

# fill params dict before call train_cnn
params = {"input_w": 15, "input_h": 15, "num_classes": 3, "batch_size": 1, "epochs": 5}

predictions, test_labels, test_prices = train_cnn(train_df, test_df, params)

result_df = pd.DataFrame({"prediction": np.argmax(predictions, axis=1),
                          "test_label": np.argmax(test_labels, axis=1),
                         "test_price": test_prices})

result_df.to_csv("./data/cnn_result.csv", sep=';', index=None)