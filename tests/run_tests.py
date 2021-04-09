import unittest
from test_api import TestApi


def run_tests():
    test_classes_to_run = [TestApi]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    runner.run(big_suite)


if __name__ == '__main__':
    run_tests()
