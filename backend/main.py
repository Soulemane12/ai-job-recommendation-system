import os
import json
from PyPDF2 import PdfReader

# Define the absolute path for the upload folder
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'uploads'))
pdf_file_name = "Soulemane_Sow_Resume.pdf"

# Construct the full path to the file
pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file_name)

# Define the recommendations data
data = [
    ("python, machine learning, deep learning", "AI Engineer"),
    ("javascript, react, html, css, web development", "Frontend Developer"),
    ("html, css, javascript, jquery, bootstrap", "Web Designer"),
    ("linux, networking, cloud services", "DevOps Engineer"),
    ("sales, crm, negotiation", "Sales Manager"),
]

# Initialize recommendations
recommendations = {
    "filename": "",
    "recommendations": [],
    "keywords_found": []
}

# Check if the file exists
if os.path.exists(pdf_path):
    print(f"File found: {pdf_path}")

    try:
        # Open and read the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            extracted_text = ""

            # Loop through each page in the PDF and extract text
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()

            # Display the first 500 characters of the extracted text for validation
            print("Extracted Text (first 500 characters):")
            print(extracted_text[:500])

            # Save extracted text for debugging
            extracted_text_path = os.path.join(UPLOAD_FOLDER, 'extracted_text.txt')
            with open(extracted_text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(extracted_text)
            print(f"Extracted text saved to: {extracted_text_path}")

            # Process keywords and generate recommendations
            recommendations['filename'] = pdf_file_name
            keywords_found = set()

            for keywords, role in data:
                keywords_list = [keyword.strip().lower() for keyword in keywords.split(',')]
                if any(keyword in extracted_text.lower() for keyword in keywords_list):
                    recommendations['recommendations'].append(role)
                    keywords_found.update(keywords_list)

            recommendations['keywords_found'] = list(keywords_found)

            # Display final recommendations
            print("Final Recommendations:")
            print(json.dumps(recommendations, indent=4))

            # Save recommendations to JSON file
            recommendations_file_path = os.path.join(UPLOAD_FOLDER, 'recommendations.json')
            with open(recommendations_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(recommendations, json_file, indent=4)
                json_file.flush()  # Ensure the data is flushed to disk

            # Confirmation that the file is written
            print(f"Recommendations saved to: {recommendations_file_path}")

            # Read back the saved JSON file for confirmation
            with open(recommendations_file_path, 'r', encoding='utf-8') as json_file:
                content = json.load(json_file)
                print("Contents of the JSON file after writing:")
                print(json.dumps(content, indent=4))  # Print the content for verification

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
else:
    print(f"File not found: {pdf_path}")
  