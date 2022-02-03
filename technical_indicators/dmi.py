from technical_indicators.atr import Atr

""" Directional Movement Indicators """


class Dmi:

    def __init__(self, original_data):
        self.data = original_data.copy()

    def __del__(self):
        self.data = []

    def get_positive_directional_index(self, look_back):
        calculated_atr = Atr(look_back, self.data).calculate_atr()
        positive_directional_movement = self.data.high.diff()
        positive_directional_movement[positive_directional_movement < 0] = 0
        positive_directional_index = 100 * (
                positive_directional_movement.ewm(alpha=1 / look_back).mean() / calculated_atr)
        return positive_directional_index

    def get_negative_directional_index(self, look_back):
        calculated_atr = Atr(look_back, self.data).calculate_atr()
        negative_directional_movement = self.data.low.diff()
        negative_directional_movement[negative_directional_movement > 0] = 0
        negative_directional_index = abs(
            100 * (negative_directional_movement.ewm(alpha=1 / look_back).mean() / calculated_atr))
        return negative_directional_index

    def calculate_dmi(self, look_back: int = 14):
        pdi = self.get_positive_directional_index(look_back)
        ndi = self.get_negative_directional_index(look_back)
        dmi = (abs(pdi - ndi) / abs(pdi + ndi)) * 100
        dmi = dmi.fillna(method='bfill')
        dmi = (dmi.shift(1)/50)-1
        return dmi
