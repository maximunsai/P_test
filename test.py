import unittest
import cap

class cap_text(unittest.TestCase):
    def one_text(self):
        text = "hello"
        result = cap.cap_text(text)
        self.assertEqual(result, "Hello")

    def multi_text(self):
        text= "hello world, i am human"
        result = cap.cap_text(text)
        self.assertEqual(result, "Hello World, I Am Human")


if __name__=='__main__':
    unittest.main()
