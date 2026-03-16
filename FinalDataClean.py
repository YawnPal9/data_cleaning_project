import tensorflow as tf
import pandas as pd
import numpy as np
# Project finished 3/16/26 @5:17am
pd.options.display.max_columns = None

print(tf.__version__)

import pygame
pygame.init()
print("Pygame ready")

#######################################################
#                   WORLD CITIES    
#######################################################                  
csv_path = "data/world_cities/worldcities.csv"

# Read dataset
df = pd.read_csv(csv_path)

# Clean Column Names 
df.columns = df.columns.str.strip().str.lower()

# Show BEFORE cleaning 
print("\n--- BEFORE DROPPING COLUMNS ---")
print(df.head())
print(df.columns)

# Columns to drop
to_drop = ['city_ascii', 'lat', 'lng', 'id', 'iso2', 'iso3', 'capital']

# Rename column -- from admin_name to state
df.rename(columns={'admin_name':'state'}, inplace=True)
# Actually drop the columns
df.drop(columns=to_drop, inplace=True)

# Clean characters
df.replace(r'\[.*?\]', '', regex=True, inplace=True)
df.replace(r'\n', '', regex=True, inplace=True)
df.replace(r'\s+', ' ', regex=True, inplace=True)
# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Show AFTER cleaning
print("\n--- AFTER DROPPING COLUMNS ---")
print(df.columns)
print(df.head().to_string())

# Find all cities in the USA
usa_cities = df[df['country'] == 'United States']
usa_cities.reset_index(drop=True, inplace=True)

print(usa_cities.head())

#######################################################
#                       MOVIES                          
#######################################################
movies_path = "data/movies/movies.csv"
movies_df = pd.read_csv(movies_path)

# Clean column names
movies_df.columns = movies_df.columns.str.strip().str.lower()
print("\n--- BEFORE DROPPING COLUMNS ---")
print("Columns:", movies_df.columns.tolist())
print(movies_df.head())

# Drop duplicates & unwanted columns
movies_df.drop_duplicates(subset='movies', inplace=True)
to_drop = ['votes', 'gross']
movies_df.drop(columns=to_drop, inplace=True)
movies_df.rename(columns={'one-line':'description'}, inplace=True)

# Clean text data
movies_df.replace(r'\[.*?\]', '', regex=True, inplace=True)
movies_df.replace(r'\n', '', regex=True, inplace=True)
movies_df.replace(r'\s+', ' ', regex=True, inplace=True)
movies_df.columns = movies_df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill missing values
movies_df.fillna("Unknown", inplace=True)
movies_df.set_index('movies', inplace=True)

# Keep only key columns
columns_to_keep = ['year', 'genre', 'rating', 'description', 'runtime']
movies_df = movies_df[[c for c in columns_to_keep if c in movies_df.columns]]

# Display first 10 movies
for idx, row in movies_df.head(10).iterrows():
    print(f"Movie: {idx}")
    for col in movies_df.columns:
        print(f"  {col:<12}: {row[col]}")
    print("\n")

#######################################################
#                   AIRBNB                    
#######################################################
airbnb_path = "data/airbnb/Airbnb_Open_Data.csv"
airbnb_df = pd.read_csv(airbnb_path)

pd.set_option('display.width', 120)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 30)

cols = ['name','host_name','neighbourhood_group','room_type','price','minimum_nights']
existing_cols = [c for c in cols if c in airbnb_df.columns]

print("\n--- BEFORE DROPPING COLUMNS ---")
print("Columns:", airbnb_df.columns.tolist())
print(airbnb_df.head().to_string())

# Clean text data
airbnb_df.replace(r'\[.*?\]', '', regex=True, inplace=True)
airbnb_df.replace(r'\n', '', regex=True, inplace=True)
airbnb_df.replace(r'\s+', ' ', regex=True, inplace=True)
airbnb_df.columns = airbnb_df.columns.str.strip().str.lower().str.replace(" ", "_")
airbnb_df.fillna("Unknown", inplace=True)

# Drop license column if exists
airbnb_df.drop(columns=['license'], inplace=True, errors="ignore")

print("\n--- AFTER DROPPING COLUMNS ---")
print("Columns:", airbnb_df.columns.tolist())

# Display first 27 rows
for idx, row in airbnb_df.head(27).iterrows():
    print(f"Airbnb: {idx}")
    for col in airbnb_df.columns:
        print(f"  {col:<27}: {row[col]}")
    print("\n")

#######################################################
#                   UNIVERSITY TOWNS                    
#######################################################
towns_path = "data/university_towns/university_towns.txt"

# Read file as raw text
with open(towns_path, "r") as f:
    lines = f.readlines()

data = []
current_state = None
for line in lines:
    line = line.strip()
    if not line:
        continue
    if "(" not in line:
        current_state = line.replace("[edit]", "").strip()
    else:
        town, university = line.split("(", 1)
        university = university.replace(")", "").strip()
        data.append({"State": current_state, "Town": town.strip(), "University": university})

towns_df = pd.DataFrame(data)

# Clean data
towns_df.replace(r'\[.*?\]', '', regex=True, inplace=True)
towns_df = towns_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

towns_df[['State','Town','University']] = towns_df[['State','Town','University']].applymap(get_citystate)
towns_df = towns_df.reset_index(drop=True)
towns_df.rename_axis('Identifier', inplace=True)
towns_df.index.name = 'Identifier'

# Display results
print("\n--- UNIVERSITY TOWNS CLEANED ---")
for idx, row in towns_df.iterrows():
    print(f"Town: {idx}")
    print(f"  State       : {row['State']}")
    print(f"  Town        : {row['Town']}")
    print(f"  University  : {row['University']}")
    print("\n")

print("\nNumber of states found:", len(towns_df['State'].unique()))
print("States detected:", sorted(towns_df['State'].unique()))

# Save cleaned data
towns_df.to_csv("data/university_towns/university_towns_cleaned.csv", index=True)