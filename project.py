import sys
import os
import json
import yaml
import xmltodict

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
        
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.json':
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON syntax in {file_path}:\n{e}")
    elif ext in ['.yml', '.yaml']:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML syntax in {file_path}:\n{e}")
    elif ext == '.xml':
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = xmltodict.parse(f.read())
                return data
        except Exception as e:
            raise ValueError(f"Invalid XML syntax in {file_path}:\n{e}")
    else:
        raise ValueError(f"Unsupported input format: {ext}")

def save_data(file_path, data):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.json':
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to write JSON to {file_path}:\n{e}")
    elif ext in ['.yml', '.yaml']:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        except Exception as e:
            raise RuntimeError(f"Failed to write YAML to {file_path}:\n{e}")
    elif ext == '.xml':
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(xmltodict.unparse(data, pretty=True))
        except Exception as e:
            raise RuntimeError(f"Failed to write XML to {file_path}:\n{e}")
    else:
        raise ValueError(f"Unsupported output format: {ext}")

def main():
    if len(sys.argv) == 1:
        try:
            import ui
            ui.run_ui()
        except ImportError:
            print("UI module not found.")
            sys.exit(1)
        return

    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    
    try:
        data = load_data(input_file)
        save_data(output_file, data)
        print(f"Successfully converted data from {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
