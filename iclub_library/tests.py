from django.test import TestCase

# Create your tests here.
class TestTestCase(TestCase):
    def setUp(self):
    	print("setUp: Run once for every test method to set up clarn data.")
    	pass

    def test_false_is_false(self):
    	print("Method: test_false_is_false.")
    	self.assertFalse(False)

    def test_false_is_true(self):
    	print("Method: test_false_is_true.")
    	self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)