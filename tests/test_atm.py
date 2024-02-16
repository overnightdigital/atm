from modules import atm

def describe_atm():
  def should_validate_below_threashold():
    """🧪 expect the validation to return -1"""
    assert atm.validate(0) == -1  	
