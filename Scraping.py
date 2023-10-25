from bs4 import BeautifulSoup
import requests
import time

print("Enter Skill you are not familiar with:")
unfamiliar_skill = input(">")
print(f"filtering out {unfamiliar_skill}")


def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_contents = requests.get(url).text
    soup = BeautifulSoup(html_contents, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        # company_name = job.h3.text.replace(' ', '')
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
        post_date = job.find('span', class_='sim-posted').text.strip()
        more_info = job.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name}")
            print(f"Required Skills: {skills}")
            print(f"Date Posted: {post_date}")
            print(f"More Info: {more_info}")
            print("*****************************")
        else:
            print(f"All jobs available includes {unfamiliar_skill}")
            break


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
