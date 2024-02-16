from modules import atm

def describe_atm():
  def should_prevent_withdraw_lt_1():
    """🧪 expect the validation to return -1"""
    assert atm.validate(0) == -1  
  def should_prevent_withdraw_gt_1500():
    """🧪 expect the validation to return -1"""
    assert atm.validate(1501) == -1
    
  def should_provide_1_bankonote_500():
    """🧪 expect the validation to return 1"""
    assert atm.validate(500) == 1	
