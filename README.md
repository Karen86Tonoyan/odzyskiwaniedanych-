# Odzyskiwanie Danych (Data Recovery)

An open-source data recovery tool for recovering deleted files from storage devices.

## Features

- 🔍 Scan storage devices for deleted files
- 📁 Support for common file types (images, documents, videos)
- 💾 Simple command-line interface
- 🔓 Open source and free to use
- 🚀 Lightweight and fast

## Installation

```bash
# Clone the repository
git clone https://github.com/Karen86Tonoyan/odzyskiwaniedanych-.git
cd odzyskiwaniedanych-

# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage

### Basic File Recovery

```bash
python recovery.py --scan /path/to/scan --output ./recovered_files
```

### Command Line Options

- `--scan PATH`: Path to scan for deleted files
- `--output PATH`: Directory to save recovered files (default: ./recovered_files)
- `--type TYPE`: File type to recover (e.g., jpg, pdf, txt) - recovers all by default
- `--help`: Show help message

## Supported File Types

- Images: JPG, PNG, GIF
- Documents: PDF
- Archives: ZIP

## How It Works

1. **Scanning**: The tool scans the specified directory or device for file signatures
2. **Detection**: Identifies deleted files by looking for file headers and footers
3. **Recovery**: Attempts to recover the file content and save it to the output directory

## Example

```bash
# Scan current directory for deleted JPG images
python recovery.py --scan . --type jpg

# Scan a specific folder and recover all file types
python recovery.py --scan /path/to/folder --output ./my_recovered_files
```

## Limitations

⚠️ **Important Notes:**
- Works best on non-overwritten data
- Recovery success depends on how recently files were deleted
- Does not guarantee 100% recovery
- For physical drive damage, professional tools may be needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided as-is for educational and recovery purposes. Always backup important data. The authors are not responsible for any data loss or damage.

## Support

For issues and feature requests, please use the GitHub issue tracker.