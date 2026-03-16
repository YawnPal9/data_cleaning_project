import tensorflow as tf
import pandas as pd
import numpy as np

pd.options.display.max_columns = None

print(tf.__version__)

import pygame
pygame.init()
print("Pygame ready")
#######################################################

#                   WORLD CITIES    

#######################################################                  
csv_path = "/Users/dayanahfranklin/python/datasets/world_cities/worldcities.csv"

# Read dataset
df = pd.read_csv(csv_path)

# Clean Column Names 
df.columns = df.columns.str.strip().str.lower()

# Show BEFORE cleaning 

print("\n--- BEFORE DROPPING COLUMNS ---")
print(df.head())
print(df.columns)

#columns dropped
to_drop = ['city_ascii', 
           'lat',
           'lng',
           'id',
           'iso2',
           'iso3',
           'capital',
           ]

#rename column -- from admin_name to state
df.rename(columns={'admin_name':'state'}, inplace=True)
# Actually drop the columns
df.drop(columns=to_drop, inplace=True)

#clean characters
df.replace(r'\[.*?\]', '', regex=True, inplace=True)
# Removed slashes \ in console
df.replace(r'\n', '', regex=True, inplace=True)
# Remove extra spaces 
df.replace(r'\s+', ' ', regex=True, inplace=True)
#Clean name whitespaces, set to lowerspace
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Show AFTER cleaning
print("\n--- AFTER DROPPING COLUMNS ---")
print(df.columns)
print(df.head().to_string())

# Find all cities in the USA
usa_cities = df[df['country'] == 'United States']
# Reset index after filtering USA Cities, 0,1,2,3...
usa_cities.reset_index(drop=True, inplace=True)

print(usa_cities.head())

#######################################################

#                       MOVIES                          

#######################################################")
movies_path = "/Users/dayanahfranklin/python/datasets/movies.csv"
# Read dataset
movies_df = pd.read_csv(movies_path)

# Define existing columns 
existing_columns = movies_df.columns  # all columns in the DataFrame


# Clean Column Names: strip spaces, lowercase, underscores instead of spaces
movies_df.columns = movies_df.columns.str.strip().str.lower()

# Show BEFORE cleaning 
print("\n--- BEFORE DROPPING COLUMNS ---")
print("Columns:", movies_df.columns.tolist())
print(movies_df.head())


print("\n--- AFTER DROPPING COLUMNS ---")
# Set index
movies_df.drop_duplicates(subset='movies', inplace=True)

# Columns dropped 
to_drop = ['votes', 'gross']
movies_df.drop(columns=to_drop, inplace=True)

# Rename one line column
movies_df.rename(columns={'one-line':'description'}, inplace=True)

#           Cleaning Text Data                  
# Remove content in brackets, newlines, extra spaces
movies_df.replace(r'\[.*?\]', '', regex=True, inplace=True)
movies_df.replace(r'\n', '', regex=True, inplace=True)
movies_df.replace(r'\s+', ' ', regex=True, inplace=True)

# Clean column whitespaces, lower case, underscores
movies_df.columns = movies_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill missing values "NaN""
movies_df.fillna("Unknown", inplace=True)
# Sets 'movies'as index 
movies_df.set_index('movies', inplace=True)

# Keep only key columns for compact display

columns_to_keep = ['year', 'genre', 'rating', 'description', 'runtime']
movies_df = movies_df[[c for c in columns_to_keep if c in movies_df.columns]]

# ------------------------------
# Console display settings
# ------------------------------
existing_columns = movies_df.columns 
for idx, row in movies_df.head(10).iterrows():
    print(f"Movie: {idx}")
    for col in movies_df.columns:
        print(f"  {col:<12}: {row[col]}")  # 12 spaces for column names
    print("\n")  # blank line between rows


#######################################################

#                   Airbnb                    
#######################################################

airbnb_path = "/Users/dayanahfranklin/python/datasets/Airbnb_Open_Data.csv"
airbnb_df = pd.read_csv(airbnb_path)

pd.set_option('display.width', 120)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 30)

# Select useful columns to display
cols = ['name','host_name','neighbourhood_group','room_type','price','minimum_nights']

# Only keep columns that actually exist
existing_cols = [c for c in cols if c in airbnb_df.columns]


print("\n--- BEFORE DROPPING COLUMNS ---")
print("Columns:", airbnb_df.columns.tolist())
print(airbnb_df.head().to_string())

# Cleaning text data
airbnb_df.replace(r'\[.*?\]', '', regex=True, inplace=True)
airbnb_df.replace(r'\n', '', regex=True, inplace=True)
airbnb_df.replace(r'\s+', ' ', regex=True, inplace=True)

# Clean column names
airbnb_df.columns = airbnb_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill missing values
airbnb_df.fillna("Unknown", inplace=True)

# Drop columns
to_drop = ['license']
airbnb_df.drop(columns=to_drop, inplace=True, errors="ignore")

print("\n--- AFTER DROPPING COLUMNS ---")
print("Columns:", airbnb_df.columns.tolist())

# ------------------------------
# Console display settings
# ------------------------------
existing_columns = airbnb_df.columns 
for idx, row in airbnb_df.head(27).iterrows():
    print(f"Airbnb: {idx}")
    for col in airbnb_df.columns:
        print(f"  {col:<27}: {row[col]}")  # 12 spaces for column names
    print("\n")  # blank line between rows


#######################################################

#                   UNIVERSITY TOWNS                    
#######################################################
towns_path = "/Users/dayanahfranklin/python/datasets/university_towns.txt"

# Read file as raw text
with open(towns_path, "r") as f:
    lines = f.readlines()

# Parse into a clean dataframe
data = []
current_state = None 

for line in lines:
    line = line.strip()
    if not line:
        continue
    # State lines have no parentheses
    if "(" not in line:
        current_state = line.replace("[edit]", "").strip()
    else:
        town, university = line.split("(", 1)
        university = university.replace(")", "").strip()
        data.append({
            "State": current_state,
            "Town": town.strip(),
            "University": university
        })

# Create dataframe
towns_df = pd.DataFrame(data)

#######################################################
# CLEAN DATA
#######################################################

# Remove wikipedia reference tags like [1] [2]
towns_df.replace(r'\[.*?\]', '', regex=True, inplace=True)

# Remove extra whitespace
towns_df = towns_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Define function to tidy text
def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

# Apply cleaning to all columns
towns_df[['State','Town','University']] = towns_df[['State','Town','University']].applymap(get_citystate)

# Reset index and set lesson-style Identifier
towns_df = towns_df.reset_index(drop=True)
towns_df.rename_axis('Identifier', inplace=True)
towns_df.index.name = 'Identifier'

#######################################################
# DISPLAY RESULTS CONSOLE-FRIENDLY
#######################################################

print("\n--- UNIVERSITY TOWNS CLEANED ---")
print("Indexes:", list(towns_df.index))

# Loop through all rows and print structured output like movies/airbnb examples
for idx, row in towns_df.iterrows():
    print(f"Town: {idx}")
    print(f"  State       : {row['State']}")
    print(f"  Town        : {row['Town']}")
    print(f"  University  : {row['University']}")
    print("\n")  # blank line between rows

# Show number of unique states
print("\nNumber of states found:", len(towns_df['State'].unique()))
print("States detected:", sorted(towns_df['State'].unique()))

#######################################################
# SAVE CLEANED DATA
#######################################################

towns_df.to_csv(
    "/Users/dayanahfranklin/python/datasets/university_towns_cleaned.csv",
    index=True
)