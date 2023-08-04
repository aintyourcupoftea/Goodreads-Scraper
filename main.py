import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from oauth2client.service_account import ServiceAccountCredentials
import gspread

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
scopes=[
    "https://www.googleapis.com/auth/spreadsheets,"
    "https://www.googleapis.com/auth/drive"
]
CREDENTIALS=ServiceAccountCredentials.from_json_keyfile_name('auth.json')
file=gspread.authorize(credentials=CREDENTIALS)
sheet=file.open("Sadhguru Books")
sheet=sheet.sheet1

driver.get('https://www.goodreads.com/ap/signin?language=en_US&openid.assoc_handle=amzn_goodreads_web_na&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fsign-in&siteState=fbf733bf4b9fe44eeabb707d4c0156a0')
email_login=driver.find_element(By.ID,"ap_email")
email_login.send_keys()
password_login=driver.find_element(By.ID,"ap_password")
password_login.send_keys()
sign_in_button=driver.find_element(By.ID,"signInSubmit")
sign_in_button.click()
time.sleep(5)




driver.get('https://www.goodreads.com/author/list/30378.Sadhguru?page=1&per_page=30&sort=original_publication_year&utf8=%E2%9C%93')
for i in range(1, 31):
    book_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/a/span').text
    meta_data = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/div/span').text  # gets entire text of the metadata of that book
    published_index = (meta_data.find("published"))  # finds index of the word published
    year_published = meta_data[published_index + 10:published_index + 14]  # stores exact value of year
    print(book_name)
    print(year_published)
    sheet.update_acell("A" + str(i + 1), book_name)
    sheet.update_acell("B" + str(i + 1), year_published)


driver.get('https://www.goodreads.com/author/list/30378.Sadhguru?page=2&per_page=30&sort=original_publication_year&utf8=%E2%9C%93')
for i in range(1, 13):
    book_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[' + str(
        i) + ']/td[2]/a/span').text
    meta_data = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[' + str(
        i) + ']/td[2]/div/span').text  # gets entire text of the metadata of that book
    published_index = (meta_data.find("published"))  # finds index of the word published
    year_published = meta_data[published_index + 10:published_index + 14]  # stores exact value of year
    print(book_name)
    print(year_published)
    sheet.update_acell("A" + str(i + 31), book_name)
    sheet.update_acell("B" + str(i + 31), year_published)