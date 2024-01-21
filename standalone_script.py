import re
import webbrowser

def detect_and_open_link(text):
    # Regular expression to find URLs in the text
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Find all URLs in the text
    urls = re.findall(url_pattern, text)

    if urls:
        for url in urls:
            print(f"Opening link: {url}")
            webbrowser.open(url)
    else:
        print("No links found in the text.")

def process_text_and_open_link():
    # Get text input from the user
    text_with_link = input("Enter a text containing a link: ")

    # Call the function to detect and open links
    detect_and_open_link(text_with_link)

# Example usage:
text_with_link = input("Enter a text containing a link: ")
detect_and_open_link(text_with_link)

# Other parts of your script...

# Call the function to process text and open links
process_text_and_open_link()

# Other parts of your script...
