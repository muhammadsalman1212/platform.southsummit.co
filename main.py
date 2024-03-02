import time
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver

scroll_times = int(input("[info] How many times do you want to scroll down? "))
delete_old_csv_data = input("[info] Do you want to delete old data from csv file? (yes/no) ")

driver = webdriver.Chrome()

driver.get("https://platform.southsummit.co/event/south-summit-2023/people/RXZlbnRWaWV3XzM4MjQ2NQ==")

driver.maximize_window()
time.sleep(12)
# accept_cookies_button = driver.find_element(By.XPATH, '//div[@class="sc-368b1b9f-5 lcigLb"]//button[@class="sc-b6a6c59b-0 lcuvrR" and @type="button"]')

accept_cookies_button = driver.find_element(By.XPATH, '//span[text()="Accept all"]')
time.sleep(5)
accept_cookies_button.click()



def scroll_page():
    # Scroll down
    driver.execute_script("window.scrollBy(0, 500)")

# Scroll
for _ in range(scroll_times):
    scroll_page()
    time.sleep(4)

time.sleep(8)

selector = "div.sc-a9938169-1 a"


header = ["Link"]

all_links_list = []

links = driver.find_elements(By.XPATH, '//div[@class="sc-a9938169-1 eweHCo"]//a')


for link in links:
    link_href = link.get_attribute('href')
    all_links_list.append(link_href)

print(all_links_list)

unique_urls = {}
for url in all_links_list:
    base_url = url.split('?')[0]
    unique_urls[base_url] = url

unique_list = list(unique_urls.values())

print(unique_list)

def converting_links_to_csv():
    with open('unique_urls.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)

        for url in unique_list:
            writer.writerow([url])

    print("Unique URLs have been saved to unique_urls.csv")
converting_links_to_csv()

try:
    def delete_old_data(delete_old_csv_data):
            with open('all_profiles_details.csv', 'r', encoding='utf-8') as file:
                first_line = file.readline()
                if not first_line:
                    print("There's no data in the CSV file.")
                    return

            if delete_old_csv_data.lower() == 'yes':
                with open('all_profiles_details.csv', 'w', encoding='utf-8') as file:
                    file.truncate()

                print("All data deleted from the CSV file.")
            else:
                print("No data deleted from the CSV file.")

    delete_old_data(delete_old_csv_data)
except:
    pass
    print("i can't delete data because there was no data in the csv file")
#------------------------------------------------------------------------------------------

csv_file = "all_profiles_details.csv"


def getting_profiles_info():
    try:

            for link in unique_list:
                driver.get(link)
                driver.refresh()
                time.sleep(4)
                try:
                    name = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[2]/div/div[2]/h2')

                    about_element = driver.find_element(By.XPATH,'//div[@class="sc-8cd680a3-3 iEQrrQ"]')

                    types_of_speaking = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[2]/div/div[8]/div[2]//div[@class="sc-d94c44f6-2 hMdzYj"]')

                    working_in = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[2]/div/div[9]/div[2]/div')

                    # job_title = driver.find_element(By.XPATH, '//span[@class="chip__Wrapper-ui__sc-st9ik3-0 gqwogJ"]')
                    job_title = driver.find_element(By.XPATH, '//div[@class="sc-2fd75577-1 lgCAuc"]')



                    country = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[2]/div/div[11]/div[2]/div')

                    industry = driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div/div[2]/div/div[12]/div[2]/div/div')
#
                    social_medias = driver.find_elements(By.XPATH,
                                                         '//div[@class="sc-9c9868a2-15 kzrhIj"]//a[@target="_blank"]')
                    for all_links in social_medias:
                        all_links_href = all_links.get_attribute('href')
                        print(all_links_href)

                    name_text = name.text
                    about_text = about_element.text
                    types_of_speaking_text = types_of_speaking.text
                    working_in_text = working_in.text
                    job_title_text = job_title.text
                    country_text = country.text
                    industry_text = industry.text
                    socialMedia = []
                    for tag in social_medias:
                        socialMedia.append(tag.get_attribute('href'))

                    header = ["Name", "link", "Types of Speaking", "Working In", "Job Title", "Country", "Industry",
                              "Social Media Links", "About"]

                    with open('all_profiles_details.csv', 'a+', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)



                        if file.tell() == 0:
                            writer.writerow(header)


                        writer.writerow([name_text, link, types_of_speaking_text, working_in_text, job_title_text, country_text, industry_text,
                                         socialMedia, about_text])



                    print(f"name: {name_text} \n about_text: {about_text} \n job_title: {job_title_text} \n types_of_speaking: {types_of_speaking_text} \n working_in: {working_in_text} \n country: {country_text} \n industry: {industry_text} \n socialMedia: {socialMedia} \n")
                    print(f"[Info] Getting speaker Name: {name_text} profile link: {link}")



                except:
                    pass

    except Exception as e:
        print(f"An error occurred: {e}")


getting_profiles_info()

driver.quit()


