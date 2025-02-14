import telebot
import dataframe_image as dfi
import matplotlib 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from background import keep_alive 
from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return chrome_options

class TableDay:
    def getTable():
        driver = webdriver.Chrome(options=get_chrome_options())
        try:
            driver.get('https://raspis.rggu.ru/')
            select_element = driver.find_element(By.ID, 'eduformList')
            select = Select(select_element)
            select.select_by_visible_text('1-Б-О')

            select_element = driver.find_element(By.ID, 'flowCourse')
            select = Select(select_element)
            select.select_by_visible_text('2')

            dropdown_container = driver.find_element(By.CLASS_NAME, 'custom-select__control')
            dropdown_container.click()
            input_field = driver.find_element(By.CLASS_NAME, 'custom-select__input')
            input_field.send_keys('ИИНиТБ-ФИСБ-ПИ-ПИвГС')
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ИИНиТБ-ФИСБ-ПИ-ПИвГС')]")))
                input_field.send_keys(Keys.ENTER)
            except Exception as e:
                driver.quit()
                exit()

            select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dayInterval')))
            select = Select(select_element)
            select.select_by_visible_text('На сегодня/завтра')

            driver.find_element(By.ID, 'submitButton').click()

            try:
                table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'scheduleTable')))
            except Exception as e:
                driver.quit()
                exit()

            # Wait for table data to load completely
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'td'))
            )

            # Get headers and clean them
            headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, 'th')]
            rows = table.find_elements(By.TAG_NAME, 'tr')

            data = []
            for row in rows[1:]:  # Skip header row
                cells = row.find_elements(By.TAG_NAME, 'td')
                if cells:  # Check if row has cells
                    row_data = [cell.get_attribute('innerText').strip() for cell in cells]
                    if any(row_data):  # Only add non-empty rows
                        data.append(row_data)

            if data:
                df = pd.DataFrame(data)
                if len(headers) == len(df.columns):
                    df.columns = headers
                else:
                    # Adjust columns if headers don't match
                    df.columns = [f'Column {i+1}' for i in range(len(df.columns))]
            else:
                df = None

            return df 

        finally: 
            driver.quit()

class TableWeek:
    def getTable():
        driver = webdriver.Chrome(options=get_chrome_options())
        try:
            driver.get('https://raspis.rggu.ru/')
            select_element = driver.find_element(By.ID, 'eduformList')
            select = Select(select_element)
            select.select_by_visible_text('1-Б-О')

            select_element = driver.find_element(By.ID, 'flowCourse')
            select = Select(select_element)
            select.select_by_visible_text('2')

            dropdown_container = driver.find_element(By.CLASS_NAME, 'custom-select__control')
            dropdown_container.click()
            input_field = driver.find_element(By.CLASS_NAME, 'custom-select__input')
            input_field.send_keys('ИИНиТБ-ФИСБ-ПИ-ПИвГС')
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ИИНиТБ-ФИСБ-ПИ-ПИвГС')]")))
                input_field.send_keys(Keys.ENTER)
            except Exception as e:
                driver.quit()
                exit()

            select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dayInterval')))
            select = Select(select_element)
            select.select_by_visible_text('На неделю')

            driver.find_element(By.ID, 'submitButton').click()

            try:
                table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'scheduleTable')))
            except Exception as e:
                driver.quit()
                exit()

            # Wait for table data to load completely
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'td'))
            )

            # Get headers and clean them
            headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, 'th')]
            rows = table.find_elements(By.TAG_NAME, 'tr')

            data = []
            for row in rows[1:]:  # Skip header row
                cells = row.find_elements(By.TAG_NAME, 'td')
                if cells:  # Check if row has cells
                    row_data = [cell.get_attribute('innerText').strip() for cell in cells]
                    if any(row_data):  # Only add non-empty rows
                        data.append(row_data)

            if data:
                df = pd.DataFrame(data)
                if len(headers) == len(df.columns):
                    df.columns = headers
                else:
                    # Adjust columns if headers don't match
                    df.columns = [f'Column {i+1}' for i in range(len(df.columns))]
            else:
                df = None

            return df 

        finally: 
            driver.quit()

class TableMonth:
    def getTable():
        driver = webdriver.Chrome(options=get_chrome_options())
        try:
            driver.get('https://raspis.rggu.ru/')
            select_element = driver.find_element(By.ID, 'eduformList')
            select = Select(select_element)
            select.select_by_visible_text('1-Б-О')

            select_element = driver.find_element(By.ID, 'flowCourse')
            select = Select(select_element)
            select.select_by_visible_text('2')

            dropdown_container = driver.find_element(By.CLASS_NAME, 'custom-select__control')
            dropdown_container.click()
            input_field = driver.find_element(By.CLASS_NAME, 'custom-select__input')
            input_field.send_keys('ИИНиТБ-ФИСБ-ПИ-ПИвГС')
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ИИНиТБ-ФИСБ-ПИ-ПИвГС')]")))
                input_field.send_keys(Keys.ENTER)
            except Exception as e:
                driver.quit()
                exit()

            select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dayInterval')))
            select = Select(select_element)
            select.select_by_visible_text('На месяц')

            driver.find_element(By.ID, 'submitButton').click()

            try:
                table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'scheduleTable')))
            except Exception as e:
                driver.quit()
                exit()

            # Wait for table data to load completely
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'td'))
            )

            # Get headers and clean them
            headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, 'th')]
            rows = table.find_elements(By.TAG_NAME, 'tr')

            data = []
            for row in rows[1:]:  # Skip header row
                cells = row.find_elements(By.TAG_NAME, 'td')
                if cells:  # Check if row has cells
                    row_data = [cell.get_attribute('innerText').strip() for cell in cells]
                    if any(row_data):  # Only add non-empty rows
                        data.append(row_data)

            if data:
                df = pd.DataFrame(data)
                if len(headers) == len(df.columns):
                    df.columns = headers
                else:
                    # Adjust columns if headers don't match
                    df.columns = [f'Column {i+1}' for i in range(len(df.columns))]
            else:
                df = None

            return df 

        finally: 
            driver.quit()

token = '8003363352:AAHobZKDZjhzDDIELmLqUWa5ZzpkiTs1VeE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    users = load_users()
    users.add(message.chat.id)
    save_users(users)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tomorrow = telebot.types.KeyboardButton('На завтра')
    week = telebot.types.KeyboardButton('На неделю')
    month = telebot.types.KeyboardButton('На месяц')
    markup.add(tomorrow, week, month)
    bot.send_message(message.chat.id, "Выберите срок:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'На завтра')
def get_tomorrow_schedule(message):
    try:
        df = TableDay.getTable()
        image_path = 'df.png'
        dfi.export(df, image_path, table_conversion='matplotlib')
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

@bot.message_handler(func=lambda message: message.text == 'На неделю')
def get_week_schedule(message):
    try:
        df = TableWeek.getTable()
        image_path = 'df.png'
        dfi.export(df, image_path, table_conversion='matplotlib')
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

@bot.message_handler(func=lambda message: message.text == 'На месяц')
def get_month_schedule(message):
    try:
        df = TableMonth.getTable() 
        image_path = 'df.png'
        dfi.export(df, image_path, table_conversion='matplotlib')
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

import json
import os
from datetime import datetime
import time

def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return set(json.load(f))
    return set()

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(list(users), f)

def send_daily_schedule():
    try:
        df = TableDay.getTable()
        image_path = 'df.png'
        dfi.export(df, image_path, table_conversion='matplotlib')
        users = load_users()
        with open(image_path, 'rb') as photo:
            for user_id in users:
                try:
                    bot.send_photo(user_id, photo)
                except Exception as e:
                    print(f"Failed to send to user {user_id}: {e}")
    except Exception as e:
        print(f"Error sending schedule: {e}")

def check_time():
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute == 0:  # 8 PM
            send_daily_schedule()
            time.sleep(60)  # Wait a minute to avoid multiple sends
        time.sleep(30)  # Check every 30 seconds

from threading import Thread
time_thread = Thread(target=check_time)
time_thread.daemon = True
time_thread.start()

keep_alive()
bot.infinity_polling()