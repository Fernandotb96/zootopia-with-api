import json


def load_data(file_path):
    """ Loads the animals data from the JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """ Serializes the animal's info into an HTML <li> block."""
    scientific_name = animal["taxonomy"].get("scientific_name", None)
    animal_class = animal["taxonomy"].get("class", None)
    diet = animal["characteristics"].get("diet", None)
    animal_type = animal["characteristics"].get("type", None)
    locations_list = animal.get("locations", [])
    location = locations_list[0] if locations_list else "Unknown"
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
    animals_data = load_data('animals_data.json')
    animals_html_text = animals_to_html(animals_data)
    new_html_text = replace_text_html("animals_template.html", animals_html_text)
    save_text_to_html(new_html_text)


if __name__ == "__main__":
    main()
