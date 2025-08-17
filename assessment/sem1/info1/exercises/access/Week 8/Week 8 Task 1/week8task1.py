
from unittest import TestCase
from week7task1function import fine_calculator


#i test che implemento devono iniziare tutti con la parola test all'inizio
class FineCalculatorTest(TestCase):
    # def test_1(self):
    #     result=fine_calculator('area',30)
    #     self.assertEqual(result, None)
    #     self.assertRaises(ValueError, fine_calculator.divide,10,0) #es per prevenire il zero division error
    #     with self.assertRaises(ValueError):   #si può fare anche cosi
    #         fine_calculator.divide(10,0) 
    def test_speed_types(self):
        actual=fine_calculator('motorway','c')
        expected='Invalid Speed Type'
        self.assertEqual(actual,expected)
        actual2=fine_calculator('motorway',[50])
        expected2='Invalid Speed Type'
        self.assertEqual(actual2,expected2)
        actual3=fine_calculator('motorway',0j)
        expected3='Invalid Speed Type'
        self.assertEqual(actual3,expected3)
        actual4=fine_calculator('motorway',{50})
        expected4='Invalid Speed Type'
        self.assertEqual(actual4,expected4)
        actual5=fine_calculator('motorway',(50,))
        expected5='Invalid Speed Type'
        self.assertEqual(actual5,expected5)
        actual6=fine_calculator('motorway','')
        expected6='Invalid Speed Type'
        self.assertEqual(actual6,expected6)
    def test_speed_values(self):
        actual=fine_calculator('motorway',-2)
        expected='Invalid Speed Value'
        self.assertEqual(actual,expected)
        actual2=fine_calculator('motorway',-1.5)
        expected2='Invalid Speed Value'
        self.assertEqual(actual2,expected2)

        

    def test_area_types(self):
        actual=fine_calculator(2,80)
        expected='Invalid Area Type'
        self.assertEqual(actual,expected)
        actual2=fine_calculator(['area'],50)
        expected2='Invalid Area Type'
        self.assertEqual(actual2,expected2)
        actual4=fine_calculator(0j,50)
        expected4='Invalid Area Type'
        self.assertEqual(actual4,expected4)
        actual5=fine_calculator({'area'},50)
        expected5='Invalid Area Type'
        self.assertEqual(actual5,expected5)
        actual6=fine_calculator(('area',),50)
        expected6='Invalid Area Type'
        self.assertEqual(actual6,expected6)
        actual7=fine_calculator(5.8,50)
        expected7='Invalid Area Type'
        self.assertEqual(actual7,expected7)

    def test_area_value(self):
        actual=fine_calculator('cacca',50)
        expected='Invalid Area Value'
        self.assertEqual(actual,expected)
        actual2=fine_calculator('Urban',50)
        expected2='Invalid Area Value'
        self.assertEqual(actual2,expected2)
        actual3=fine_calculator('Motorway',50)
        expected3='Invalid Area Value'
        self.assertEqual(actual3,expected3)
        actual4=fine_calculator('Expressway',50)
        expected4='Invalid Area Value'
        self.assertEqual(actual4,expected4)
        actual5=fine_calculator('',50)
        expected5='Invalid Area Value'
        self.assertEqual(actual5,expected5)

    def test_speed_limit(self):
        actual=fine_calculator('expressway',99)
        expected=0
        self.assertEqual(actual,expected)
        actual2=fine_calculator('urban',40)
        expected2=0
        self.assertEqual(actual2,expected2)
        actual3=fine_calculator('motorway',110)
        expected3=0
        self.assertEqual(actual3,expected3)

    def test_working(self):
        actual=fine_calculator('motorway',180)
        expected=round(0.5*50**2)
        self.assertEqual(actual,expected,0) 
        actual4=fine_calculator('urban',60)
        expected4=round(1*20**2)
        self.assertEqual(actual4,expected4,0)
        actual7=fine_calculator('expressway',95)
        expected7=0
        self.assertEqual(actual7,expected7)
        actual8=fine_calculator('expressway',110)
        expected8=round(0.8*10**2)
        self.assertEqual(actual8,expected8,0)
    def test_fine(self):
        actual=fine_calculator('expressway',118)
        self.assertIsInstance(actual,int)


