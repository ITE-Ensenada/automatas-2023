## Introduction

This API provides endpoints for performing Optical Character Recognition (OCR) on images and PDF files. It utilizes the Flask web framework and relies on the `imageprocessor` module for image and PDF processing.

## Getting Started

### Prerequisites

- Python (3.10 or higher)
- Flask
- `imageprocessor` module (ensure it is installed, you can install it using `pip install imageprocessor`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python your_app_name.py
   ```

   Replace `your_app_name.py` with the name of the file containing your Flask application.

## Endpoints

### 1. OCR on Images

#### Endpoint: `/ocr/image/frombytes`

- **Method:** POST
- **Parameters:**
  - `image` (File): The image file to be processed.

#### Example Usage:

```bash
curl -X POST -F "image=@/path/to/your/image.jpg" http://localhost:5000/ocr/image/frombytes
```

#### Response:

```json
{
  "text": "Extracted text from the image."
}
```

### 2. OCR on PDFs

#### Endpoint: `/ocr/pdf/frombytes`

- **Method:** POST
- **Parameters:**
  - `pdf` (File): The PDF file to be processed.

#### Example Usage:

```bash
curl -X POST -F "pdf=@/path/to/your/document.pdf" http://localhost:5000/ocr/pdf/frombytes
```

#### Response:

```json
{
  "text": "Extracted text from the PDF."
}
```

## Error Handling

- If the request does not contain a valid image or PDF file, the API will respond with a 400 Bad Request and an error message.

```json
{
  "Error": "Provide a valid image."
}
```

or

```json
{
  "Error": "Provide a valid PDF file."
}
```