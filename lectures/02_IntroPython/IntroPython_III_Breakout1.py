def circle_prop(rad, calc='area'):
    """
    Calculate the area or circumference of a circle
    with a specified radius
    
    Input:
    ------
    
    rad : int or float
        radius of circle
        
    calc : str [default='area']
        what property to calculate
        options are area and circumference
        ['area', 'circ']
        
    Output:
    -------
    result : float
        area or circumference of circle
    """
    area = 3.14159 * rad**2
    circ = 2 * rad * 3.14159
    if calc == 'area':
        return area
    elif calc == 'circ':
        return circ
