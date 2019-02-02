#Task 1 Answer
dollarPerBolivar = 0.016
bolivars= 1000000
result= dollarPerBolivar*bolivars
print (bolivars, 'bolivars =', "{:.2f}".format(result), 'dollars')

#1000000 bolivars = 16000.00 dollars

#Task 2 Answer
"""
Calculate how many Bolivars you would need to have today 
to live for the next 3 years if you require $12,060 (US) 
per year, and you keep the sum in cash under your mattress 
(instead of putting it in a bank to earn interest). 
Print this result out in a readable way.
"""
annual_expend = 12060
no_years = 3
total_req_us = annual_expend * no_years
total_req_bol = total_req_us / dollarPerBolivar
print("{:.2f}".format(total_req_bol), "Bolivars required")

#2261250.00

#Task 3 Answer
"""
Calculate how many minutes there will be in the next 3 years, 
if there are 365.2425 days in a year. Calculate how many 
Bolivars you would spend per minute, on average, based on the 
calculations here and in task 2 above. Do this using both 
floating point division and integer division. Print these 
calculated results out in readable ways.
"""

#Assumption: to make numbers "readable" we are restricting
#display to 2 decimal places
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


