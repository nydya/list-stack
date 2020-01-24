import stack
import unittest 


class Test(unittest.TestCase):
    s1 = stack.Stack()
    
    def test_empty(self):
        self.assertTrue(self.s1.empty)
    
    def test_add(self):
        self.s1.push('a')
        self.s1.push('b')
        self.s1.push('c')
        self.assertEqual(self.s1.stack, ['a','b','c'])
        
    def test_pop(self):
        self.assertEqual(self.s1.pop(), 'c')
    
    def test_top(self):
        self.assertEqual(self.s1.top(), 'b')
    
    def test_size(self):
        self.assertEqual(self.s1.size(), 2)
    



if __name__ == "__main": 
    unittest.main()