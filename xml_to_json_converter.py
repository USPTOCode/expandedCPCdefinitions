import xml.etree.ElementTree as ET
import json
import sys

def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(xml_to_dict(child))
    return result

def process_hierarchy(data):
    if isinstance(data, dict):
        if 'symbol' in data and 'title' in data:
            return {
                'symbol': data['symbol'],
                'title': data['title'],
                'children': [process_hierarchy(child) for child in data.get('children', [])]
            }
        else:
            return process_hierarchy(next(iter(data.values())))
    elif isinstance(data, list):
        return [process_hierarchy(item) for item in data]
    else:
        return data

def convert_xml_to_json(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    data = xml_to_dict(root)
    processed_data = process_hierarchy(data)
    
    with open(output_file, 'w') as f:
        json.dump(processed_data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xml_to_json_converter.py <input_xml_file> <output_json_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_xml_to_json(input_file, output_file)
    print(f"Conversion complete. JSON saved to {output_file}")