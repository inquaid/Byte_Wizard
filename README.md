# Byte_Wizard

Byte_Wizard is an automated installer designed to simplify the process of setting up essential software and tools on your Windows machine. The project is powered by Python and utilizes batch scripts to manage the installation process.

## Software Included in the Installation

- Chocolatey (Package Manager)
- MinGW (Minimalist Development Environment for Native Windows Applications)
- Python (Programming Language)
- Java Development Kit (JDK)
- Visual Studio Code (Source Code Editor)
- NetBeans (Java IDE)
- JetBrains Toolbox (IDE Management for IntelliJ IDEA, PyCharm, etc.)
- Code::Blocks (IDE for C, C++, and Fortran)

## Features

- **Automated Installation:** Easily install a suite of essential software with minimal user interaction.
- **Chocolatey Integration:** Uses Chocolatey, a popular Windows package manager, to handle software installations.
- **User-Friendly Interface:** A simple UI allows users to select options and execute tasks without the need for command-line operations.
- **Customizable:** Modify the included Python scripts and batch files to add or remove software as needed.

## Project Structure

- **Python Files**: Handle the backend logic and UI for the application.
  - `main.py`: Initializes the program.
  - `UI.py`: Manages the main interface where users interact with the application.
  - `my_functions.py`: Contains all the functions for the program, including calls to the installation batch files.
  - `second_window.py`: Manages the installation window. This part of the program may require further modifications.

- **Batch Files**: Execute specific installation commands.
  - `choco_install.bat`: Installs Chocolatey, the package manager used for subsequent software installations.
  - `mingw_install.bat`: Installs MinGW, a minimalist development environment for native Windows applications.
  - `python_install.bat`: Installs Python, a versatile programming language.
  - `java_install.bat`: Installs the Java Development Kit (JDK) required for Java development.
  - `vsc_install.bat`: Installs Visual Studio Code, a lightweight but powerful source code editor.
  - `netbeans_install.bat`: Installs NetBeans, an IDE primarily for Java development.
  - `jetbrain_install.bat`: Installs JetBrains Toolbox, which allows you to manage JetBrains IDEs like IntelliJ IDEA, PyCharm, etc.
  - `codeblocks_install.bat`: Installs Code::Blocks, an IDE for C, C++, and Fortran.

## Getting Started

### Prerequisites

Before running Byte_Wizard, ensure that your system meets the following requirements:

- Windows 7 or later

### Installation Steps

1. **Download the Byte_Wizard Package**
   - Navigate to the [Download](https://github.com/inquaid/Byte_Wizard/tree/main/Download) section of this repository and download the latest version of `Byte_Wizard.zip`.

2. **Extract the ZIP File**
   - Unzip the downloaded file to a directory of your choice.

3. **Run the Application**
   - Navigate to the extracted directory and double-click on `byte_wizard_no_console.exe` to launch the program.

4. **Install Chocolatey**
   - In the program interface, first click on the "Install Chocolatey" button.
   - Once the installation process begins, follow the on-screen prompts, if any, and press any key to continue when prompted.

5. **Install Software**
   - After installing Chocolatey, choose the software you wish to install by clicking on the respective options within the UI.
   - The installation will proceed automatically, with progress displayed in the program window.

6. **Enjoy!**
   - Once all installations are complete, your system will be ready with the selected software installed.

## Customization

If you'd like to customize the software installation process, you can edit the Python and batch files to suit your needs. Each file is well-commented to guide you through making changes.

## Contributing

If you find any issues or have suggestions for improving Byte_Wizard, feel free to open an issue or submit a pull request. Contributions are always welcome!

## Acknowledgments

- [Chocolatey](https://chocolatey.org/) for providing a robust package management solution for Windows.
- [Python](https://www.python.org/) for making automation simple and powerful.
