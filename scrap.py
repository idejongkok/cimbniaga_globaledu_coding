import requests
from bs4 import BeautifulSoup

# URL yang akan di-scrape
url = 'https://google.com'  # Ganti dengan URL yang diinginkan

# Melakukan permintaan ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Menggunakan BeautifulSoup untuk mem-parsing HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mengambil data yang diinginkan, misalnya semua teks dalam tag <p>
    paragraphs = soup.find_all('p')
    data = [para.get_text() for para in paragraphs]

    # Menyimpan data ke dalam file teks
    with open('data.txt', 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")
else:
    print(f"Failed to retrieve data: {response.status_code}")
