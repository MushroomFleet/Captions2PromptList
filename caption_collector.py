import os

def collect_captions():
    # Get the output filename from user
    output_filename = input("Enter the name for the output file (e.g., captions.txt): ")
    
    # Ensure the filename ends with .txt
    if not output_filename.endswith('.txt'):
        output_filename += '.txt'
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Initialize list to store first lines
    first_lines = []
    
    # Scan for text files and collect first lines
    for filename in os.listdir(current_dir):
        if filename.endswith('.txt') and filename != output_filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    first_line = file.readline().strip()
                    if first_line:  # Only add non-empty lines
                        first_lines.append(first_line)
            except Exception as e:
                print(f"Error reading {filename}: {str(e)}")
    
    # Write collected lines to output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in first_lines:
                output_file.write(line + '\n')
        print(f"\nSuccess! Collected {len(first_lines)} captions into {output_filename}")
    except Exception as e:
        print(f"Error writing to output file: {str(e)}")

if __name__ == "__main__":
    collect_captions()
