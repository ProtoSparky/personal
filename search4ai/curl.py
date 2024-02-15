import requests 

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
url = 'https://en.wikipedia.org/wiki/Kuben_Upper_Secondary_School'
html_content = get_html_content(url)
if html_content:
    print(html_content)
else:
    print("Failed to retrieve HTML content.")
