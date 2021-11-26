import unittest
from homeinsurance import HomeInsurance


class MyTestCase(unittest.TestCase):
    def test_get_house_years(self):  # test the method get_home_years() in Homeinsurance object
        # Behaviour Driven Development (BDD) example
        # Given - setup
        homeinsurance = HomeInsurance()
        homeinsurance.set_home_age("20")

        # When
        result = homeinsurance.get_house_years()

        # Then
        self.assertEqual(result, 2001)  # pass


if __name__ == '__main__':
    unittest.main()

