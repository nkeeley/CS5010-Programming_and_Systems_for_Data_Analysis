# File: hw4_keeley.py
# CS 5010
# Homework 4: Testing and Debugging (Python version: 3)
# Nicholas Keeley, ngk3pf

## Import module to be tested and unit testing class.
import unittest
from homework2_keeley import ACCOUNT, CHECKING


## Define testing class.
class TestCheckingAccount(unittest.TestCase):

    
    ## ACCOUNT constructor test 1: pass the correct values?
    def test_ACCOUNTinit_did_initialize_balance (self):
        
        # Create sample.
        sample = ACCOUNT("1234", 500)
        test1 = sample.balance
        self.assertEqual(test1, 500)
    
    ## ACCOUNT constructor test 2: did create instance of right type?
    def test_ACCOUNTinit_did_create_right_instance (self):
        
        # Create sample.
        sample = ACCOUNT("1234", 500)
        self.assertIsInstance(sample, ACCOUNT)
    
    ## CHECKING constructor test 1: pass the correct values?
    def test_CHECKINGinit_did_initialize_balance (self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        self.assertEqual(sample.fee, 1.50)
    
     ## CHECKING constructor test 2: did create instance of right type?
    def test_CHECKINGinit_did_create_right_instance (self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        self.assertIsInstance(sample, CHECKING)

    ## CHECKING getFee test 1: did return the right fee after construction?
    def test_CHECKINGgetFee_did_return_fee(self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        test = sample.getFee()
        self.assertEqual(test, 1.50)
    
    ## CHECKING getFee test 2: is the fee of type float?
    def test_CHECKINGgetFee_is_float_type(self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        test = sample.getFee()
        self.assertIsInstance(test, float)
        
    ## Deposit test 1: does the balance add the deposit?
    def test_CHECKINGdeposit_does_addTo_balance(self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        sample.deposit(400)
        self.assertEqual(sample.balance, 900)
    
    ## Deposit test 2: does the method return None? This was a specification.
    def test_CHECKINGdeposit_does_return_none(self):
        
        # Create sample.
        sample = CHECKING("1234", 500, 1.50)
        test = sample.deposit(200)
        self.assertIsNone(test)
     
    ## Withdraw test 1: does the withdrawal also deduct a fee from balance?    
    def test_CHECKINGwithdraw_does_deduct_fee(self):
        
        #Create sample.
        sample = CHECKING("1234", 500, 1.50)
        sample.withdraw(100)
        self.assertEqual(sample.balance, 398.50)
    
    ## Withdraw test 2: does the withdrawal cancel if amount > balance?    
    def test_CHECKINGwithdraw_does_avoid_overdraw(self):
        
        #Create sample.
        sample = CHECKING("1234", 2, 1.50)
        sample.withdraw(3) # Actually a weird caveat found. If balance==amount, charges fee negative value.
        self.assertEqual(sample.balance, 2)   

if __name__=="__main__":
    unittest.main()

lst=["A", "E", "I"]
word = "ebe"

print("this is my sheet")


