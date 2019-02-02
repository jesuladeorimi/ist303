"""
Module 2: BCE 2.2: Team Exercise

Note: to make answers "readable" display of numbers is generally restricted 2 decimal places
and embedded in a sentence (string).
"""

#Task 1
#How many US dollars is 1,000,000 Venezuelan Bolivars worth given exchange rate of 1 Bolivar = US$0.016?
dollars_per_bolivar = 0.016
quantity_bolivars = 1000000
quantity_dollars = dollars_per_bolivar * quantity_bolivars
print ("{:,.0f}".format(quantity_bolivars), "Venezuelan Bolivars is the equivalent of US$"+"{:,.2f}".format(quantity_dollars))
#Output: "1,000,000 Venezuelan Bolivars is the equivalent of US$16,000.00"

#Task 2
#How many Bolivars you would need to have to live for the next 3 years if you require $12,060 (US) per year? 
annual_expend = 12060
years = 3
total_needed_us = annual_expend * years
total_needed_bolivars = total_needed_us / dollars_per_bolivar
print("Given US$"+"{:,.0f}".format(annual_expend), "per annum, living expenses for", years, "years is", \
      "{:,.0f}".format(total_needed_bolivars), "Bolivars.")
#Output: "Given US$12,060 per annum, living expenses for 3 years is 2,261,250 Bolivars."

#Task 3
#How many minutes are in the next 3 years if there are 365.2425 days in a year?
#How many Bolivars you would spend per minute, on average?
#Use both floating point division and integer division.
no_minutes = 365.2425 * 24 * 60 * no_years
no_bolivars_per_minute = total_req_bol / no_minutes
print("{:.2f}".format(no_bolivars_per_minute), "Bolivars per minute")
no_bolivars_per_minute_int = int(total_req_bol) // int(no_minutes)
print(no_bolivars_per_minute_int, "Bolivars per minute (int)")

#1.43 Bolivars per minute
#1 Bolivars per minute (int)

#Task 4 Answer
"""
Create the variable, bloody_vikings, containing the value 
‘Wonderful Spam! Glorious Spam!’.
"""
bloody_vikings = "Wonderful Spam! Glorious Spam!"

#Task 5 Answer
"""
Create a variable, viking_exclamations, containing a two-item 
list of the values of the two exclamations in bloody_vikings.
"""
viking_exclamations = bloody_vikings.split("! ")
print(viking_exclamations)

#['Wonderful Spam', 'Glorious Spam!']

#Task 6 Answer
"""
Create a variable, viking_exaggeration, containing the 
second value in the list assigned to viking_exclamations.
"""
viking_exaggeration = viking_exclamations[1]
print(viking_exaggeration)

#Glorious Spam!

#Task 7 Answer
"""
Create a variable, upper_exaggeration, containing the 
completely capitalized (not just the first letter) 
version of the contents of viking_exaggeration.
"""
upper_exaggeration = viking_exaggeration.upper()
print(upper_exaggeration)

#GLORIOUS SPAM!

#Task 7 Answer
"""
Create a variable, partial_exaggeration, containing the 
4th through 8th characters of the string assigned to 
viking_exaggeration.
"""
partial_exaggeration = viking_exaggeration[3:8]
print(viking_exaggeration)
print(partial_exaggeration)


