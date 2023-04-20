import requests
from bs4 import BeautifulSoup


class Manpower:
    def __init__(self):
        self.main_url = "http://manpower.si"
        self.response = requests.get(self.main_url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.all_links = []

    def check_links(self, links_selector):
        self.links = [link.get("href") for link in self.soup.select(links_selector)]
        self.valid_links = []
        print("\n")
        for link in self.links:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    self.valid_links.append(link)
                    print(f"{links_selector} - {link}: 200 OK")
                else:
                    print(f"{links_selector} - {link}: {response.status_code}")
            except:
                print(f"{links_selector} - {link}: ERROR")
        return self.valid_links

    def check_footer(self):
        header_list = self.check_links("footer a")
        footer_list = []
        for link in header_list:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                footer_links = self.check_links("footer a")
                footer_list.extend(footer_links)
        return footer_list



