# TODO: yellow card count not quite right. Still not gone through multiple pages successfully
import json
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
# options.add_argument("window-size=1600x600")
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options)
driver.install_addon('ublock_origin-1.44.4.xpi')
base_url = "https://fbref.com/en/squads/1df6b87e/Sheffield-United-Stats"
driver.get(base_url)
miscellaneous_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div[6]/div[9]/a')
# table = driver.find_element(By.CSS_SELECTOR, "#div_matchlogs_for")
for j in range(1, 10, 1):
    table = driver.find_element(By.ID, 'matchlogs_for').find_elements(By.TAG_NAME, 'tr')
    # driver.find_elements(By.XPATH, '//*[@id="matchlogs_for"]//*[@data-row]')
    driver.find_element(By.CLASS_NAME, 'button2, prev').click()
    match_list = []
    for i in range(1, len(table), 1):
        date = driver.find_element(By.CSS_SELECTOR,
                                   f'#matchlogs_for > tbody:nth-child(4) > tr:nth-child({i}) > th:nth-child(1)').text
        if date != 'Date':
            result = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[6]").text
            if result != '':
                venue = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[5]").text
                result = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[6]").text
                gf = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[7]").text
                ga = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[8]").text
                opponent = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[9]").text
                possession = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[12]").text
                attendance = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[13]").text

                match_link = driver.find_element(By.XPATH,
                                                 f"//*[@id='matchlogs_for']/tbody/tr[{i}]/td[17]/a").get_attribute(
                    'href')
                driver.get(match_link)
                driver.implicitly_wait(10)
                title = driver.find_element(By.CSS_SELECTOR, '#content > h1:nth-child(1)').text
                # driver.get(base_url)
                driver.back()
                driver.implicitly_wait(5)
                miscellaneous_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div[6]/div[9]/a')
                driver.execute_script("arguments[0].click();", miscellaneous_link)
                sleep(1)
                miscellaneous_table = driver.find_element(By.ID, 'matchlogs_for').find_elements(By.TAG_NAME, 'tr')
                driver.implicitly_wait(10)
                sleep(1.5)

                sheff_yel = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[10]").text
                sheff_red = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[11]").text
                sheff_fouls = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[13]").text
                sheff_fouled = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[14]").text
                sheff_tackles = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[18]").text
                sheff_pen_won = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[19]").text
                sheff_pen_giv = driver.find_element(By.XPATH, f"//*[@id='matchlogs_for']//*[@data-row][{i}]/td[20]").text
                opponent_stats = driver.find_element(By.CSS_SELECTOR,
                                                     'div.filter:nth-child(4) > div:nth-child(2) > a:nth-child(1)')
                driver.execute_script("arguments[0].click();", opponent_stats)
                opp_yel = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[10]").text
                opp_red = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[11]").text
                opp_tackles = driver.find_element(By.XPATH, f"//*[@id='matchlogs_against']//*[@data-row][{i}]/td[18]").text
                driver.back()
                match = Match(title, date, venue, result, gf, ga, opponent, possession, attendance, sheff_yel, sheff_red,
                              sheff_fouls, sheff_fouled, sheff_tackles, sheff_pen_won, sheff_pen_giv, opp_yel, opp_red,
                              opp_tackles)
                match_list.append(match.__dict__)
                with open('matches.jl', 'a') as file:
                    file.write(json.dumps(match.__dict__) + '\n')

    print(match_list)
    driver.find_element(By.CLASS_NAME, 'button2, prev').click()

driver.close()
