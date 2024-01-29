def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    
    d = x * x 
    e = d * a 
    f = b * x 

    return e + f + c
