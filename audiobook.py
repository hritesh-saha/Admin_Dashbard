import pyttsx3
import PyPDF2

file_path = "Audex\\DSA.pdf"  # Replace with your desired relative file path

# Check if the file exists
try:
    # Open the PDF file
    with open(file_path, "rb") as my_file:
        my_pdf_reader = PyPDF2.PdfReader(my_file)
        pages = len(my_pdf_reader.pages)
        print(f"The PDF has {pages} pages.")

        # Initialize the Text-To-Speech Engine
        speaker = pyttsx3.init()

        start_page = 22

        for page_num in range(start_page, pages):
            print(f"Reading from page {page_num + 1}...")
            page = my_pdf_reader.pages[page_num]
            page_text = page.extract_text()
            speaker.say(page_text)
            speaker.runAndWait()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
