import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plot

def get_txt(URL, headers):
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    for points in soup:
        li.append(points)
    
    file = open("repos.txt", "w+")
    
    for line in li:
        file.write(line)
    
    file.close()


if __name__ == "__main__":
    username = input("Whose stats do you want to know about? (Case-sensitive) \n")
    userAgent = input("Please enter your device's user agent (can be found by googling 'my user agent'): ")
    URL = "https://api.github.com/users/" + username + "/repos"
    headers = {"User-Agent": userAgent}
    li = []

    get_txt(URL, headers)

    langs = []
    userLang = []
    
    with open("repos.txt") as file:
        for line in file.readlines():
            if '"language":' in line:
                langs.append(line)

    for i in langs:
        a = i.strip('    "language": "')
        b = a.strip('",\n')
        userLang.append(b)

    diffLangs = []
    dict = {}
    
    for lang in userLang:
        if lang not in diffLangs:
            diffLangs.append(lang)
            dict[lang] = 1

        else:
            dict[lang] += 1
    
    if "" in dict:
        del dict['']
    
    languages = []
    values = []
    colors = ['r', 'y', 'g', 'b']
    explode = []
    
    for i in range(len(dict)):
        explode.append(0.1)
    
    for i in dict:
        languages.append(i)
        values.append(dict[i])

    plot.pie(values, labels = languages, colors=colors,  
        startangle=90, shadow = True, explode = explode, 
        radius = 1.2, autopct = '%1.1f%%')

    plot.legend()
    plot.show()

    