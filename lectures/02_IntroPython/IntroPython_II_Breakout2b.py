# Breakout 2b

state2abbr = {
    'Michigan': 'MI',
    'Oregon' : 'OR',
    'Califonia' : 'CA',
    'Nevada' : 'NV' }

cities = {
    'Ann Arbor' : 'MI',
    'Chicago' : 'IL',
    'Portland' : 'OR',
    'Berkeley' : 'CA',
    'San Francisco' : 'CA' }

# 1.
state2abbr['Illinois'] = 'IL'
state2abbr['Florida'] = 'FL'
state2abbr['Georgia'] = 'GA'
cities['Atlanta'] = 'GA'
cities['Miami'] = 'FL'
cities['Las Vegas'] = 'NV'

# 2.
abbr2state = dict(list(zip(state2abbr.values(), state2abbr.keys())))

# 3.
print("-" * 10)
for k in state2abbr.keys():
    print("%s has abbreviation %s" % (k, state2abbr[k]))

# 4. 
print("-" * 10)
for k in cities.keys():
    print("%s is in the state of %s" % (k, abbr2state[cities[k]]))
    
# 5. 
print('-'*10)
while True:
    question1 = input("Would you like to get a state abbr [a] or get the state of a city [c]? [a/c] ")
    
    if question1 != 'a' and question1 != 'c':
        print("please use a or c to respond...")
        continue
        
    elif question1 == 'a':
        question2 = input("Name a state you want an abbr for: ")
        response = state2abbr.get(question2, 'sorry dont have that!')
        print("The answer is: %s" % response)
        
    elif question1 == 'c':
        question2 = input("Name a city that you want to know which state it resides in: ")
        response = cities.get(question2, 'sorry dont have that!')
        print("The answer is: %s" % response)
        
    question3 = input("Would you like to coninue? [y/n] ")
    if question3 != 'y':
        break