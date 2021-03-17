import requests
import xml.etree.ElementTree as ET


def getSugList(keyword):
    url = "http://suggestqueries.google.com/complete/search?output=toolbar&q=" + keyword
    req = requests.get(url)

    # print(req.text)
    root = ET.fromstring(req.text)

    sug_word_list = []

    for sug_word in root.iter('suggestion'):
        sug_word_list.append(sug_word.get('data'))

    # print(sug_word_list)
    return sug_word_list



# print(getSugList("이재명"))


