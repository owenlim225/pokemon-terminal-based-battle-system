from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extract_google_form_questions(form_url):
    # Create a Service object with the path to the WebDriver
    service = Service(executable_path="./chromedriver.exe")  # Assuming chromedriver is in the same folder

    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)

    try:
        # Open the Google Form URL
        driver.get(form_url)

        # Use WebDriverWait to ensure the page is fully loaded before finding elements
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.freebirdFormviewerComponentsQuestionBaseTitle')))
        
        # Find all question elements
        questions = driver.find_elements(By.CSS_SELECTOR, '.freebirdFormviewerComponentsQuestionBaseTitle')

        # Debugging output: Check how many questions were found
        print(f"Number of questions found: {len(questions)}")

        # If no questions found, print a message
        if not questions:
            print("No questions found or the form content might be loaded differently.")
            return

        # Open a text file to save the questions
        with open('google_form_questions.txt', 'w') as file:
            for i, question in enumerate(questions, 1):
                question_text = question.text.strip()
                file.write(f"{i}. {question_text}\n")
        
        # Success message
        print("Questions have been extracted and saved to google_form_questions.txt")

    except Exception as e:
        # Print any errors that occur during execution
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# URL of the Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdgMFGgnuUMImXMCjFjaNYeAg17y8YpdJd3EONNMqq82CT6Kw/viewform?usp=sf_link'
extract_google_form_questions(form_url)
