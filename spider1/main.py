from bot import NewSpider as NewSpider
import unittest

class testScrapy(unittest.TestCase):
    def startScript(self):
        self.assertTrue(NewSpider)

if __name__ == '__main__':
    unittest.main()


