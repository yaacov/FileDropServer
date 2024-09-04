"""
FileDropServer: A lightweight HTTP server for file uploads.

This module implements a custom HTTP server using Python's http.server module.
It allows seamless file uploads through POST requests.

Usage:
    python server.py

Features:
    - Handle file uploads via POST requests
    - Generate unique filenames for uploaded files
"""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import uuid

UPLOAD_DIR = './uploads'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A custom HTTP request handler for serving files and handling uploads.
    
    Attributes:
        None
    
    Methods:
        do_GET(): Handles GET requests to serve files.
        do_POST(): Handles POST requests to handle file uploads.
    """

    def do_GET(self):
        """
        Handles GET requests to serve files the uploader.py utility
        """
        file_path = "./uploader.py"
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")

    def do_POST(self):
        """
        Handles POST requests to upload files.
        
        This method processes incoming POST requests, extracts the file content,
        saves it to the specified upload directory, and returns a success message.
        
        Args:
            None
        
        Returns:
            None
        
        Side Effects:
            Saves uploaded file to UPLOAD_DIR directory.
        """
        # Get the content length of the POST data
        content_length = int(self.headers['Content-Length'])

        # Check if the 'X-Filename' header exists
        client_filename = self.headers.get('X-Filename')

        if client_filename:
            # Use the filename provided by the client in the headers
            file_name = os.path.basename(client_filename)
        else:
            # Generate a unique filename if no filename is provided in the headers
            unique_id = uuid.uuid4()  # Generate a unique ID
            timestamp = int(time.time())  # Get the current timestamp
            file_name = f"uploaded_file_{unique_id}_{timestamp}"

        file_path = os.path.join(UPLOAD_DIR, file_name)

        # Read and save the uploaded file
        with open(file_path, 'wb') as f:
            f.write(self.rfile.read(content_length))

        # Send response to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"File uploaded successfully as {file_name}".encode('utf-8'))

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    server_address = ('', 8000)  # Serve on port 8000
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()
