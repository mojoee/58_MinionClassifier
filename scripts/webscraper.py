import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Check if the URL is valid.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def save_image(url, folder_path, i):
    """
    Save the image from the URL to the specified folder.
    """
    response = requests.get(url, stream=True)
    image_name = os.path.join(folder_path, str(i))

    with open(image_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

def scrape_images(url, folder_path):
    """
    Scrape images from the given URL and save them to the specified folder.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i, img in enumerate(img_tags):
        img_url = img.attrs.get("src")
        if not img_url:
            continue

        # Resolve relative URLs
        img_url = urljoin(url, img_url)
        if not is_valid(img_url):
            continue

        try:
            save_image(img_url, folder_path, i)
            print(f"Downloaded {img_url}")
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")

if __name__ == "__main__":
    minions = ["Bob", "Kevin", "Stuart", "Bob", "Dave", "Jerry", "Carl", 
               "Phil", "Steve", "Tim", "Mark", "Larry", "Tom", "Donny", "Ken",
               "Mike", "John", "Norbert", "Josh", "Lance"]
    for minion in minions:

        url = f"https://www.google.com/search?q=minion+{minion}&sxsrf=APwXEdcxKYmeDvIvNHtBiF5ahzbvfjhKug:1681907033814&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjcpK7697X-AhU_QfUHHS6xB4kQ_AUoAXoECAEQAw&biw=1440&bih=821&dpr=2"  # Replace with the URL of the page you want to scrape images from
        folder_path = f"./data/{minion}"
        scrape_images(url, folder_path)