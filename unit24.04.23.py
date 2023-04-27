import unittest 

class User:
    def say_hello(self):
        return "Hello world"

class Admin:
    def say_hello(self):
        return "Hello world"
    
    def mend_something(self):
        return 0b01101101

class Developer:
    def say_hello(self):
        return "Hello world"
    
    def mend_something(self):
        return 0b01101101
    
    def write_code(self):
        return [0, 1, 0, 0, 1, 0]
    
#---------------------------------------------ll

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.admin = Admin()
        self.developer = Developer()

    def test_say_hello(self):
        self.assertIsInstance(self.user.say_hello(), str)
        self.assertIsInstance(self.admin.say_hello(), str)
        self.assertIsInstance(self.developer.say_hello(), str)

    def test_mend_something(self):
        self.assertIsInstance(self.admin.mend_something(), int)
        self.assertIsInstance(self.developer.mend_something(), int)

    def test_write_code(self):
        self.assertIsInstance(self.developer.write_code(), list)
        for item in self.developer.write_code():
            self.assertIsInstance(item, int)

if __name__ == '__main__':
    unittest.main()

abooba = 'booba'