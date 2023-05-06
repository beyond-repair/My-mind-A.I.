import unittest

from test_main import TestMain


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    unittest.TextTestRunner(verbosity=2).run(suite)
