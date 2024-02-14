from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.oca.ac.jp/course/'
response = request.urlopen(url)
soup = BeautifulSoup(response,  'html.parser')

item = soup.find("div", class_="p-course_list -c2024")
courses = item.find_all("div", class_="p-course_list__block")

for course in courses:
    # print(course.select("div.name")[0].text)
    subjects = course.find_all("a", class_="js-hover")

    for subject in subjects:
        print(subject.text)
response.close()