# print("Hello World")


counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':

    print(counties[1])
# It worked

# Testing membership and logical operators

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
# It worked

# Exercie 2

#AND
if "Arapahoe" and "El Paso" in counties:
    print("Both counties are in the list.")
else:
    print("Both counties are not in the list.")

# OR
if "Arapahoe" or "El Paso" in counties:
    print("One or both of them are in the list of counties.")
else:
    print("One or both of them are not in the list of counties.")

#NOT IN
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")



# Exercise with For Loops

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

for i in range(3):
    print(i)


# Iterate Through a Dictionary

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Get the Keys of a Dictionary
for county in counties_dict:
    print(county)

# Using the keys() method to print the keys

for county in counties_dict.keys():
    print(county)

# Get the values using the values() method

for voters in counties_dict.values():
    print(voters)


#  Using format dictionary_name[key] to get the value for the key

for county in counties_dict:
    print(counties_dict[county])


# Using the get() method to get the value

for county in counties_dict:
    print(counties_dict.get(county))


#Get the key-value pairs of a dictionary

for county, voters in counties_dict.items():
    print(county, voters)

#Skill Drill
#for county, voters in counties_dict.items():
    #print(str(county) + " county has", str(voters) + " registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county_dict in voting_data:
    print(county_dict['registered_voters'])


# F-Strings

#Original Code
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#using f-strings

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {(my_votes / total_votes) * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# Multiline

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {(candidate_votes / total_votes) * 100:.2f}% of the total votes.")

print(message_to_candidate)


#Skill Drill

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#Skill Drill
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

