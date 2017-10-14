from builtins import print
import itertools
import nltk
import random
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from nltk import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.metrics import precision
import collections
from nltk.metrics import recall
from nltk.metrics import f_measure
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


class SaveBigramsClassifier(object):
    def __init__(self):
        self.saveClassifier()

    def remove_duplicates(self, numbers):
        numbers.sort()
        i = len(numbers) - 1
        while i > 0:
            if numbers[i] == numbers[i - 1]:
                numbers.pop(i)
            i -= 1
        return numbers

    def balance_pos_class(self, pos_list, neg_list):
        new_mix = list(set(pos_list).intersection(set(neg_list)))  # gets only the common words between two classes

        for item in new_mix:
            for pos_i in pos_list:
                if item in pos_list:
                    pos_list.remove(item)
                    pos_list = self.remove_duplicates(pos_list)
        return pos_list

    def balance_neg_class(self, pos_list, neg_list):
        new_mix = list(set(neg_list).intersection(set(pos_list)))  # gets only the common words between two classes

        for item in new_mix:
            for neg_i in neg_list:
                if item in neg_list:
                    neg_list.remove(item)
                    neg_list = self.remove_duplicates(neg_list)
        return neg_list

    # def find_features(self, document):
    #     words = word_tokenize(document)
    #     features = {}
    #     for w in self.word_features:
    #         features[w] = (w in words)
    #     # print("Features: ",features)
    #
    #     return features

    def bi_features(self, sentence):
        try:
            tokens = nltk.word_tokenize(sentence)
            bigram_finder = BigramCollocationFinder.from_words(tokens)
            bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 200)
            return dict([(str(ngram).lower(), True) for ngram in itertools.chain(tokens, bigrams)])
        except ZeroDivisionError:
            pass


    def saveClassifier(self):
        short_pos = open("positive4.txt", "r").read()
        short_neg = open("negative4.txt", "r").read()

        pos_documents = []
        neg_documents = []
        all_words = []
        allowed_word_types = ["J", "N", "V"]  # J-Adjectives, N-nouns, V-Verb, R-Adverb

        for p in short_pos.split('\n'):
            pos_documents.append((p, "pos"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in allowed_word_types:
                    all_words.append(w[0].lower())

        for p in short_neg.split('\n'):
            neg_documents.append((p, "neg"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in allowed_word_types:
                    all_words.append(w[0].lower())

        short_pos_words = word_tokenize(short_pos)
        short_neg_words = word_tokenize(short_neg)

        balanced_pos_words = self.balance_pos_class(short_pos_words, short_neg_words)
        balanced_neg_words = self.balance_neg_class(short_pos_words, short_neg_words)

        for w in balanced_pos_words:
            all_words.append(w.lower())

        for w in balanced_neg_words:
            all_words.append(w.lower())

        save_all_words=open("pickle_saves/all_words","wb")
        pickle.dump(all_words,save_all_words)
        save_all_words.close()

        all_words = nltk.FreqDist(all_words)

        pos_bigramfeaturesets = [(self.bi_features(rev), category) for (rev, category) in pos_documents]  # 935
        neg_bigramfeaturesets = [(self.bi_features(rev), category) for (rev, category) in neg_documents]  # 909

        pos_featuresets = [i for i in pos_bigramfeaturesets[:909] if
                           i[0] != None]  # Removing None from sntences which does not have any bigrams
        neg_featuresets = [i for i in neg_bigramfeaturesets if i[0] != None]


        bigram_featuresets = pos_featuresets + neg_featuresets

        save_bigram_featuresets = open("pickle_saves/bigram_featuresets", "wb")
        pickle.dump(bigram_featuresets, save_bigram_featuresets)
        save_bigram_featuresets.close()

        featuresets = bigram_featuresets

        random.shuffle(featuresets)

        print(len(all_words))
        print(len(featuresets))
        print("pos_featuresets", len(pos_featuresets))
        print("neg_featuresets", len(neg_featuresets))

        training_set = featuresets[:1620]
        testing_set = featuresets[1620:]

        print(len(featuresets))

        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(training_set)
        print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

        save_MNB_classifier = open("pickle_saves/MNB_classifier", "wb")
        pickle.dump(MNB_classifier, save_MNB_classifier)
        save_MNB_classifier.close()


        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(training_set)
        print("SGDClassifier_classifier accuracy percent:",
              (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

        save_SGDClassifier_classifier = open("pickle_saves/SGDClassifier_classifier", "wb")
        pickle.dump(SGDClassifier_classifier, save_SGDClassifier_classifier)
        save_SGDClassifier_classifier.close()

        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(training_set)
        print("LinearSVC_classifier accuracy percent:",
              (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

        save_LinearSVC_classifier = open("pickle_saves/LinearSVC_classifier", "wb")
        pickle.dump(LinearSVC_classifier, save_LinearSVC_classifier)
        save_LinearSVC_classifier.close()

        voted_classifier = VoteClassifier(LinearSVC_classifier, MNB_classifier, SGDClassifier_classifier)

        src_doc = open("aMIX.txt", 'rt', encoding='utf-8').readlines()
        words = []
        user_input = None
        # doc = src_doc.read().split("\n");
        for line in src_doc:
            line = line.replace("\n", "")
            line = line.replace(".", "")
            words.append(line)
            user_input = ' '.join(str(e) for e in words)
        # print(user_input)
        # print("Predicted polarity by naive bayes: ", classifier.classify(self.bi_features(user_input)))
        print("Predicted polarity by MNB_classifier: ", MNB_classifier.classify(self.bi_features(user_input)))
        # print("Predicted polarity by MNB_classifier BIGRAMS: ", MNB_classifier.classify(self.bi_features(user_input)))
        # print("Predicted polarity by LogisticRegression_classifier : ",LogisticRegression_classifier.classify(self.bi_features(user_input)))
        print("Predicted polarity by SGDClassifier_classifier: ",
              SGDClassifier_classifier.classify(self.bi_features(user_input)))
        print("Predicted polarity by LinearSVC_classifier: ",
              LinearSVC_classifier.classify(self.bi_features(user_input)))
        # print("Predicted polarity by NuSVC_classifier: ", NuSVC_classifier.classify(self.bi_features(user_input)))

        self.finalpolarity = voted_classifier.classify(self.bi_features(user_input))
        self.finalconfidence = voted_classifier.confidence(self.bi_features(user_input)) * 100

        print("Voted classifier accuracy (%):", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)
        print("Classification:", self.finalpolarity,
              "Confidence %:", self.finalconfidence)

        # Precison and recall calculations
        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)

        for i, (feats, label) in enumerate(testing_set):
            refsets[label].add(i)
            observed = voted_classifier.classify(feats)
            testsets[observed].add(i)

        # Higher the precision lesser the false positive
        print('Positive precision:', precision(refsets['pos'], testsets['pos']))
        # Higher the recall lesser the false negative
        print('Positive recall:', recall(refsets['pos'], testsets['pos']))
        # Higher the better
        print('Positive F-measure:', f_measure(refsets['pos'], testsets['pos']))

        print('Negative precision:', precision(refsets['neg'], testsets['neg']))
        print('Negative recall:', recall(refsets['neg'], testsets['neg']))
        print('Negative F-measure:', f_measure(refsets['neg'], testsets['neg']))

        # Analyzing sentences to get polarity of each sentence
        sa_words = []
        for line in user_input.split('\n'):
            sa_words.append(line)

        sid = SentimentIntensityAnalyzer()
        res_dic = {"Positive": 0, "Negative": 0}
        for sentence in sa_words:
            sentiment_score = sid.polarity_scores(sentence)
            if sentiment_score["compound"] < 0.0:
                res_dic["Negative"] += 1
            elif sentiment_score["compound"] > 0.0:
                res_dic["Positive"] += 1
                # else:
                #     res_dic["less"] +=1
        print(res_dic)
        print("Compound value: ", sentiment_score["compound"])

        # Classifying sentences
        results = {"Positive": 0, "Negative": 0}
        number_sentences = 0
        negative_sentences = []
        for sentence in src_doc:
            number_sentences += 1
            line = sentence.replace("\n", "").replace(".", "")
            polarity = voted_classifier.classify(self.bi_features(line))
            if str(polarity) == 'pos':
                results["Positive"] += 1
            elif str(polarity) == 'neg':
                negative_sentences.append(line)
                results["Negative"] += 1

        polarity_pos_percentage = (results["Positive"] / number_sentences)
        polarity_neg_percentage = (results["Negative"] / number_sentences)
        print("Positive percentage: ", polarity_pos_percentage * 100)
        print("Negative percentage: ", polarity_neg_percentage * 100)


if __name__ == "__main__":
        SaveBigramsClassifier()
