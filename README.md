# Byte Wizard

![Byte Wizard Logo](assets/wizard_icon.png)

Byte Wizard is a sleek, user-friendly software installation assistant designed to streamline the setup of essential development tools on your Windows system. With a modern interface and one-click installation process, Byte Wizard simplifies the often complex process of configuring a development environment.

## Features

- **Modern, Intuitive UI**: Clean and polished interface that's easy to navigate
- **One-Click Installation**: Install complex development tools with a single click
- **Visual Feedback**: Clear installation progress indicators
- **Categorized Software**: Tools organized by category for easy discovery
- **Tooltips**: Helpful descriptions of each software package
- **Cross-Platform Compatible**: Works on Windows systems with plans for Linux/macOS support

## Software Available for Installation

### Essential Tools
- **Chocolatey**: Package manager for Windows that simplifies software installation

### Programming Languages
- **C/C++ (MinGW)**: Minimalist GNU for Windows compiler and toolset
- **Python**: Versatile programming language popular for web, data science, and general applications
- **Java**: Cross-platform language and runtime environment

### Development Environments
- **VS Code**: Lightweight yet powerful code editor with extensive plugin support
- **NetBeans**: Full-featured IDE primarily for Java development
- **JetBrains Tools**: Suite of professional IDEs for various languages
- **Code::Blocks**: Free, open-source IDE for C/C++ development

### Simulation Tools
- **Iverilog**: Verilog HDL compiler and simulation tool
- **GtkWave**: Waveform viewer for digital simulation results

## Project Structure

The project follows a clear, modular organization:

```
Byte_Wizard/
├── assets/                 # Images and static resources
├── src/                    # Source code
│   ├── core/               # Core functionality
│   │   └── functions.py    # Helper functions and installation logic
│   ├── scripts/            # Installation scripts
│   │   └── installers/     # Batch files for software installation
│   ├── ui/                 # User interface components
│   │   └── main_window.py  # Main application window
│   └── main.py             # Application entry point
└── README.md               # Documentation
```

## Getting Started

### Prerequisites

- Windows 7 or later
- Administrator privileges (required for software installation)
- Internet connection

### Installation

1. **Download the latest release**
   - Download the latest release from the [Releases](https://github.com/yourusername/Byte_Wizard/releases) page

2. **Run the application**
   - Extract the ZIP file to a directory of your choice
   - Run `Byte_Wizard.exe` to start the application

3. **Install software**
   - Click on the software you want to install
   - Follow any on-screen prompts if required

## Development

### Setting Up the Development Environment

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Byte_Wizard.git
   cd Byte_Wizard
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application in development mode:
   ```
   python src/main.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Icons and visual elements inspired by [Feather Icons](https://feathericons.com/)
- Color palette based on [Coolors](https://coolors.co/)
- Special thanks to all contributors and early testers
