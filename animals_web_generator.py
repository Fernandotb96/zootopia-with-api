import data_fetcher


def ask_animal():
    """Ask the user to enter an animal name and handle empty inputs."""
    while True:
        animal_user = input("Enter a name of an animal: ").strip()
        if not animal_user:
            print("Please enter a valid name.")
        else:
            return animal_user


def serialize_animal(animal):
    """Serialize an animal's data into an HTML list item block."""
    name = animal.get("name", "No data")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})
    locations_list = animal.get("locations", [])

    scientific_name = taxonomy.get("scientific_name", "No data")
    animal_class = taxonomy.get("class", "No data")
    diet = characteristics.get("diet", "No data")
    animal_type = characteristics.get("type", "No data")
    location = locations_list[0] if locations_list else "No data"

    output = f"""<li class="cards__item">
        <div class="card__title">{name}</div>
        <div class="card__text">
            <ul class="card__info_list">
                <li class="card__trait"><strong>Scientific name:</strong> {scientific_name}</li>
                <li class="card__trait"><strong>Animal class:</strong> {animal_class}</li>
                <li class='card__trait'><strong>Type:</strong> {animal_type}</li>
                <li class="card__trait"><strong>Diet:</strong> {diet}</li>
                <li class="card__trait"><strong>Location:</strong> {location}</li>
            </ul>
        </div></li>
        """
    return output


def animals_to_html(list_animals):
    """Transform a list of animal data into a single concatenated HTML string."""
    output = "\n".join(serialize_animal(animal) for animal in list_animals)
    return output


def replace_text_html(html_file, new_text):
    """Replace the placeholder in the template HTML file with the new HTML content."""
    with open(html_file, "r", encoding="utf-8") as handle:
        html_text = handle.read()
    html_text = html_text.replace("__REPLACE_ANIMALS_INFO__", new_text)
    return html_text


def save_text_to_html(html_text):
    """Ask the user for a filename and save the HTML content into it."""
    user_file_name = input("Enter name for the new file: ").strip()
    if not user_file_name.endswith(".html"):
        user_file_name += ".html"
    with open(user_file_name, "w", encoding="utf-8") as handle:
        handle.write(html_text)
    print(f"Website was successfully generated to the file '{user_file_name}'.")


def main():
    """Orchestrate the workflow to generate the Zootopia website.

    It prompts the user for an animal, fetches its data from the Animal API,
    and generates an HTML page with the animal data based on a template."""
    animal_choice = ask_animal()
    animals_data = data_fetcher.fetch_data(animal_choice)
    if not animals_data:
        animals_html_text = f"<h2>The animal '{animal_choice}' doesn't exist.</h2>"
    else:
        animals_html_text = animals_to_html(animals_data)
    new_html_text = replace_text_html("animals_template.html", animals_html_text)
    save_text_to_html(new_html_text)


if __name__ == "__main__":
    main()
