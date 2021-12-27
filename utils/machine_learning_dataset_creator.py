from logger.logger import Logger
import numpy as np
import pandas as pd


class MachineLearningDataset:

    def __init__(self, data, window_size):
        self.log = Logger(MachineLearningDataset.__name__).get_log()
        self.data = data.copy().dropna()
        self.look_back = window_size
        self.close_mean = data.close.mean()
        self.output = []
        self.relative_max_price = self.close_mean
        self.relative_min_price = self.close_mean
        self.relative_max_price_index = 0
        self.relative_min_price_index = 0
        self.begin_index = 0
        self.end_index = 0
        self.middle_index = 0

    def prepare_data_for_ml(self):
        self.log.info("Creating buy/sell labels")
        self.label_data_though_sliding_window(self.data.close)
        a = pd.DataFrame(index=self.data.index, data=self.output)
        a.rename(columns={0: 'label'}, inplace=True)
        self.log.info("Done!")
        return a

    def label_data_though_sliding_window(self, close_data):
        counter = 0

        while counter < len(close_data):
            # if counter > self.look_back:
            self.set_sliding_window_indexes(counter)

            for i in range(self.begin_index, self.end_index + 1):
                self.set_relative_min_max_and_indexes(close_data, i)

            self.establish_label()
            self.reset_min_max_values()

            counter += 1

    def set_sliding_window_indexes(self, counter):
        self.begin_index = counter - self.look_back
        self.end_index = self.begin_index + self.look_back - 1
        self.middle_index = (self.begin_index + self.end_index) // 2

    def set_relative_min_max_and_indexes(self, close_data, index):
        actual_price = close_data.iloc[index]

        if actual_price < self.relative_min_price:
            self.relative_min_price = actual_price
            self.relative_min_price_index = np.where(close_data == self.relative_min_price)[0][0]
        if actual_price > self.relative_max_price:
            self.relative_max_price = actual_price
            self.relative_max_price_index = np.where(close_data == self.relative_max_price)[0][0]

    def establish_label(self):
        if self.relative_max_price_index == self.middle_index:
            self.output.append(2)
        elif self.relative_min_price_index == self.middle_index:
            self.output.append(1)
        else:
            self.output.append(0)

    def reset_min_max_values(self):
        self.relative_min_price = self.close_mean
        self.relative_max_price = self.close_mean
