param = input()

def main(param):
    #from janome.tokenizer import Tokenizer
    #t = Tokenizer()
    #print(param2)
    def search(param):
        param2 = '"' + param + '":'
        gokan_sentence_list = []
        with open('gokan_dict.tsv', encoding = 'utf-8')as f:
            for line in f:
                #print(line)
                if param2 in line:
                    _,line = line.split(param2)
                    gokan_sentence_list = line.split('\t')
                    break
        if gokan_sentence_list == []:
            return []
        return gokan_sentence_list


    gokan_sentence_list = search(param)
    #print(gokan_dict)          
    from dictionary import make_synonym_dict
    synonym_dict = {}
    synonym_dict=make_synonym_dict(param)
    print(synonym_dict)
    for synonym in synonym_dict[param]:
            print(synonym)
            gokan_sentence_list += search(synonym)
            #if gokan_dict.get(synonym):
    for sentence in gokan_sentence_list:
                    print(sentence)
            
            
main(param)