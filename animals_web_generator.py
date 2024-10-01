import data_fetcher

def generate_website(animals_data, animal_name):
    # Your existing code to generate the website
    pass

def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_animal_data(animal_name)
    generate_website(animals_data, animal_name)

if __name__ == "__main__":
    main()
youtube