import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementNotInteractableException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.action_chains import ActionChains
import json

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(500)
driver.set_window_size(1500,1000)
# ===================================================================================================================================================================
# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')
# ===================================================================================================================================================================

def run():
  index = 0
  youtuberDict = {}
  for i in range(1,6):
    driver.get(f"https://www.youha.info/search/influencers/youtube-channels?page={i}")
    sleep(3)
    youtubers = driver.find_elements(By.CSS_SELECTOR,'div.MuiDataGrid-row')
    for youtuber in youtubers:
      try:
        imgUrl = youtuber.find_element(By.CSS_SELECTOR,'img.MuiAvatar-img.mui-style-1hy9t21').get_attribute('src').strip()
        name = youtuber.find_element(By.CSS_SELECTOR,'p.MuiTypography-root.MuiTypography-body1.mui-style-1hxmejr').text.strip()
        link = youtuber.find_element(By.CSS_SELECTOR,'div.MuiBox-root.mui-style-k008qs a').get_attribute('href').strip()
        subscribers = int(youtuber.find_elements(By.CSS_SELECTOR,'div.MuiDataGrid-cell--withRenderer.MuiDataGrid-cell.MuiDataGrid-cell--textRight')[0].text.replace(',','').strip())
        print(f"index : {index}, name : {name}, subscribers, {subscribers}, link : {link}, imgUrl : {imgUrl}")
        youtuberDict[index] = {'name' : name, 'subscribers' : subscribers, 'link' : link, 'imgUrl' : imgUrl}
        index += 1
      except Exception as e:
        continue
  toJson(youtuberDict,f'youtuberData')
    