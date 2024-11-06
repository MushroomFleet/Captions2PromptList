# Caption Collector

A simple utility script to collect the first lines ("captions") from multiple text files in a folder and combine them into a single output file.

## Features

- Scans all text files in the current directory
- Collects the first line from each file
- Creates a new consolidated file with all captions
- Easy to use with included batch file
- Handles UTF-8 encoding
- Skips empty first lines

## Requirements

- Python 3.x

## Installation

1. Download all files to your target folder:
   - `caption_collector.py`
   - `run_collector.bat`

## Usage

### Method 1: Using the Batch File
1. Simply double-click `run_collector.bat`
2. Enter the desired output filename when prompted
3. The script will create a new text file containing all captions

### Method 2: Direct Python Execution
1. Open a terminal in the folder containing the script
2. Run: `python caption_collector.py`
3. Enter the desired output filename when prompted

## File Structure

```
your-folder/
├── caption_collector.py    # Main Python script
├── run_collector.bat      # Batch file for easy execution
└── README.md             # This file
```

## Notes

- The script will automatically add `.txt` extension if not provided
- The script skips the output file itself when scanning for text files
- Empty first lines are ignored
- Files are read using UTF-8 encoding

## Error Handling

The script includes basic error handling for:
- File reading errors
- File writing errors
- Invalid filenames

## Contributing

Feel free to submit issues and enhancement requests!

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
