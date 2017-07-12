def convert(filename, csv2tab=True):
    """
    convert a tab or csv delimited file from one 
    type to the other or vice versa
    
    filename : str
        name of file to be converted
        
    csv2tab : bool [default=True]
        if False, convert from tab to csv
        if True, opposite
    """
    # Read file
    with open(filename, 'r') as f:
        lines = f.read()
        
    # Parse data
    lines = lines.strip()
    lines = lines.split('\n')
        
    if csv2tab == True:
        lines = list(map(lambda x: x.split(', '), lines))
        with open(filename[:-3]+'tab', 'w') as f:
            for i, l in enumerate(lines):
                f.write('\t'.join(l) + '\n')
                
    elif csv2tab == False:
        lines = list(map(lambda x: x.split('\t'), lines))
        with open(filename[:-3]+'csv', 'w') as f:
            for i, l in enumerate(lines):
                f.write(', '.join(l) + '\n')
            