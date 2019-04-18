
from SI507project_tools import *
import types
import unittest

data_call_obj = call_mostpopular_video()
list = []

class Test_stuff(unittest.TestCase):
    def setup(self):
        self.object = data_call_obj

# Test 1: Check data was called
    def test_datatype(self):
        self.assertTrue(type(self.object), list)

if __name__ == '__main__':
    unittest.main()
    #
    #
    # if type(data_call_obj) is type(list):
    #     pass
    # else:
    #     print("Error: Video information is not fetched")

# Test 2:
# what = DB_setup()
# print(Vidoe_class())

suite = unittest.TestSuite()
# suite.addTest(Introduction('test_case1'))
print(suite)
unittest.TextTestRunner().run(suite)

# if isinstance(DB,  ):
#     pass
# else:
#     print("Error: Video information is not fetched")
