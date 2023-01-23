import unittest
import validation as val


class Test(unittest.TestCase):
    """
    Verification of the user inputs test
    """
    def test_validate_email(self):
        self.assertTrue(val.vaidate_email_input('email@gmail.com'), True)

    def vaidate_wrong_email_input(self):
        self.assertEqual(val.vaidate_email_input('emailgmail.com'), None)

    def test_validate_data_input(self):
        self.assertTrue(val.validate_data('report'), True)
        self.assertTrue(val.validate_data('off'), True)

    def test_validate_wrong_data_input(self):
        self.assertFalse(val.validate_data('hello'), False)


if __name__ == '__main__':
    unittest.main()
