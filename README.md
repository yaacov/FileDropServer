# FileDropServer

FileUploaderServer is a lightweight HTTP server built with Python that allows users to upload files. The server accepts file uploads via POST requests and stores them in a specified directory. Each upload can either use a custom filename (provided in the request headers) or have a unique name generated automatically. Users can retrieve
an uploader.py utility by sending GET requests to the server.

## Features:

Supports file uploads via POST requests with multipart form data.
Automatically generates unique filenames for each upload or accepts a custom filename from the request.
Serves an uploader utility via GET requests.
Simple to configure and run without external dependencies.

## Usage:

### Start the server:

```bash
python server.py
```

The server listens on port 8000 by default and stores uploaded files in the uploads/ directory.

### Upload a file using the uploader.py utlity:

```bash
# Fetch the uploader
curl http://<server-ip>:8000/ -o uploader.py

# Upload a file
python uploader.py <server-ip> our_file.tar.gz
```

### Upload a file using curl:

```bash
# Set file name
curl --data-binary @your_file.tar.gz -H "X-Filename: custom_name.tar.gz" http://<server-ip>:8000/

# Uploader will asign a rundom name to the file
curl --data-binary @your_file.tar.gz http://<server-ip>:8000/
```

### Retrieve the file via a GET request:

```bash
curl http://<server-ip>:8000/ -o uploader.py
```
