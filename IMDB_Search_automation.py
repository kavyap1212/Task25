from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.imdb.com/search/name/")

    # Explicit wait for the input boxes to be present
    wait = WebDriverWait(driver, 10)
    
    # Fill in the name input box
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.send_keys("Barbara Rush")
    
    # Fill in the birth date input box
    birth_date_input = wait.until(EC.presence_of_element_located((By.ID, "birth_date")))
    birth_date_input.send_keys("1927-01-04")
    
    # Fill in the death date input box
    death_date_input = wait.until(EC.presence_of_element_located((By.ID, "death_date")))
    death_date_input.send_keys("2024-03-31")
    
    # Select a birth month from the drop-down menu
    birth_month_select = wait.until(EC.presence_of_element_located((By.ID, "birth_monthday")))
    birth_month_select.send_keys("January")

    # Select a profession from the drop-down menu
    profession_select = wait.until(EC.presence_of_element_located((By.ID, "professions")))
    profession_select.send_keys("Actor")
    
    # Perform the search by clicking the search button
    search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.primary")))
    search_button.click()
    
    # Print a success message
    print("Search operation was successful.")

except TimeoutException:
    print("The operation timed out. The elements were not found in time.")
except NoSuchElementException:
    print("One of the elements was not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()