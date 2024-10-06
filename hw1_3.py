def celsius_to_fahrenheit(celsius):
    """
    將攝氏溫度轉換為華氏溫度
    :param celsius: 攝氏溫度
    :return: 華氏溫度
    """
    return celsius * 9/5 + 32

# 單元測試
import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # 測試攝氏0度轉換為華氏32度
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # 測試攝氏100度轉換為華氏212度
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        # 測試攝氏-40度轉換為華氏-40度
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
        # 測試攝氏37度轉換為華氏98.6度
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)

if __name__ == '__main__':
    unittest.main()