from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service("C:/Users/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL
url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)

# Wait for table to load
time.sleep(10)
data=[]
i=4
while i<6:
    l=[]

    time.sleep(10)
    view_button = driver.find_elements(By.LINK_TEXT, 'View Details')[i]
        
    driver.execute_script("arguments[0].click();", view_button)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    overview=soup.find_all('div',class_="d-flex align-items-center mb-3")
    project_name=overview[0].get_text()
    regdno=overview[3].get_text()
    l.append(project_name.replace('Project Name',''))
    l.append(regdno.replace('RERA Regd. No.',''))
    promoter_details=driver.find_element(By.LINK_TEXT,'Promoter Details')
    driver.execute_script("arguments[0].click();", promoter_details)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    details=soup.find_all('div',class_="col-md-6")
    promoter_name=details[0].get_text()
    address=details[5].get_text()
    gst=details[10].get_text()+details[11].get_text()
    l.append(promoter_name.replace('Company Name',''))
    l.append(address.replace('Registered Office Address',''))
    l.append(gst.replace('GST No.',''))
    data.append(l)
    driver.back()
    time.sleep(10)
    print(data)
    i=i+1
