"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def count_people_by_city(file_path: pathlib.Path) -> dict:
    """Count the number of people from each city from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            people_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            city_counts_dictionary = {}
            # people is a list of dictionaries in the JSON file
            people_list: list = people_dictionary.get("people", [])
            for person_dictionary in people_list:  
                city = person_dictionary.get("city", "Unknown")
                city_counts_dictionary[city] = city_counts_dictionary.get(city, 0) + 1
            return city_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count people by city, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "users.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "json_people_by_city.txt")
    
    city_counts = count_people_by_city(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("People by City:\n")
        for city, count in city_counts.items():
            file.write(f"{city}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")