from modules import atm

def describe_atm():
    def should_validate_true():
        """🧪 expect the validation to be true"""
        assert atm.validate() == True