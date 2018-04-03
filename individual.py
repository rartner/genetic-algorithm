from individual_bin import Individual_Bin
from individual_int import Individual_Int
from individual_real import Individual_Real
from individual_perm import Individual_Perm

class Individual():

    ''' Return the object according to the encoding '''
    def __new__(cls, size, encoding, min_bound, max_bound):
        if encoding == 'BIN':
            return Individual_Bin(size)
        elif encoding == 'INT':
            return Individual_Int(size, min_bound, max_bound)
        elif encoding == 'REAL':
            return Individual_Real(size, min_bound, max_bound)
        elif encoding == 'INT-PERM':
            return Individual_Perm(size)
        else:
            raise Exception('Invalid encoding')
