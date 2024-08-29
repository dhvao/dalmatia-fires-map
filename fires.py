import requests
from bs4 import BeautifulSoup

# List of dates you want to fetch data for
dates = ["25-08-2024", "26-08-2024", "27-08-2024", "28-08-2024"]

for date in dates:
    url = f"https://hvz.gov.hr/vijesti/dvoc-{date}-{date}/2024"
    print(f"Attempting to fetch data from: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the content section
        page_content = soup.find('div', class_='page_content')
        
        if page_content:
            # Extract and print date
            date_info = soup.find('li', class_='time_info').text.strip()
            print(f"Date: {date_info}")

            # Extract and print locations
            locations = page_content.find_all('strong')
            for location in locations:
                print(f"Location: {location.text.strip()}")
                
            # Extract detailed descriptions
            descriptions = page_content.find_all('p')
            for desc in descriptions:
                print(desc.text.strip())

            print("\n" + "-"*50 + "\n")
        else:
            print("No content found on the page.")
    else:
        print(f"Failed to retrieve data from: {url}")
