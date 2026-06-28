import sys
import os
import json

def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        sys.exit(1)
        
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.json':
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"Successfully read and verified {file_path}")
                return data
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON syntax in {file_path}:\n{e}")
            sys.exit(1)
    else:
        print(f"Error: Unsupported input format: {ext}")
        sys.exit(1)

def save_data(file_path, data):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.json':
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
                print(f"Successfully saved data to {file_path}")
        except Exception as e:
            print(f"Error: Failed to write JSON to {file_path}:\n{e}")
            sys.exit(1)
    else:
        print(f"Error: Unsupported output format: {ext}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    
    data = load_data(input_file)
    save_data(output_file, data)

if __name__ == "__main__":
    main()
