from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


class Test_odev:

    def test_no_id_pw(self):
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorNoPwId = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorNoPwId.text)
        sleep(1)
    
    def test_no_pw(self):
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorNoPw = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorNoPw.text)#-->error cümlesini göstermesi için

    def test_locked_out(self):
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        sleep(1)
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)
        errorLockedOut = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorLockedOut.text)#-->error cümlesini göstermesi için

    def test_x_icon(self):
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)
        xBtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        xBtn.click()
        sleep(1)

    def test_login(self):
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        sleep(1)
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)
        print(driver.current_url)#-->inventory kısmına girdiğini göstermek için

    def test_items(self):
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        items = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"The number of items is:{len(items)}")





    
test = Test_odev()
#test.test_no_id_pw()
#test.test_no_pw()
#test.test_locked_out()
#test.test_x_icon()
#test.test_login()
#test.test_items()
#<--Hepsi de kontrol edildi-->


