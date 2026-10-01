import unittest


if __name__ == '__main__':
    from test_main import TestMain
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
