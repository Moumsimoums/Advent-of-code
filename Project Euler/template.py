from time import time
import unittest
a = time()
            
class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    print(f"The answer is {}")
    print(time()-a)

