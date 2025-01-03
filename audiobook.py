import os
import sys
import pyttsx3
from gtts import gTTS
import PyPDF2

if len(sys.argv) < 3:
    print("Usage: python audiobook.py <relative_file_path> <starting_page_number>")
    sys.exit(1)

file_path = sys.argv[1]
start_page = int(sys.argv[2]) - 1

if not os.path.isfile(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
    sys.exit(1)

try:
    
    with open(file_path, "rb") as my_file:
        my_pdf_reader = PyPDF2.PdfReader(my_file)
        pages = len(my_pdf_reader.pages)
        print(f"The PDF has {pages} pages.")

        full_text = ""

        for page_num in range(start_page, pages):
            print(f"Extracting text from page {page_num + 1}...")
            page = my_pdf_reader.pages[page_num]
            page_text = page.extract_text()

            if page_text:
                full_text += page_text + "\n"
            else:
                print(f"Warning: Page {page_num + 1} has no extractable text.")

        if full_text:
            file_number = 1
            while os.path.exists(f"output{file_number}.mp3"):
                file_number += 1
            output_filename = f"output{file_number}.mp3"
            
            # Use gTTS (Google Text-to-Speech) to convert the text to speech
            tts = gTTS(text=full_text, lang='en')
            tts.save(output_filename)  # Save the speech as an MP3 file
            print(f"MP3 file has been saved as '{output_filename}'.")
        else:
            print("No text extracted from the PDF to convert to speech.")

except Exception as e:
    print(f"An error occurred: {e}")
