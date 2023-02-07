"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

      location
      magnitude (magnitude greater than 6)
      longitude (4 decimal places)
      latitude (4 decimal places)

      new dictionary = 'eq_dict'

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

# print(f"Location: {EQ_Location}\nMagnitude: {EQ_Magnitude}\nLongitude: {EQ_Longitude:.4}\nLatitude: {EQ_Latitude:.4}")

"""
# import json library to use the json files
import json

# Load Earthquake data from eq_data.json
with open("eq_data.json") as eq_data_json:
    eq_data = json.load(eq_data_json)

# Create a variable EQ_count and give it the earthquake count value
EQ_count = eq_data["metadata"]["count"]

# Task 1: print out the number of earthquakes
print(
    f"\nThere are {EQ_count} earthquakes in the eq_data.json file as found in the metadata->count"
)

# Task 2: iterate through the dictionary and extract the location, magnitude,
#   longitude and latitude of the location and put it in a new
#   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#   magnitude > 6. Print out the new dictionary.

# Create a new dictionary called 'eq_dict'
eq_dict = {}

# Create magnitude limit
mag_limit = 6

# Create a for loop that will iterate through eq_data to get the earthquake information
for i, eq in enumerate(eq_data["features"]):
    if eq["properties"]["mag"] > mag_limit:
        eq_dict[i] = {
            "location": eq["properties"]["place"],
            "magnitude": eq["properties"]["mag"],
            "longitude": eq["geometry"]["coordinates"][0],
            "latitude": eq["geometry"]["coordinates"][1],
        }

# print eq_dict
print("\nThe new dictionary: eq_dict\n")
print(eq_dict)
print()

# Task 3: Using the eq_dict dictionary, print out the information as shown below
print("Below are the earthquakes with magnitudes greater than 6:\n")
for i, eq in eq_dict.items():
    print(
        f"Location: {eq['location']}\nMagnitude: {eq['magnitude']}\nLongitude: {eq['longitude']}\nLatitude: {eq['latitude']}\n"
    )
