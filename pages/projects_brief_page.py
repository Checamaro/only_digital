import os.path
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class BriefPage(Base):

    url = 'https://only.digital/projects#brief'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_word = "//form[1]/div[1]/p[1]"
    user_name = "//div[1]/div[1]/div[1]/input[1]"
    email = "//div[2]/div[1]/input[1]"
    country_code_drop = "//div[1]/div[1]/div[1]/div[1]/div[2]"
    code_russia = "//li[1]/span[1]"
    phone_number = "//div[3]/div[1]/div[1]/input[1]"
    company = "//div[4]/div[1]/input[1]"
    project_site_button = "//div[2]/div[1]/label[2]/span[1]"
    about_field = "//div[2]/textarea[1]"
    attach_button = "//div[2]/div[1]/div[2]/form[1]/div[2]/div[3]/div[2]/div[1]/label[1]/span[1]"
    budget_button = "//div[3]/div[1]/label[2]/span[1]"
    info_button = "//div[4]/div[1]/label[3]/span[1]"

    # Getters

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_country_code_drop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country_code_drop)))

    def get_code_russia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code_russia)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_company(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.company)))

    def get_project_site_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.project_site_button)))

    def get_about_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_field)))

    def get_attach_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attach_button)))

    def get_budget_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.budget_button)))

    def get_info_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.info_button)))



    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_phone_number(self, phone_number):
        self.get_country_code_drop().click()
        self.get_code_russia().click()
        self.get_phone_number().send_keys(phone_number)
        print("Input phone_number")

    def input_company(self, company):
        self.get_company().send_keys(company)
        print("Input company")

    def click_project_site_button(self):
        self.get_project_site_button().click()
        print("Click 'project: site' button")

    def input_about_field(self, about_field):
        self.get_about_field().send_keys(about_field)
        print("Input about project info")

    def attach_file(self, file_name):
        file_path = os.path.abspath(os.path.join("attachments", file_name))
        file_input = self.get_attach_button()
        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", file_input, file_path)

    def click_budget_button(self):
        self.get_budget_button().click()
        print("Click budget button")

    def click_info_button(self):
        self.get_info_button().click()
        print("Click budget button")

    # Methods

    def form_filling(self):
        with allure.step("Form filling"):
            Logger.add_start_step(method="form_filling")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.assert_url("https://only.digital/projects#brief")
            self.assert_word(self.get_main_word(), 'Ваши контакты')
            self.input_user_name("Поликарп")
            self.input_email("788test567@gmail.com")
            self.input_phone_number("9123456789")
            self.input_company("Рога и копыта")
            self.click_project_site_button()
            self.input_about_field("Заготовка рогов и копыт")
            self.attach_file("card kirill.png")
            self.get_screenshot()
            self.click_budget_button()
            self.click_info_button()
            Logger.add_end_step(url=self.driver.current_url, method="form_filling")