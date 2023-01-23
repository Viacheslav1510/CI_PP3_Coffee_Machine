import unittest
import validation as val


class Test(unittest.TestCase):
    """
    Verification of the user inputs test
    """
    def test_validate_email(self):
        self.assertTrue(val.validate_email_input('email@gmail.com'), True)

    def test_not_valid_email(self):
        self.assertEqual(val.validate_email_input('email'), None)

    def test_validate_data_input(self):
        self.assertTrue(val.validate_data('report'), True)
        self.assertTrue(val.validate_data('off'), True)

    def test_validate_wrong_data_input(self):
        self.assertFalse(val.validate_data('hello'), False)


if __name__ == '__main__':
    unittest.main()
