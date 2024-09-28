# G10L CPC Classification Expanded Definitions

This project processes the G10L CPC (Cooperative Patent Classification) hierarchy, converts it from XML to JSON format, and generates expanded definitions for each category using the Claude AI model.

## Description

This project consists of two main components:
1. An XML to JSON converter for the G10L CPC hierarchy using Python's built-in xml.etree.ElementTree module
2. A script that processes the JSON hierarchy and adds expanded definitions to each category using the Claude AI model

The system traverses the entire hierarchy, from main groups to the deepest subgroups, and appends an 'expanded_definition' field to each category in the JSON structure.

## Requirements

- Python 3.7+
- Anthropic API key

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/g10l-cpc-expanded-definitions.git
cd g10l-cpc-expanded-definitions

2. Install the required packages:
pip install -r requirements.txt

3. Set up your Anthropic API key as an environment variable:
export ANTHROPIC_API_KEY='your-api-key-here'


## Usage

1. First, convert the XML hierarchy to JSON:
python xml_to_json_converter.py 
input_hierarchy.xml 
g10l_hierarchy.json

This will create a `g10l_hierarchy.json` file from your input XML.

2. Then, run the expansion script:
python expand_definitions.py

This will process the hierarchy and save the expanded version as `g10l_hierarchy_expanded.json`.



## Script Descriptions

### xml_to_json_converter.py

This script converts the G10L CPC hierarchy from XML format to JSON. It uses Python's built-in `xml.etree.ElementTree` module to parse the XML and then processes the resulting structure to create a more usable JSON structure.

Usage:
python xml_to_json_converter.py 
<input_xml_file> 
<output_json_file>

### expand_definitions.py

This script reads the JSON hierarchy, uses the Claude AI model to generate expanded definitions for each category, and then saves the result back to a JSON file.

Usage:
python expand_definitions.py

## Note

Processing the entire hierarchy may take a considerable amount of time and API calls, depending on its size. Please be patient and ensure you have sufficient API quota.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)