import os
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as eC


def parse_main_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def get_total_number_of_pages(driver):
    if driver.page_source:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        pagination = soup.find("ul", class_="pagination")

        if pagination:
            pagination_items = pagination.find_all("li", class_="pagination__item")

            last_page_text = pagination_items[-2].find("span").text

            if last_page_text.isdigit():
                total_number_of_pages = int(last_page_text)
                return total_number_of_pages
    return 1


def selecting_page(driver, page_number, keyword="page"):
    try:
        selector = WebDriverWait(driver, 20).until(
            eC.element_to_be_clickable(
                (By.XPATH, f'//span[@aria-label="{keyword} {page_number}"]')
            )
        )
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);"
        )
        WebDriverWait(driver, 30).until(
            eC.element_to_be_clickable((By.CLASS_NAME, "explore__link"))
        )
        print(f"Page {page_number} is ready")
        selector.click()
        return driver
    except Exception as e:
        print(f"Failed to select page {page_number}. Error: {e}")


def get_list_of_links(driver):
    try:
        WebDriverWait(driver, 30).until(
            eC.visibility_of_all_elements_located((By.CLASS_NAME, "explore__link"))
        )
        soup = BeautifulSoup(driver.page_source, "html.parser")
        container = soup.find("div", class_="full-content")
        if container:
            links_list = container.find_all("div", class_="mvl-card--explore")
            return [link_of_hero.find("a")["href"] for link_of_hero in links_list]
    except Exception as e:
        print(f"Failed to wait for hero links. Error: {e}")
    return None


def parse_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        else:
            print(
                f"Failed to retrieve page content. Status code: {response.status_code}"
            )
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def get_bio_from_links(links_list):
    all_superhero_info = []
    labels_bio = [
        "Universe",
        "Other Aliases",
        "Education",
        "Place of Origin",
        "Identity",
        "Known Relatives",
    ]

    for url in links_list:
        soup = parse_link(f"https://www.marvel.com{url}")

        if not soup:
            continue

        superhero_info = {
            "Name": "N/A",
            "Link": f"https://www.marvel.com{url}",
        }

        name_element = soup.find("span", {"class": "masthead__headline"})
        if name_element:
            superhero_info["Name"] = name_element.text.strip()

        for label in labels_bio:
            item = soup.find("p", {"class": "railBioInfoItem__label"}, string=label)
            if item:
                values = [
                    li.text.strip()
                    for li in item.find_next("ul", {"class": "railBioLinks"}).find_all(
                        "li"
                    )
                ]
                superhero_info[label] = values

        all_superhero_info.append(superhero_info)

    return all_superhero_info


def create_csv(char_list, filename):
    fieldnames = [
        "Name",
        "Link",
        "Universe",
        "Other Aliases",
        "Education",
        "Place of Origin",
        "Identity",
        "Known Relatives",
    ]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(char_list)


if __name__ == "__main__":
    marvel_url = "https://www.marvel.com/characters"
    driver = parse_main_page(marvel_url)
    heroes_list = []

    for page in range(1, get_total_number_of_pages(driver) + 1):
        driver = selecting_page(driver, page)
        hero_links = get_list_of_links(driver)
        if hero_links:
            heroes_list.extend(hero_links)

    char_list = get_bio_from_links(heroes_list)
    create_csv(char_list, "marvel_characters.csv")

    driver.quit()
