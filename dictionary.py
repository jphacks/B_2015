import requests
from bs4 import BeautifulSoup


def make_synonym_dict(word):
    #word = input()
    synonym_dict={word:[]}
    url = "https://thesaurus.weblio.jp/content/" + word
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
    r = requests.get(url)
    html = r.text
    bs = BeautifulSoup(html, 'html.parser')
    try:
        synonyms_table = bs.find_all("td" ,class_="nwntsR")
        #synonyms_table = bs.find_all("div" ,class_="Nwnts")
        for synonyms in synonyms_table:
            synonyms = synonyms.find_all("li")#class_='crosslink')
            #meanings = bs.select_one("#main > div:nth-of-type(13) > div > div.Nwnts > table > tbody > tr:nth-of-type(2) > td.nwntsR > ul > li:nth-of-type(1) > a").text
            for synonym in synonyms:
                if synonym.find(class_='crosslink')!=None:
                    synonym = synonym.find(class_='crosslink')
                synonym_dict[word] += synonym.contents
        #print(synonym_dict)
        return synonym_dict
    except AttributeError:
        meanings = "そのような言葉は見つからなかったよ...。ごめんね。"
        print(meanings)
        return {}
        
    
synonym_dict={}  
synonym_dict = make_synonym_dict("ぬこ")
synonym_dict
