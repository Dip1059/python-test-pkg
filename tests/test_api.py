import sys
import os
package_root_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
# adding root path to sys.path to find collpay package
sys.path.append(package_root_path)
#
import unittest
import collpay


class TestApi(unittest.TestCase):
    def setUp(self):
        self.collpay_obj = collpay.api.Collpay("xxxxxxxxxxxxxxxxx", collpay.ENV_SANDBOX)

    def test_env_production_will_be_1(self):
        self.assertEqual(collpay.ENV_PRODUCTION, 1)

    def test_env_sandbox_will_be_2(self):
        self.assertEqual(collpay.ENV_SANDBOX, 2)

    def test_getExchangeRate_basic_error(self):
        response = self.collpay_obj.get_exchange_rate('USD', 'BTC')
        self.assertEqual(response["success"], False)

    def test_createTransaction_basic_error(self):
        response = self.collpay_obj.create_transaction([])
        self.assertEqual(response["success"], False)

    def test_getTransaction_basic_error(self):
        response = self.collpay_obj.get_transaction('')
        self.assertEqual(response["success"], False)


if __name__ == "__main__":
    unittest.main()
