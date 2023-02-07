import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    
    # Set up Function 
    def setUp(self):
        self.emp_1 = Employee("Baby", "Panda", 50000)
        self.emp_2 = Employee("Unlimited", "Wanda", 60000)

    # Tear Down Function
    def tearDown(self) -> None:
        pass

    def test_email(self):
       # I assert whether the name returned by the emai is equal to the second string
        self.assertEqual(self.emp_1.email, 'Baby.Panda@gmail.com')
        self.assertEqual(self.emp_2.email, 'Unlimited.Wanda@gmail.com')

        # I change their first names to run another test case
        self.emp_1.first = "John"
        self.emp_2.first = "Lisa"

        # I assert
        self.assertEqual(self.emp_1.email, 'John.Panda@gmail.com')
        self.assertEqual(self.emp_2.email, 'Lisa.Wanda@gmail.com')

    def test_fullname(self):
        # Assert 
        self.assertEqual(self.emp_1.fullname, 'Baby Panda')
        self.assertEqual(self.emp_2.fullname, 'Unlimited Wanda')

        # Second Test Case
        self.emp_1.first = "John"
        self.emp_2.first = "Lisa"

        # Assert
        self.assertEqual(self.emp_1.fullname, 'John Panda')
        self.assertEqual(self.emp_2.fullname, 'Lisa Wanda')

    def test_apply_raise(self):
        # Call the method to apply a raise
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        # Assert
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # We define a function to test the monthly schedule 
    def test_monthly_schedule(self):
        # Using path, we can can mock the employee.requests.get method assing the mock to a variable mocked_get
        with patch('employee.requests.get') as mocked_get:
            
            # using mocked_get, you can set the return value of ok to True
            # And this 'ok' is the response you expect to received as defined in the 
            # employer class
            mocked_get.return_value.ok = True
            
            # using mocked_get you can mock the return value of text as success since this is what you expect 
            # When the response is true
            mocked_get.return_value.text = 'Success'

            # Here, we calll the monthly_schedule method on employer one an store the schedule in a schedule 
            # object. the schedule we want is the schedule for the month of may
            schedule = self.emp_1.monthly_schedule('May')

            # We can assert that the method was called with the correct url
            mocked_get.assert_called_with('http://company.com/Panda/May')

            # Then you assert if the value stored in schedule is success
            self.assertEqual(schedule, 'Success')

            # #############

            # Tesing A False Response, I just negate the true response. The code should return Bad Response
            # So I check if, when the ok value is false, whether we really return the string Bad Response
            
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('January')
            mocked_get.assert_called_with('http://company.com/Wanda/January')

            self.assertAlmostEqual(schedule, "Bad Response!")

if __name__ == '__main__':
    unittest.main()

