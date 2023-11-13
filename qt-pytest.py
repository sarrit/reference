import unittest 
from unittest.mock import patch
import menu
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

class Test1(unittest.TestCase):

    def test_on_click(self):
        with patch('menu.MainWindow.clickMethod') as clickCheck:
            app = menu.MainWindow()
            QTest.mouseClick(app.pybutton1, Qt.LeftButton)
            self.assertTrue(clickCheck.called)
        
if __name__ == "__main__":
    unittest.main() 
