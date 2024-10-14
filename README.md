# PDF Merger Application

A simple cross-platform Python application for merging multiple PDF files into one. The application provides a sleek GUI built with Tkinter and uses `PyPDF2` for merging PDFs. It supports opening the merged file and its directory, and is compatible with Windows, macOS, and Linux.

## Features

- Merge multiple PDFs into one file.
- Easy-to-use GUI built with Tkinter.
- Automatically opens the merged file and its directory.
- Adaptive screen resolution and text size.

## Requirements

- Python 3.x
- Tkinter (for GUI, typically included with Python)
- PyPDF2 (for PDF merging)
- screeninfo (for detecting screen resolution)

## Installation and Setup

Follow these steps to clone the repository, set up the environment, and run the application.

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-NC4321/pdf-merger.git
cd pdf-merger
```

### 2. Create a Virtual Environment (Optional but Recommended)

It is a good practice to create and activate a virtual environment to avoid dependency conflicts with other Python projects.

For Windows:

```bash
python -m venv env
env\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

This command will install all the dependencies listed in the `requirements.txt` file (e.g., `PyPDF2` and `screeninfo`).

### 4. Run the Application

After setting up the environment and installing the dependencies, you can run the application:

For Windows:

```bash
python merger.py
```

For macOS/Linux:

```bash
python3 merger.py
```

This will open the application window where you can select and merge PDF files.

## How to Use

1. **Add Files:** Click the "Add Files" button to select PDF files that you want to merge.
2. **Clear List:** If you want to reset your selection, click the "Clear List" button.
3. **Merge PDFs:** After selecting the files, click "Merge PDFs" to combine them into one file.
4. **Access Merged PDF:** After merging, a clickable link will appear that allows you to:
    - Open the merged PDF directly.
    - Open the folder where the merged PDF is saved.

## Platform-Specific Notes

- **Windows:** The application will use `os.startfile()` to open the PDF and folder.
- **macOS:** The application will use `subprocess.call(['open', ...])` to open files and folders.
- **Linux:** The application will use `subprocess.call(['xdg-open', ...])` to open files and folders.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
