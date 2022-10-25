from app.calculator import *
from app.calculator_form import *
import unittest



class TestCalculator(unittest.TestCase):

    # you may create more test methods
    # you may add parameters to test methods
    # this is an example

        def test_cost_calculation_isPeak_isHoliday(self):
            self.calculator = Calculator()
            self.assertEqual(2.475, self.calculator.cost_calculation(10, 100, 50, True, True, configuration1))

        def test_cost_calculation_isPeak_noHoliday(self):
            self.calculator = Calculator()
            self.assertEqual(2.25, self.calculator.cost_calculation(10, 100, 50, True, False, configuration1))

        def test_cost_calculation_noPeak_isHoliday(self):
            self.calculator = Calculator()
            self.assertEqual(1.2375, self.calculator.cost_calculation(10, 100, 50, False, True, configuration1))

        def test_cost_calculation_noPeak_noHoliday(self):
            self.calculator = Calculator()
            self.assertEqual(1.125, self.calculator.cost_calculation(10, 100, 50, False, False, configuration1))

        def test_time_calculation(self):
            self.calculator = Calculator()
            self.assertEqual(900, self.calculator.time_calculation(20, 30, 300, configuration1))

        def test_is_Holiday(self):
            self.calculator = Calculator()
            self.assertTrue(True, self.calculator.is_holiday('26-1-2021'))

        def test_is_Holiday2(self):
            self.calculator = Calculator()
            self.assertFalse(False, self.calculator.is_holiday('27-1-2021'))

        def test_is_not_Holiday(self):
            self.calculator = Calculator()
            self.assertFalse(False, self.calculator.is_holiday('28-1-2021'))

        def test_is_not_Holiday2(self):
            self.calculator = Calculator()
            self.assertTrue(True, self.calculator.is_holiday('29-1-2021'))

        def test_location_ID(self):
            self.calculator = Calculator()
            self.assertEqual('70e5fe76-37e2-447f-b7e2-5cd81b721094', self.calculator.get_locationId('3186'))

        def test_is_peak(self):
            self.calculator = Calculator()
            self.assertTrue(True, self.calculator.is_peak('12:00'))

        def test_is_peak2(self):
            self.calculator = Calculator()
            self.assertFalse(False, self.calculator.is_peak('4:00'))


        def test_get_period(self):
            self.calculator = Calculator()
            self.assertEqual('12.5-12.5' , self.calculator.get_period('12:30'))

        def test_get_solar_energy_period(self):
            self.calculator = Calculator()
            self.assertEqual(0, self.calculator.get_solar_energy_period('3142', '2020-01-01'))

        def test_get_solar_energy_duration(self):
            #!!!!!!!!not sure!!!!!
            self.calculator = Calculator()
            self.assertEqual([[5, 0.016666666666666607], [7, 0.23636363636363633], [6, 1]]
                             ,calculator.get_solar_energy_duration('3142','2020-01-01'))

        def test_toHours(self):
            self.calculator = Calculator()
            self.assertAlmostEqual(6.58,calculator.toHour('6:35'),2)

        def test_get_sunrise_hour(self):
            self.calculator = Calculator()
            self.assertAlmostEqual(5.02,calculator.get_sunrise_hour('3142', '2020-01-01'),2)

        def test_get_sunset_hour(self):
            self.calculator = Calculator()
            self.assertAlmostEqual(19.77,calculator.get_sunset_hour('3142', '2020-01-01'),2)

        def test_get_day_light_length(self):
            self.calculator = Calculator()
            self.assertAlmostEqual(14.75,calculator.get_day_light_length('3142', '2020-01-01'),2)

        def test_get_solar_insolation(self):
            self.calculator = Calculator()
            self.assertEqual(8.8,calculator.get_solar_insolation('3142','2020-01-01'))

        def test_get_cloud_cover(self):
            self.calculator = Calculator()
            self.assertEqual(0, calculator.get_cloud_cover('3142','2020-01-01',1))

        def test_calculate_solar_energy(self):
            #!!!!!not sure about du!!!!!!!!!!
            self.calculator = Calculator()
            self.assertAlmostEqual(7.48, calculator.calculate_solar_energy(8.8,0.016666666666666607+0.23636363636363633+1,14.75,0),2)

class TestCaculatorForm(unittest.TestCase):

    def testFinal_Charge(self):

       self.calForm = Calculator_Form()
       self.assertEqual('Field data is none', self.calForm.validate_BatteryPackCapacity(None))

def main():

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

    unittest.TextTestRunner(verbosity=2).run(suite)

    #suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCaculatorForm)

    #unittest.TextTestRunner(verbosity=2).run(suite1)

main()


