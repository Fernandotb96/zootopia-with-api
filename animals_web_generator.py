import requests

URL_API = "https://api.api-ninjas.com/v1/animals"
API_KEY = 'qxnYeyzdqUCF16UH1BUTYugjvZvw9EmOAEo048O6'


def load_data():
    """ Ask user to enter the name of an animal and loads the data from the Animals API."""
    user_input = input("Introduce the name of the animal: ").strip()
    url = f"{URL_API}?name={user_input}"
    params = {"X-Api-Key": API_KEY}
    response = requests.get(url, params=params)
    animals_data = response.json()
    if len(animals_data) == 0:
        print(f"No animals found for {user_input}.")
    return animals_data


def serialize_animal(animal):
    """ Serializes the animal's info into an HTML <li> block."""
    scientific_name = animal["taxonomy"].get("scientific_name", "No data")
    animal_class = animal["taxonomy"].get("class", "No data")
    diet = animal["characteristics"].get("diet", "No data")
    animal_type = animal["characteristics"].get("type", "No data")
    locations_list = animal.get("locations", [])
    location = locations_list[0] if locations_list else "No data"
    output = f"""<li class="cards__item">
        <div class="card__title">{animal["name"]}</div>
        <div class="card__text">
            <ul class="card__info_list">
                <li class="card__trait"><strong>Scientific name:</strong> {scientific_name}</li>
                <li class="card__trait"><strong>Animal class:</strong> {animal_class}</li>
                <li class="card__trait"><strong>Diet:</strong> {diet}</li>
                <li class="card__trait"><strong>Location:</strong> {location}</li>
        """
    if animal_type:
        output += f"<li class='card__trait'><strong>Type:</strong> {animal_type}</li>"
    output += "</ul></div></li>"
    return output


def animals_to_html(list_animals):
    """Transform list of animals into a unique HTML string."""
    output = ""
    for animal in list_animals:
        output += serialize_animal(animal)
    return output


def replace_text_html(html_file, new_text):
    """Replace HTML text with new HTML animal's text and returns the new HTML string."""
    with open(html_file, "r") as handle:
        html_text = handle.read()
    html_text = html_text.replace("__REPLACE_ANIMALS_INFO__", new_text)
    return html_text


def save_text_to_html(html_text):
    """Ask user for filename and save new HTML text into it."""
    user_file_name = input("Enter new for the new file that ends in '.html' : ")
    if user_file_name[-5:] == ".html":
        with open(user_file_name, "w") as handle:
            handle.write(html_text)
        print("File saved successfully.")
    else:
        print("File not saved.")


def main():
    animals_data = load_data()
    animals_html_text = animals_to_html(animals_data)
    new_html_text = replace_text_html("animals_template.html", animals_html_text)
    if animals_data:
        save_text_to_html(new_html_text)


if __name__ == "__main__":
    main()
