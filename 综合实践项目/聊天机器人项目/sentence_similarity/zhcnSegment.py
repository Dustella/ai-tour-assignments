import jieba
import codecs
import os


class zhcnSeg(object):
    stopwords = []
    current_path = os.path.dirname(__file__)
    stopword_filepath = os.path.join(current_path, "stopword.txt")

    def __init__(self):
        self.read_in_stopword()

    def read_in_stopword(self):
        with codecs.open(self.stopword_filepath, 'r', 'utf-8') as file_obj:
            self.stopwords = [line.strip('\r\n') for line in file_obj]

    def cut(self, sentence, stopword=True):
        seg_list = jieba.cut(sentence)
        results = [
            seg for seg in seg_list if seg not in self.stopwords or not stopword]
        return results

    def cut_for_search(self, sentence, stopword=True):
        seg_list = jieba.cut_for_search(sentence)
        results = [
            seg for seg in seg_list if seg not in self.stopwords or not stopword]
        return results

    def cut_for_search(self, sentence, stopword=True):
        seg_list = jieba.cut_for_search(sentence)
        results = [
            seg for seg in seg_list if seg not in self.stopwords or not stopword]
        return results
