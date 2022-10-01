import unittest

class TestTrans(unittest.TestCase):


    def setUp(self):
        self.sk, self.pk = account.generate_account()
        self.mnemonic_phrase = mnemonic.from_private_key(self.sk) 
        self.user = User(passphrase=self.mnemonic_phrase)
        self.balance = get_balance(self.pk)

    def test_id(self):
        self.assertEqual(self.user.id, self.sk)

    def test_public_key(self):
        self.assertEqual(self.user.public_key, self.pk)

    def test_get_balance(self):
        self.assertEqual(self.balance, 0)


if __name__ == '__main__':
    unittest.main()