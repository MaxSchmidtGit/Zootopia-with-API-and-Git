import os  # Importing the os module to work with environment variables
from dotenv import load_dotenv  # Importing load_dotenv to load .env variables into the environment
import data_fetcher  # Importing the custom data_fetcher module to retrieve animal data

# Load environment variables from a .env file
load_dotenv()

def serialize_animal(animal_obj):
    """
    Serialize a single animal object to HTML format.

    Args:
        animal_obj (dict): A dictionary containing details of a single animal.

    Returns:
        str: A string representing the HTML format of the animal's information.
    """
    output = '<li class="cards__item"><div class="card"><div class="card__content">'  # Initialize the HTML structure

    # Retrieve basic animal properties
    name = animal_obj.get("name")  # Extract the name of the animal
    characteristics = animal_obj.get("characteristics", {})  # Extract characteristics or use an empty dictionary
    locations = animal_obj.get("locations", [])  # Extract locations or use an empty list

    # Add the animal's name to the HTML content
    if name:
        output += f"<p><strong>Name:</strong> {name}</p>\n"

    # Iterate through characteristics and add them to the HTML content
    for key, value in characteristics.items():
        formatted_key = key.replace('_', ' ').title()  # Format the characteristic key
        output += f"<p><strong>{formatted_key}:</strong> {value}</p>\n"

    # Add the animal's first location to the HTML content if available
    if locations:
        output += f"<p><strong>Location:</strong> {locations[0]}</p>\n"

    # Close the HTML tags for the card and the list item
    output += '</div></div></li>\n'
    return output

def generate_animal_info(animals_data, animal_name):
    """
    Generate HTML formatted string for a list of animals based on the provided data.

    Args:
        animals_data (list): A list of dictionaries, where each dictionary contains details of an animal.
        animal_name (str): The name of the animal being queried.

    Returns:
        str: HTML formatted string with animal data or an error message if the animal does not exist.
    """
    # Check if there is any data to display; if not, show an error message
    if not animals_data:
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    # Serialize each animal in the list and concatenate them into a single HTML string
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    return output

def replace_placeholder(template_path, output_path, placeholder, replacement):
    """
    Replace a specific placeholder in the HTML template and save the modified content.

    Args:
        template_path (str): The file path to the template HTML file.
        output_path (str): The file path to save the modified HTML file.
        placeholder (str): The placeholder text to be replaced.
        replacement (str): The replacement text for the placeholder.

    Returns:
        None
    """
    # Open and read the HTML template file
    with open(template_path, "r") as template_file:
        template_content = template_file.read()  # Read the template file's content

    # Replace the placeholder with the given replacement content
    new_content = template_content.replace(placeholder, replacement)

    # Write the modified content to the output HTML file
    with open(output_path, "w") as output_file:
        output_file.write(new_content)

def main():
    """
    Main function to generate a webpage based on user-provided animal name.

    The function:
    1. Loads the API key from environment variables.
    2. Prompts the user to enter an animal name.
    3. Fetches the animal's data using the data_fetcher module.
    4. Generates an HTML file with the animal's information.
    5. Replaces the placeholder in the HTML template with the animal's details.
    """

    # Retrieve the API key from environment variables
    api_key = os.getenv('API_KEY')  # Get the API_KEY from environment variables

    # Check if the API key is available; if not, prompt the user to add it
    if not api_key:
        print("API key not found! Please add it to the .env file.")
        return

    # Prompt the user to enter an animal name
    animal_name = input("Please enter an animal: ").strip()

    # Fetch the animal's data using the data_fetcher module
    animals_data = data_fetcher.fetch_data(animal_name)

    # Generate a formatted HTML string based on the animal's data
    animal_info = generate_animal_info(animals_data, animal_name)

    # Replace the placeholder in the HTML template with the generated animal information
    replace_placeholder('animals_template.html', 'animals.html', '__REPLACE_ANIMALS_INFO__', animal_info)

    # Notify the user that the website has been generated
    print("Website was successfully generated to the file animals.html.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
