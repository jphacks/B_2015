# 以下ほぼ彩花ちゃんのコピペ

"""import requests


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

url_1 = 'https://www.aozora.gr.jp/cards/000035/files/301_ruby_5915.zip'
url_2 = 'https://www.aozora.gr.jp/cards/000035/files/1565_ruby_8220.zip'
url_3 = 'https://www.aozora.gr.jp/cards/000035/files/1567_ruby_4948.zip'
url_4 = 'https://www.aozora.gr.jp/cards/000035/files/1569_ruby_18584.zip'
url_5 = 'https://www.aozora.gr.jp/cards/000035/files/270_ruby_1164.zip'
r_1 = requests.get(url_1, headers= headers)
r_2 = requests.get(url_2, headers= headers)
r_3 = requests.get(url_3, headers= headers)
r_4 = requests.get(url_4, headers= headers)
r_5 = requests.get(url_5, headers= headers)
content_1 = r_1.content
content_2 = r_2.content
content_3 = r_3.content
content_4 = r_4.content
content_5 = r_5.content


import io
import zipfile

f_1 = io.BytesIO(content_1)
f_2 = io.BytesIO(content_2)
f_3 = io.BytesIO(content_3)
f_4 = io.BytesIO(content_4)
f_5 = io.BytesIO(content_5)
zipf_1 = zipfile.ZipFile(f_1)
zipf_2 = zipfile.ZipFile(f_2)
zipf_3 = zipfile.ZipFile(f_3)
zipf_4 = zipfile.ZipFile(f_4)
zipf_5 = zipfile.ZipFile(f_5)
namelist_1 = zipf_1.namelist()
namelist_2 = zipf_2.namelist()
namelist_3 = zipf_3.namelist()
namelist_4 = zipf_4.namelist()
namelist_5 = zipf_5.namelist()
namelist_1
namelist_2
namelist_3
namelist_4
namelist_5

import re
title = ''
author = ''
def syori(text,first_sentence,last_sentence):
    #title, text = text.split('【テキスト中に現れる記号について】')
    #print(title)
    _, text = text.split(first_sentence)
    text, _ = text.split(last_sentence)
    text = first_sentence + text + last_sentence
    text = text.replace('|', '').replace(' ', '')
    text = re.sub('《\w+》', '', text)
    text = re.sub('［＃.*］','', text)
    text = text.replace('\r','').replace('\n','')
    text = re.sub('[、「」？]', '', text)
    text = re.sub('\（\w+\）', '', text)
    text = re.sub('\[\w+\]', '', text)
    text = re.sub('[ \t]+$','',text)
    text = re.sub('^[ \t]+$','',text)
    text = re.sub('^ +$','',text)
    text = re.sub('[　]+','',text)
    text = text.split('。')
    return text

#info = {}

def make_info(btext,atext):
    list = btext.splitlines()
    #print(list[0])
    #print(list[1])
    #print(btext[:10])
    #print('\n')
    #print(atext[:10])
    info={}
    for sentence in atext:
        #print(sentence)
        info[sentence]=list[:2]
    return info

print("loading......")

###########################################
data_1 = zipf_1.read(namelist_1[0])
original_text_1 = data_1.decode('Shift_JIS')
#print(original_text_1[:500])

#title, _ = original_text_1.split('【テキスト中に現れる記号について】')
#title, _ = title.split('-------------------------------------------------------')
#list = title.splitlines()
#print(list[1])


#print(text)
#sentences_1 = text.split('。')
first_sentence = '私は、その男の写真を三葉、見たことがある。'
last_sentence = '神様みたいないい子でした'
sentences_1 = syori(original_text_1,first_sentence,last_sentence)
info = make_info(original_text_1,sentences_1)
# print('文の数:', len(sentences_1))

# print(sentences_1[:10])

#print(info['私は、その男の写真を三葉、見たことがある。'])
#print(info)

###########################################
data_2 = zipf_2.read(namelist_2[0])
original_text_2 = data_2.decode('Shift_JIS')
#print(original_text[:500])



first_sentence = '朝、食堂でスウプを一さじ、すっと吸ってお母さまが、'
last_sentence = 'ぜひお聞きいれのほど願います。'

#print(text)

sentences_2 = syori(original_text_2,first_sentence,last_sentence)
# print('文の数:', len(sentences_2))
#print(type(sentences_1[0]))
# print(sentences_2[:10])
info.update(make_info(original_text_2,sentences_2))
#print(type(text))

#print(info)


##########################################

data_3 = zipf_3.read(namelist_3[0])
original_text_3 = data_3.decode('Shift_JIS')
#print(original_text[:500])



first_sentence = 'メロスは激怒した。必ず、'
last_sentence = '勇者は、ひどく赤面した。'

#print(text)


sentences_3 = syori(original_text_3,first_sentence,last_sentence)
# print('文の数:', len(sentences_3))
#print(type(sentences_1[0]))
# print(sentences_3[:10])
# print(type(sentences_3[0]))
info.update(make_info(original_text_3,sentences_3))


##########################################

data_4 = zipf_4.read(namelist_4[0])
original_text_4 = data_4.decode('Shift_JIS')
#print(original_text[:500])



first_sentence = '伊豆の南、温泉が湧き出ているというだけで、他には何一つとるところの無い、つまらぬ山村である。'
last_sentence = '何をしている事やら。'

sentences_4 = syori(original_text_4,first_sentence,last_sentence)
# print('文の数:', len(sentences_4))
#print(type(sentences_1[0]))
# print(sentences_4[:10])
#print(type(text))
info.update(make_info(original_text_4,sentences_4))

##########################################

data_5 = zipf_5.read(namelist_5[0])
original_text_5 = data_5.decode('Shift_JIS')
#print(original_text[:500])



first_sentence = '富士の頂角、広重《ひろしげ》の富士は八十五度、文晁《ぶんてう》の富士も八十四度くらゐ、'
last_sentence = '酸漿《ほほづき》に似てゐた。'

#print(text)
sentences_5 = syori(original_text_5,first_sentence,last_sentence)
# print('文の数:', len(sentences_5))
#print(type(sentences_1[0]))
# print(sentences_5[:10])
#print(type(text))
sentences_list = [sentences_1,sentences_2,sentences_3,sentences_4,sentences_5]
# print(type(sentences_list))
info.update(make_info(original_text_5,sentences_5))


####################################################################


#ここは関数化しない方がいいのかな... viewsよくわからん
from janome.tokenizer import Tokenizer
BEGIN = '__BEGIN__'
END = '__END__'

#after_list = []

t = Tokenizer()

gokan_dict={}
for sentences in sentences_list:
    for sentence in sentences:
        for gokan in [token.base_form for token in t.tokenize(sentence)]:
            if gokan_dict.get(gokan)==None:
                gokan_dict[gokan]=[sentence]
            else:
                gokan_dict[gokan].append(sentence)

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RETURN = '\033[07m' #反転
    ACCENT = '\033[01m' #強調
    FLASH = '\033[05m' #点滅
    RED_FLASH = '\033[05;41m' #赤背景+点滅
    END = '\033[0m'


import os
import csv


def search(param):
    # param = input()
    from dictionary import make_synonym_dict
    synonym_dict = {}
    synonym_dict=make_synonym_dict(param)
    datas = []
    for synonym in synonym_dict[param]:
        if gokan_dict.get(synonym):
            for sentence in gokan_dict[synonym]:
                words=t.tokenize(sentence)
                words=list(words)
                #b=False
                #text1 = ""

                #text2 = ""
                for word in words:
                    if word.base_form==synonym:
                        #b=True
                        param2=word.surface
                        text_list = sentence.split(word.surface)
                        break
                datas.append(text_list[0]+param2+text_list[1]+':'+info[sentence][0]+','+info[sentence][1])
                # 色付き datas.append(text_list[0]+pycolor.BLUE+param2+pycolor.END+text_list[1]+':'+info[sentence][0]+','+info[sentence][1])
                # print(text_list[0]+pycolor.BLUE+param2+pycolor.END+text_list[1]+':'+info[sentence][0]+','+info[sentence][1])
    with open(os.getcwd()+'/polls/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n,')
        writer.writerow(datas)
        # writer.writerow("DONE")"""
import os
import csv
#from dictionary import make_synonym_dict
def search(param):
        #from janome.tokenizer import Tokenizer
    #t = Tokenizer()
    #print(param2)
    print("search:")
    print(param)
    def flatten(nested_list):
        """2重のリストをフラットにする関数"""
        return [e for inner_list in nested_list for e in inner_list]

    def search2(param):
        param2 = '"' + param + '":'
        gokan_sentence_list = []
        print(os.getcwd())
        with open(os.getcwd()+'/sitm.pythonanywhere.com/polls/application/'+'akutagawa_gokan_dict.tsv', encoding = 'utf-8')as f:
            print("開けた！")
            for line in f:
                #print(line)
                if param2 in line:
                    _,line = line.split(param2)
                    gokan_sentence_list = line.split('\t')
                    break
        print(gokan_sentence_list)
        print("aaa")
        return flatten(gokan_sentence_list)


    gokan_sentence_list = search2(param)
    #print(gokan_dict)
    
    synonym_dict = {}
    #synonym_dict=make_synonym_dict(param)
    #print(synonym_dict)
    with open(os.getcwd()+'/sitm.pythonanywhere.com/polls/application/'+'akutagawa_synonym_dict.tsv', encoding = 'utf-8')as f:
            param2 = '"'+param+'":'
            for line in f:
                if param2 in line:
                    _,line = line.split(param2)
                    synonym_dict[param] = line.split('\t')

    
    for synonym in synonym_dict[param]:
            #print(synonym)
        gokan_sentence_list += search2(synonym)
            #if gokan_dict.get(synonym):
    #for sentence in gokan_sentence_list:
    with open(os.getcwd()+'/sitm.pythonanywhere.com/polls/application/'+'data.csv','a') as f:
        for sentence in flatten(gokan_sentence_list):
            f.write(sentence + '::::::::::')
            #writer.writerow(gokan_sentence_list)
        # writer.writerow("DONE")"""




# 以下を追記(return_text()を呼び出すと"Hello!!"が返される)
def return_text():
    #return "Hello!"
    
    with open(os.getcwd()+'/sitm.pythonanywhere.com/polls/application/'+'data.csv') as f:
        reader = csv.reader(f, lineterminator='\n,')
        datas = []
        for row in reader:
            # print(row)
            datas.append(row)
    os.remove(os.getcwd()+'/sitm.pythonanywhere.com/polls/application/'+'data.csv')
    return datas


    """
    with open(os.getcwd()+'/polls/application/'+'data.csv','a') as f:
        reader = csv.reader(f, lineterminator='\n')
        datas = []
        for row in reader:
            datas.append(row)
    return datas
    """

"""
テスト用
# coding:utf-8

import os
import csv

# htmlからのデータをcsvファイルに記録
def search(data):
    print("dataだよ")
    datas = [data]
    with open(os.getcwd()+'/polls/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(datas)
"""