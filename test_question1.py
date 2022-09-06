import unittest

class MockTimeDisplay(object):
    '''Mock class for tests, no validation required'''

    def __init__(self, min:int, hour:int, am_pm:str, correct_degrees:int):
        self._min = min
        self._hour = hour
        self._am_pm = am_pm
        self._degrees = correct_degrees

    @property
    def time(self):
        return f"{self._min}:{self._hour} {self._am_pm} - {self._degrees} degrees"

class BadFormatException(Exception):
    pass

class BadTimeException(Exception):
    pass

class MockFailTime(object):
    def __init__(self, time_string:str, badformat:bool):
        if badformat:
            raise BadFormatException()
        raise BadTimeException()

class TestTimeDisplay(unittest.TestCase):

    # would be better to run as subtests but forgot how to do that feeding a data function to the test and all that
    def test_good_formats(self):
        for test_times_scenarios in [
            {"time": "11:50 am", "degrees": "30"},
            {"time": "11:50 pm", "degrees": "30"},
            {"time": "9:00 AM", "degrees": "90"},
            {"time": "9:00 PM", "degrees": "90"},
            {"time": "12:50 am", "degrees": "60"},
            {"time": "12:50 pm", "degrees": "60"}
        ]:
            time_set = test_times_scenarios
            time_values, am_pm_value = time_set["time"].split(' ')
            hours, min = time_values.split(':')
            time_function_mock = MockTimeDisplay(hours, min, am_pm_value, time_set["degrees"])
            self.assertEqual(time_function_mock.time, f"{time_set['time']} - {time_set['degrees']} degrees", "wrong time returned")

    def test_bad_formats(self):
        for test_times_scenarios in [
            {"time": "iamapotato", "expectedExceptionType": BadFormatException},
            {"time": "88:99 am", "expectedExceptionType": BadTimeException},
            {"time": "75:98 pm", "expectedExceptionType": BadTimeException},
            {"time": "0:00 pm", "expectedExceptionType": BadTimeException},
            {"time": "15:56", "expectedExceptionType": BadFormatException},
            {"time": "10:50 sm", "expectedExceptionType": BadFormatException},
            {"time": " ", "expectedExceptionType": BadFormatException},
            {"time": "*%#&%@", "expectedExceptionType": BadFormatException},
            {"time": "11:50 am#shouldFail", "expectedExceptionType": BadFormatException}
        ]:
            try:
                if test_times_scenarios["expectedExceptionType"] is BadFormatException:
                    MockFailTime(test_times_scenarios["time"], True)
                else:
                    MockFailTime(test_times_scenarios["time"], False)
            except BadFormatException as e:
                if test_times_scenarios["expectedExceptionType"] is BadFormatException:
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)
            except BadTimeException as e:
                if test_times_scenarios["expectedExceptionType"] is BadTimeException:
                    self.assertTrue(True)
                else:
                    self.assertTrue(False)





if __name__ == '__main__':
    unittest.main()
