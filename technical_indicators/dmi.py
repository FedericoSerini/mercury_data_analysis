from technical_indicators.atr import Atr

""" Directional Movement Indicators """


class Dmi:

    def __init__(self, look_back, original_data):
        self.look_back = look_back
        self.data = original_data.copy()
        self.calculated_atr = Atr(look_back, self.data).calculate_atr()

    def __del__(self):
        self.data = []

    def get_positive_directional_index(self):
        positive_directional_movement = self.data.high.diff()
        positive_directional_movement[positive_directional_movement < 0] = 0
        positive_directional_index = 100 * (
                positive_directional_movement.ewm(alpha=1 / self.look_back).mean() / self.calculated_atr)
        return positive_directional_index

    def get_negative_directional_index(self):
        negative_directional_movement = self.data.low.diff()
        negative_directional_movement[negative_directional_movement > 0] = 0
        negative_directional_index = abs(
            100 * (negative_directional_movement.ewm(alpha=1 / self.look_back).mean() / self.calculated_atr))
        return negative_directional_index

    def calculate_dmi(self):
        pdi = self.get_positive_directional_index()
        ndi = self.get_negative_directional_index()
        return (abs(pdi - ndi) / abs(pdi + ndi)) * 100
