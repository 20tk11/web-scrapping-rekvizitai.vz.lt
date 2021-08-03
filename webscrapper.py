from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Data:
    def __init__(self, code, emp, sal, inc):
        self.CompanyCode = code
        self.Employees = emp
        self.AvgSalary = sal
        self.SellingIncome = inc

    def display(self):
        print("Įmonės kodas: " + self.CompanyCode)
        print("Darbuotojai: " + self.Employees)
        print("Vidutinis atlyginimas: " + self.AvgSalary)
        print("Pardavimo pajamos: " + self.SellingIncome)

driver = webdriver.Chrome()
driver.get('https://rekvizitai.vz.lt/')
searchbox = driver.find_element_by_xpath('//*[@id="code"]')
searchbox.send_keys('300086828')
searchbutton = driver.find_element_by_xpath('//*[@id="ok"]')
searchbutton.click()
searchbutton2 = driver.find_element_by_xpath('//*[@id="leftContainer"]/div[1]/div/div[3]/div[2]/a[1]')
searchbutton2.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "info"))
    )
    #print(element.text)
    rows = element.find_elements_by_tag_name("tr")
    value1 = ""
    value2 = ""
    value3 = ""
    value4 = ""
    for x in range(len(rows)):
        columns = rows[x].find_elements_by_tag_name("td")
        #print(x)
        #print(columns[1].text)
        #print(columns[2].text)

        if(columns[1].text == "Įmonės kodas"):
            value1 = columns[2].text
        if(columns[1].text == "Darbuotojai"):
            value2 = columns[2].text
        
        if(columns[1].text == "Vidutinis atlyginimas"):
            value3 = columns[2].text
        
        if(columns[1].text == "Pardavimo pajamos"):
            value4 = columns[2].text
    h1 = Data(value1, value2, value3, value4)
    h1.display()
finally:
    driver.quit()


#element = driver.find_element_by_class_name('info')


