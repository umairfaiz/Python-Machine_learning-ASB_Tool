import re
import enchant
from builtins import input, print
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag


class LanguageProcessing(object):
    def __init__(self):
        self.clean_dataset()

    def tokeniz(self, line):

        # filename = open("history1.csv", "r")
        tokens = []
        #for line in file_name.readlines():
            #line = line.decode('ASCII', 'ignore')
            # line = line.lower()  # converting words to lower case
            #print("tokenized :",line)
        tokens = word_tokenize(line)
        #print("tokens :", tokens)
        return tokens
        # self.clean_URL(tokens)
        # filename.close()

    def clean_URL(self, f):  # need to call this method in tokenize
        cleanedurl = []
        for line in f:
            line = line.lower()
            #line = line.decode('utf-8', 'ignore')
            line = line.replace('+', ' ').replace('.', ' ').replace('=', ' ').replace('-', ' ').replace('/',
                                                                                                        ' ').replace(
                '//', ' ').replace(',', ' ').replace('www', ' ').replace('https', ' ').replace('http', ' ').replace(':', ' ').replace('\'', ' ')
            line = re.sub("(^|\W)\d+($|\W)", '', line) #removing other chararcters
            line = line.strip(' ')
            # self.remove_stopwords(line)
            cleanedurl.append(line)
        new_line = filter(lambda x: len(x) > 1, cleanedurl)  # removing the spaces from text
        # return cleanedurl
        return new_line
        # self.remove_non_englishwords(new_line)

    def remove_non_englishwords(self, w):
        d = enchant.Dict("en_US")
        string = " ".join(w)
        english_words = []
        for word in string.split():
            if d.check(word):
                if len(word) > 1:  # checks with Enchant library to give a bool value
                    english_words.append(word)
        return english_words
        #self.remove_stopwords(english_words)

    def remove_stopwords(self, words):  # here "words" is tokenized array
        stop_words = set(stopwords.words("english"))
        stop_words.update(('chromes','search', 'web','website', 'websites','com', 'searched','mega'))
        filered_words = []
        for word in words:
            if word not in stop_words:  # "len(words)<2" removes fullstops & other characters
                filered_words.append(word)
        return filered_words

    def lemmatizing(self, words):
        lemmatizer = WordNetLemmatizer()
        # l_words = map(lemmatizer.lemmatize(words))
        l_words = list(map(lemmatizer.lemmatize, words))
        return l_words

    def stemming(self, words):  # here "words" is a tokenized array
        stemmer = PorterStemmer()
        for w in words:
            stemmer.stem(w)

    def pos_tagging(self, words):
        tagged_words = pos_tag(words)

    def penn_to_wordnet(treebank_tag):

        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return ''

    def avoid_blank_lines(self,file):

        line = file.rstrip()
        if line:
            yield line

    def remove_similar_words(self,sent):

        # original_set = set()
        # result = []
        # for item in sent:
        #     if item not in original_set:
        #         original_set.add(item)
        #         result.append(item)
        # return result
        last = ""
        result = []
        for item in sent:
            if item != last:
                last = item
                result.append(item)
        #print(result)
        return result

    def clean_dataset(self):#limitLogHistory_log
        input_file = open('limitLogHistory_log.txt', 'rt', encoding='utf-8')
        output_file = open('outputfile.txt', 'w', encoding='utf-8')
        #l_p = LanguageProcessing()
        #sentences=[]
        for lines in input_file.readlines():
            #print(lines)
            tokeniz = self.tokeniz(lines)
            cleaned_url = self.clean_URL(tokeniz)
            remove_words = self.remove_non_englishwords(cleaned_url)
            stopwords_removed1 = self.clean_URL(remove_words)
            stopwords_removed = self.remove_stopwords(stopwords_removed1)

            # print(stopwords_removed)
            if stopwords_removed==[]:
                continue
            else:
                new_sentence=self.remove_similar_words(stopwords_removed)
                cleaned_sentence=' '.join(str(s) for s in new_sentence)+"\n"
                # print(new_sentence)
            #sentences.append(cleaned_sentence)
            output_file.writelines(cleaned_sentence)
        input_file.close()
        output_file.close()

# def main():
#     l_p = LanguageProcessing()
#     l_p.clean_dataset()
#
# main()
