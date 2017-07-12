import math

def pi_approx(Nterms):
    """
    This functiona approximates pi via the
    series of inverse squares
    
    Input:
    ------
    Nterms : int
        number of terms in the series to sum
        
    Output:
    -------
    tot : float
        approximation of pi
        
    err : float
        fractional error from true value in math module
    """
    squares = range(1, Nterms+1)
    terms = [1/float(i)**2 for i in squares]
    tot = math.sqrt(sum(terms)*6)
    err = (tot - math.pi)
    return tot, err
