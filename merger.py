import PyPDF2
import os
import subprocess
from tkinter import Tk, Label, Listbox, filedialog, END, SINGLE, Canvas, CENTER
from tkinter import ttk
from pathlib import Path
from screeninfo import get_monitors
from tkinter.font import Font
import platform  # To detect OS

# Function to merge selected PDFs
def merge_pdfs(pdf_list, output_path):
    try:
        # Create a PdfMerger object
        merger = PyPDF2.PdfMerger()

        # Append each selected PDF file to the merger
        for pdf in pdf_list:
            merger.append(pdf)

        # Write the combined PDF to the output file
        with open(output_path, 'wb') as output_pdf:
            merger.write(output_pdf)

        # Close the merger object
        merger.close()

        # Display a clickable link to open the merged file and the file path
        display_link(output_path)
    except Exception as e:
        print(f"Error: {e}")

# Function to select PDF files using file dialog
def select_pdfs():
    selected_files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return selected_files

# Function to generate a combined filename from the selected PDFs
def generate_output_filename(pdf_list):
    base_names = [os.path.splitext(os.path.basename(pdf))[0] for pdf in pdf_list]
    combined_name = "_".join(base_names[:3])
    if len(base_names) > 3:
        combined_name += "_and_more"
    return combined_name + ".pdf"

# Function to get the Downloads folder path
def get_downloads_folder():
    return str(Path.home() / "Downloads")

# Function to add files to the listbox
def add_files():
    pdf_files = select_pdfs()
    for file in pdf_files:
        if file not in listbox.get(0, END):  # Avoid adding duplicates
            listbox.insert(END, file)

# Function to merge selected files
def merge_selected_files():
    if listbox.size() == 0:
        print("Please add at least one PDF file.")
        return

    # Get the list of selected PDFs
    pdf_files = listbox.get(0, END)

    # Generate the output filename
    output_filename = generate_output_filename(pdf_files)

    # Set the path to the Downloads folder
    downloads_path = get_downloads_folder()
    output_path = os.path.join(downloads_path, output_filename)

    # Merge the PDFs
    merge_pdfs(pdf_files, output_path)

# Function to clear the listbox
def clear_list():
    listbox.delete(0, END)
    link_label.config(text="", cursor="")
    folder_link_label.config(text="", cursor="")

# Function to display clickable link for opening the file and the file path
def display_link(file_path):
    bold_underline_font = Font(family="Helvetica", size=adaptive_font_size(14), weight="bold", underline=1)
    link_label.config(text="Open merged PDF", cursor="hand2", font=bold_underline_font, fg="lightblue")
    link_label.bind("<Button-1>", lambda e: open_file(file_path))

    folder_link_label.config(text="Open file path", cursor="hand2", font=bold_underline_font, fg="lightblue")
    folder_link_label.bind("<Button-1>", lambda e: open_file_path(file_path))

# Function to open the merged file
def open_file(file_path):
    # Use platform-specific commands to open files
    if platform.system() == 'Windows':
        os.startfile(file_path)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', file_path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', file_path])

# Function to open the folder containing the merged file
def open_file_path(file_path):
    folder = os.path.dirname(file_path)
    if platform.system() == 'Windows':
        os.startfile(folder)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])

# Function to get the actual screen resolution using the screeninfo library
def get_actual_screen_resolution():
    for monitor in get_monitors():
        return monitor.width, monitor.height  # Return the resolution of the primary monitor

# Function to calculate adaptive font size based on screen resolution
def adaptive_font_size(base_size):
    screen_width, _ = get_actual_screen_resolution()
    scale_factor = screen_width / 1920  # Base size designed for 1920px width, adjust according to current screen
    return int(base_size * scale_factor)

# Set up the main window with adaptive size based on screen resolution
def setup_window(root):
    screen_width, screen_height = get_actual_screen_resolution()  # Get the screen resolution
    window_width = int(screen_width * 0.7)  # Use 70% of the screen width
    window_height = int(screen_height * 0.8)  # Use 80% of the screen height

    root.geometry(f"{window_width}x{window_height}")  # Set the window size

    # Set up the main window with modern design
    root.title("PDF Merger")
    root.configure(bg="#1E1E1E")  # Dark modern background

# Set up the GUI
root = Tk()

setup_window(root)  # Call the function to set up window size dynamically

# Customizing styles for rounded buttons and hover effects
style = ttk.Style()
style.configure("RoundedButton.TButton", font=(adaptive_font_size(14)), padding=12, relief="flat", background="#4A4A4A", foreground="black")
style.map("RoundedButton.TButton", background=[("active", "#6C6C6C")], relief=[("pressed", "flat")])

# Apply background color to the ttk.Frame using the ttk style system
style.configure("Custom.TFrame", background="#1E1E1E")  # Custom style for the frame background

# Instructions label with adaptive font size for the header
label = Label(root, text="Upload PDF files to merge", font=(adaptive_font_size(18)), bg="#1E1E1E", fg="white")
label.pack(pady=30)

# Center the listbox
canvas = Canvas(root, bg="#1E1E1E", highlightthickness=0)
canvas.pack(pady=10)

# Listbox for uploaded files with adaptive width, height, and matching font size
listbox_width = int(get_actual_screen_resolution()[0] * 0.04)  # Adaptive listbox width
listbox_height = int(get_actual_screen_resolution()[1] * 0.015)  # Adaptive listbox height

listbox = Listbox(canvas, selectmode=SINGLE, width=listbox_width, height=listbox_height, font=(adaptive_font_size(14)), bg="#1E1E1E", fg="white", bd=0, highlightthickness=0, relief="flat")
listbox.pack(anchor=CENTER)  # Centering the listbox horizontally

# Buttons frame with matching background color
btn_frame = ttk.Frame(root, style="Custom.TFrame")  # Apply custom frame style
btn_frame.pack(pady=30)

# Add files button with dark grey color and hover effect, with adaptive width
add_button = ttk.Button(btn_frame, text="Add Files", command=add_files, style="RoundedButton.TButton")
add_button.grid(row=0, column=0, padx=adaptive_font_size(20))

# Clear list button with dark grey color and hover effect, with adaptive width
clear_button = ttk.Button(btn_frame, text="Clear List", command=clear_list, style="RoundedButton.TButton")
clear_button.grid(row=0, column=1, padx=adaptive_font_size(20))

# Merge PDFs button
merge_button = ttk.Button(root, text="Merge PDFs", command=merge_selected_files, style="RoundedButton.TButton")
merge_button.pack(pady=adaptive_font_size(20))

# Label for the clickable link to open the merged PDF
link_label = Label(root, text="", font=(adaptive_font_size(14)), fg="lightblue", bg="#1E1E1E")
link_label.pack(pady=20)

# Label for the clickable link to open the file path
folder_link_label = Label(root, text="", font=(adaptive_font_size(14)), fg="lightblue", bg="#1E1E1E")
folder_link_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()