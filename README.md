# Zootopia with API

This project is a dynamic web generator that fetches real-time animal data from an external API, processes the information safely, and generates an interactive HTML page using a template.

## Installation

To install this project, simply clone the repository and install the dependencies in requirements.txt using `pip`:

```bash
pip install -r requirements.txt
```

Additionally, you need to set up your environment variables:

1. Create a `.env` file in the root directory of the project.
2. Add your API key from API Ninjas:
   ```env
   API_KEY=your_api_key_here
   ```

## Usage

To use this project, run the following command:

```bash
python animals_web_generator.py
```

The program will prompt you to enter the name of an animal. After fetching the data, it will ask for a filename to save and generate your new website.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request.