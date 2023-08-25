# BisCardX - Info Extracter 🛡️

**BisCardX** is a Streamlit application that facilitates the extraction of information from images. It utilizes the EasyOCR library to recognize text content in the uploaded images and then extracts relevant details such as names, designations, phone numbers, email addresses, websites, addresses, and pin codes.

## Requirements

Ensure you have the necessary dependencies installed by running:

```
pip install streamlit pandas pillow easyocr numpy mysql-connector-python
```

## How to Run

1. Clone this repository to your local machine.
2. Open the command line and navigate to the repository's directory.
3. Run the Streamlit app:

```
streamlit run app.py
```

4. The application will open in your default web browser, and you can start using it.

## Features

- Upload an image and preview it in the application.
- Extract information such as names, designations, phone numbers, email addresses, websites, addresses, and pin codes from the uploaded image.
- Upload extracted data into a MySQL database for storage and retrieval.
- View, update, and delete details stored in the MySQL database.


## Future Enhancements

- Improved user authentication and security features.
- More robust error handling and feedback to the user.
- Additional features for data manipulation and analysis.
- Enhancements to the UI/UX for a more polished experience.
