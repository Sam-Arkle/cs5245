# Sam Arkle
# Resources used: https://selenium-python.readthedocs.io/getting-started.html
# https://www.selenium.dev/documentation/webdriver/browsers/firefox/

# To exceed a B:
# Scraped over 400 pages
# Installed add-ons to the webdriver
# Scraped 19 attributes for each 'match', using 3 different pages per match
# Executed scripts through the driver
# Used selenium to wait for certain elements (usually whichever was first scraped from a page)
# Made a robust program which deals with changes in the way data is displayed. For example, football matches prior to
# a certain year did not collect stats such as expected goals, and so the data from those years is ordered differently.
# (This also explains the relative sparsity of data in later data-entries as compared to earlier)

import json
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class Match:
    def __init__(self, title, date, venue, result, gf, ga, opponent, possession, attendance, sheff_yel, sheff_red,
                 sheff_fouls, sheff_fouled, sheff_tackles, sheff_pen_won, sheff_pen_giv, opp_yel, opp_red, opp_tackles):
        self.title = title
        self.date = date
        self.venue = venue
        self.result = result
        self.gf = gf
        self.ga = ga
        self.opponent = opponent
        self.possession = possession
        self.attendance = attendance
        self.sheff_yel = sheff_yel
        self.sheff_red = sheff_red
        self.sheff_fouls = sheff_fouls
        self.sheff_fouled = sheff_fouled
        self.sheff_tackles = sheff_tackles
        self.sheff_pen_won = sheff_pen_won
        self.sheff_pen_giv = sheff_pen_giv
        self.opp_yel = opp_yel
        self.opp_red = opp_red
        self.opp_tackles = opp_tackles


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
driver.install_addon('ublock_origin-1.44.4.xpi')
base_url = "https://fbref.com/en/squads/1df6b87e/Sheffield-United-Stats"
driver.get(base_url)

for j in range(1, 10, 1):
    table = driver.find_elements(By.XPATH, '//*[@id="matchlogs_for"]//*[@data-row]')
    match_list = []
    p = 0
    q = 0
    if j > 5:
        p = 2
        q = 5
    n = 0
    m = 0
    for i in range(1, len(table), 1):
        if (i + m > len(table)):
            break
        date = driver.find_element(By.CSS_SELECTOR,
                                   f'#matchlogs_for > tbody:nth-child(4) > tr:nth-child({i + m}) > th:nth-child(1)').text
        if date == 'Date':
            m += 1
            date = driver.find_element(By.CSS_SELECTOR,
                                       f'#matchlogs_for > tbody:nth-child(4) > tr:nth-child({i + m}) > th:nth-child(1)').text
        result = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[6]").text
        if result == '':
            break
        venue = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[5]").text
        result = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[6]").text
        gf = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[7]").text
        ga = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[8]").text
        opponent = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[9]").text
        possession = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[{12-p}]").text
        attendance = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[{13-p}]").text

        match_link = driver.find_element(By.XPATH,
                                         f"//*[@id='matchlogs_for']/tbody/tr[{i + m}]/td[{17 - p}]/a").get_attribute(
            'href')
        driver.get(match_link)
        driver.implicitly_wait(10)
        title = driver.find_element(By.CSS_SELECTOR, '#content > h1:nth-child(1)').text
        # driver.get(base_url)
        driver.back()
        sleep(1)
        driver.implicitly_wait(5)
        miscellaneous_link = driver.find_element(By.XPATH, f'/html/body/div[2]/div[7]/div[6]/div[{9-q}]/a')
        driver.execute_script("arguments[0].click();", miscellaneous_link)
        sleep(1)
        miscellaneous_table = driver.find_element(By.ID, 'matchlogs_for').find_elements(By.TAG_NAME, 'tr')
        driver.implicitly_wait(10)
        sleep(1.5)

        if re.search(driver.find_element(By.XPATH,
                               f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]").text,  'For Sheffield United Performance*'):
            n += 2
        sheff_yel = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[10]").text
        sheff_red = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[11]").text
        sheff_fouls = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[13]").text
        sheff_fouled = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[14]").text
        sheff_tackles = driver.find_element(By.XPATH,
                                            f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[18]").text
        sheff_pen_won = driver.find_element(By.XPATH,
                                            f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[19]").text
        sheff_pen_giv = driver.find_element(By.XPATH,
                                            f"//*[@id='matchlogs_for']//*[@data-row][{i + n}]/td[20]").text
        opponent_stats = driver.find_element(By.CSS_SELECTOR,
                                             'div.filter:nth-child(4) > div:nth-child(2) > a:nth-child(1)')
        driver.execute_script("arguments[0].click();", opponent_stats)
        opp_yel = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[10]").text
        opp_red = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[11]").text
        opp_tackles = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[18]").text
        driver.back()
        sleep(1)
        match = Match(title, date, venue, result, gf, ga, opponent, possession, attendance, sheff_yel, sheff_red,
                      sheff_fouls, sheff_fouled, sheff_tackles, sheff_pen_won, sheff_pen_giv, opp_yel, opp_red,
                      opp_tackles)
        match_list.append(match.__dict__)
        with open('matches.jl', 'a') as file:
            file.write(json.dumps(match.__dict__) + '\n')

    print(match_list)
    driver.find_element(By.CLASS_NAME, 'button2, prev').click()

driver.close()
