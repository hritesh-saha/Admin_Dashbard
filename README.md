![github](https://img.shields.io/badge/GitHub-000000.svg?style=for-the-badge&logo=GitHub&logoColor=white)
![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

<h1 align=center>Audex (PDF to MP3 Converter)</h1>

**Audex** is a Python script that converts the text from PDF files into an audio MP3 file using Google's Text-to-Speech (gTTS) API. The script reads a PDF from a given file path starting from the specified page number, converts the text of each page to speech, and saves the output as an MP3 file.

## Features
- Converts a PDF's text to audio, starting from a specified page.
- Outputs audio as MP3 using gTTS (Google Text-to-Speech).
- Can be easily run from the command line.

## Requirements
Before using the script, make sure you have the following Python libraries installed:
- `gtts`: Google Text-to-Speech
- `PyPDF2`: PDF handling library
- `os`: File system operations
- `sys`: Command-line argument handling

You can install the necessary libraries by running the following:

```bash
pip install gtts PyPDF2
```
## How to Use

### 1. Clone the Repository:
First, clone or download the repository to your local machine.

```bash
git clone <repository_url>
```
navigate into the clone directory `Audex`
```bash
cd Audex
```

### 2. Run the Script:
The script can be run from the command line, passing two arguments:

- The relative or absolute file path of the PDF.
- The starting page number (1-based index).

#### Example:
```bash
python audiobook.py <file_path> <starting_page_number>
```
### 3. Sample PDF for Testing:
For testing purposes, a sample PDF file named `DSA.pdf` is provided in this repository. You can test the script by running:
```bash
python audiobook.py "DSA.pdf" 23
```
This will read the PDF file starting from page 23 and convert it to audio.

>[!NOTE]
>### Important Notes and Caution
>
> - ***Long PDFs will take longer:*** The time required for conversion increases with the number of pages and amount of text on each page. Large PDFs may take a longer time (e.g., more than 10 minutes) to process, as the script needs to send text to Google's server for each page and wait for a response.
>
>   - ***Recommendation:*** For longer PDFs, it is advisable to break down the conversion process by converting smaller portions (e.g., process 10 pages at a time).
>
> - ***PDF Formatting:*** The script relies on extracting plain text from the PDF, so PDFs with complex layouts, images, or scanned pages may not extract cleanly. Text-heavy PDFs will provide the best results.
