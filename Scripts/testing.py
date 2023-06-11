import requests

def upload_image_to_server(image_url, server_url):
    try:
        # Download the image from the provided link
        response = requests.get(image_url)
        response.raise_for_status()

        # Upload the image to the server
        files = {'image': response.content}
        upload_response = requests.post(server_url, files=files)
        upload_response.raise_for_status()

        # Get the new image link from the server response
        new_image_link = upload_response.text
        return new_image_link
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Example usage
image_link = "https://example.com/image.jpg"
upload_server_url = "https://example-upload-server.com/upload"
new_image_link = upload_image_to_server(image_link, upload_server_url)
print("New image link:", new_image_link)


