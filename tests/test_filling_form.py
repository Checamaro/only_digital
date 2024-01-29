import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.projects_brief_page import BriefPage



@allure.description("Test filling form")
def test_filling_in_form():

    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    g = Service('C:\\Users\\checa\\PycharmProjects\\pythonProject\\only_digital\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    form = BriefPage(driver)
    form.form_filling()

    print("Test Finished")
    driver.quit()



