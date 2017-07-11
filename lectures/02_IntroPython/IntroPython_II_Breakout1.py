# parse hidden message
a = "T3j4hs92ij38sjsi_810i_2_sj1s_jj2a^@(_#JSh!JQiJD)dpw-d.1(e__FnJs3_jdamaa2eap2s234sjaws1(#a#*(g@#@easij9ja029dj9@"
print(a[:-12:4])

# dictionaries
cities = {"Berkeley" : "California", "Ann Arbor" : "Michigan", "Chicago" : "Illinois"}
states = {"Michigan" : "MI", "California" : "CA", "Illinois" : "IL"}
city_name = "Ann Arbor"
print("{} resides in {}".format(city_name, states[cities[city_name]]))

# String sets
str1 = "It is a wonderful day outside!"
str2 = "What terrible weather we are having!"
set1 = set(str1)
set2 = set(str2)

print("Union of set1 and set2 is {}".format(set1 & set2))




