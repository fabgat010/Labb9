import unittest
from main import *

class TestSyntaxKoll(unittest.TestCase):
    #Testar olika fall som ska funka
    def testa_Na(self):
        self.assertEqual(Syntaxen("Na"), 'Formeln är syntaktiskt korrekt')
    def testing_H20(self):
        self.assertEqual(Syntaxen("H2O"), "Formeln är syntaktiskt korrekt")
    def testa_SiC3COOH24H2O7(self):
        self.assertEqual(Syntaxen("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
    def testa_Na332(self):
        self.assertEqual(Syntaxen("Na332"), 'Formeln är syntaktiskt korrekt')


    #Testar fall som inte ska funka
    def testa_fel_CXx45(self):
        self.assertEqual(Syntaxen("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
    def testa_fel_grup_COH4C(self):
        self.assertEqual(Syntaxen("C(OH4)C"), "Saknad siffra vid radslutet C")
    def testa_fel_COH4Cnr2(self):
        self.assertEqual(Syntaxen("C(OH4C"), "Saknad högerparentes vid radslutet ")
    def testa_fel_H20Fe(self):
        self.assertEqual(Syntaxen("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
    def testa_fel_H0(self):
        self.assertEqual(Syntaxen("H0"), 'För litet tal vid radslutet ') 
    def testa_fel_H1C(self):
        self.assertEqual(Syntaxen("H1C"), "För litet tal vid radslutet C")
    def testa_fel_H02C(self):
        self.assertEqual(Syntaxen("H02C"), "För litet tal vid radslutet 2C")
    def testa_fel_Nacl(self):
        self.assertEqual(Syntaxen("Nacl"), "Saknad stor bokstav vid radslutet cl")
    def testa_fel_a(self):
        self.assertEqual(Syntaxen("a"), "Saknad stor bokstav vid radslutet a")
    def testa_fel_Cl23(self):
        self.assertEqual(Syntaxen("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
    def testa_fel_paranteser(self):
        self.assertEqual(Syntaxen(")"), "Felaktig gruppstart vid radslutet )")
    def testa_fel_2(self):
        self.assertEqual(Syntaxen("2"), "Felaktig gruppstart vid radslutet 2")



if __name__ == '__main__':
    unittest.main()