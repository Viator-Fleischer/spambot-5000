import os
import time
import random
from multiprocessing import Process, Value
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# Initialize global variables for profiles and processes
profiles = []
line_numbers = []
processes = []

def interact_with_chat(profile_name, url, lines_file, line_number, flag_value, profile_path):
    # Path to the user data directory for the profile
    profile_path = os.path.join(profile_path, profile_name)

    # Create the profile directory if it doesn't exist
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)

    # Configure Chrome options for the profile
    options = uc.ChromeOptions()
    options.add_argument(f'--user-data-dir={profile_path}')

    # Create undetected_chromedriver instance with the options
    driver = uc.Chrome(options=options)

    # Change the target website to the specified YouTube URL
    driver.get(url)

    # Wait for the chat input field to be visible
    time.sleep(5)

    # Wait for the chat iframe to be present
    iframe_xpath = "//iframe[contains(@src, 'live_chat')]"
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
    driver.switch_to.frame(iframe)

    # Begin the comment posting process
    while True:
        with open(lines_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        while flag_value.value == 1:
            # Select a random line from the text file
            chat_message = random.choice(lines).strip()

            # Locate the chat input field and submit the chat message
            chat_input = driver.find_element(By.CSS_SELECTOR, "div.style-scope.yt-live-chat-text-input-field-renderer[contenteditable='']")
            chat_input.send_keys(chat_message)
            chat_input.send_keys(Keys.ENTER)

            # Sleep for 0.5 seconds before posting the next comment
            time.sleep(3)

            # Scroll the chat box to ensure the sent message is visible
            chat_box = driver.find_element(By.CSS_SELECTOR, "div#items.style-scope.yt-live-chat-item-list-renderer")
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", chat_box)

        # If flag is 0, pause for 1 second before checking the flag again
        time.sleep(1)

    # Close the browser when exiting the loop
    driver.quit()

def open_browsers(num_browsers, url, lines_file, flag_value, profile_path):
    global profiles, line_numbers, processes

    # Clear the existing processes and profiles
    profiles.clear()
    line_numbers.clear()
    processes.clear()

    # Create separate processes for each profile
    for i in range(num_browsers):
        profile_name = f"profile{i+1}"
        profiles.append(profile_name)
        line_numbers.append(i+1)

        process = Process(target=interact_with_chat, args=(profile_name, url, lines_file, i+1, flag_value, profile_path))
        process.start()
        processes.append(process)
        time.sleep(random.uniform(1, 3))  # Add a random delay between launching processes

def start_comments(flag_value):
    flag_value.value = 1

def stop_comments(flag_value):
    flag_value.value = 0

if __name__ == '__main__':
    # Specify the path for the profiles
    profile_path = r"/home/MorGoth/Asiakirjat/bot-attack"

    # Create the start switch button window
    root = tk.Tk()
    root.title("Start Switch")

    # Entry for URL
    url_label = tk.Label(root, text="Website URL:")
    url_label.pack()
    url_entry = tk.Entry(root)
    url_entry.pack()

    # Entry for the number of browsers
    num_browsers_label = tk.Label(root, text="Number of Browsers:")
    num_browsers_label.pack()
    num_browsers_entry = tk.Entry(root)
    num_browsers_entry.pack()

    # Entry for lines.txt path
    lines_label = tk.Label(root, text="lines.txt Path:")
    lines_label.pack()
    lines_entry = tk.Entry(root)
    lines_entry.pack()

    # Create a shared Value to communicate between Tkinter and browser processes
    flag_value = Value('i', 0)

    open_button = tk.Button(root, text="Open Browsers",
                            command=lambda: open_browsers(int(num_browsers_entry.get()), url_entry.get(), lines_entry.get(), flag_value, profile_path))
    open_button.pack()

    start_button = tk.Button(root, text="Start Posting", command=lambda: start_comments(flag_value))
    start_button.pack()

    stop_button = tk.Button(root, text="Stop Posting", command=lambda: stop_comments(flag_value))
    stop_button.pack()

    # Set the window size and start the Tkinter event loop
    root.geometry("400x300")
    root.mainloop()

    # Signal the browser processes to stop and wait for them to complete
    for process in processes:
        process.join()

    print("All processes completed. Exiting.")
