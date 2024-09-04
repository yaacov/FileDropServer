"""
FileDropServer Uploader Module

This module contains functions for uploading files to a FileDropServer.

Functions:
    upload_file(ip, file_path): Uploads a file to the server at the given IP address.

Usage:
    python uploader.py <server-ip> <file-path>
"""

import http.client
import os
import sys


def upload_file(ip, file_path):
    """
    Uploads a file to the server at the given IP address.

    Args:
        ip (str): The IP address of the server.
        file_path (str): The path to the local file to upload.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as file:
        file_content = file.read()

    body = file_content.decode("latin1")

    # Set up the connection and headers, including custom X-Filename
    conn = http.client.HTTPConnection(ip, 8000)
    headers = {
        "Content-Type": "multipart/form-data; charset=utf-8",
        "Content-Length": str(len(body)),
        "X-Filename": file_name,
    }

    # Send the request
    conn.request("POST", "/", body, headers)
    response = conn.getresponse()

    # Handle the response
    if response.status == 200:
        print(f"File uploaded successfully: {file_name}")
    else:
        print(f"Failed to upload file: {response.status} {response.reason}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python upload_file.py <server-ip> <file-path>")
        sys.exit(1)

    ip_address = sys.argv[1]
    file_to_upload = sys.argv[2]

    upload_file(ip_address, file_to_upload)
