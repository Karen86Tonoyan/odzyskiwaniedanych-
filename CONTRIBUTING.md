# Contributing to Odzyskiwanie Danych (Data Recovery)

Thank you for your interest in contributing to this open-source data recovery project! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear description of the problem
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your operating system and Python version

### Suggesting Features

We welcome feature suggestions! Please open an issue describing:
- The feature you'd like to see
- Why it would be useful
- Any implementation ideas you have

### Code Contributions

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/odzyskiwaniedanych-.git
   cd odzyskiwaniedanych-
   ```

3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes** following our coding standards:
   - Write clear, readable code
   - Add comments where necessary
   - Follow PEP 8 style guide for Python
   - Test your changes thoroughly

5. **Test your changes**:
   ```bash
   # Run the example script
   python example.py
   
   # Run the recovery tool
   python recovery.py --scan test_recovery --output ./test_output
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request** on GitHub

## Development Guidelines

### Adding New File Type Support

To add support for a new file type, update the `FILE_SIGNATURES` dictionary in `recovery.py`:

```python
FILE_SIGNATURES = {
    'yourtype': {
        'header': b'\x00\x00\x00\x00',  # File signature bytes
        'footer': b'\xFF\xFF\xFF\xFF',  # Optional footer bytes
        'ext': '.yourext'               # File extension
    },
}
```

### Code Style

- Use 4 spaces for indentation
- Keep lines under 100 characters when possible
- Use descriptive variable names
- Add docstrings to functions and classes
- Include type hints where helpful

### Testing

Before submitting a PR:
1. Test with the example script
2. Test with real-world scenarios if possible
3. Verify no existing functionality is broken
4. Check for edge cases

## Ideas for Contributions

Here are some areas where contributions would be particularly valuable:

- **More file types**: Add support for more file formats (MP4, DOCX, etc.)
- **GUI interface**: Create a graphical user interface
- **Better scanning**: Improve file detection algorithms
- **Performance**: Optimize scanning for large drives
- **Documentation**: Improve docs, add tutorials
- **Tests**: Add automated unit tests
- **Internationalization**: Add support for multiple languages

## Questions?

Feel free to open an issue if you have questions about contributing!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
