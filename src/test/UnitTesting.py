import unittest
import util.Format

class FormatTimeMethods(unittest.TestCase):
	def test_dropZeros(self):
		self.assertEqual(dropZeros(5.4500),5.45)