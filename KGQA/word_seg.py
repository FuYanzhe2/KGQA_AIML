import jieba
import jieba.posseg as pseg
import os

class jieba_seg(object):
    '''
    initialize jieba Segment
    '''
    def __init__(self):
        jieba.load_userdict(os.path.dirname(os.path.split(os.path.realpath(__file__))[0])+'./dictionary/movie_dict.txt')
        jieba.initialize()
    '''
    Segment words by jieba
    '''
    def wordSegment(self,text):
        text = text.strip()
        seg_list = jieba.cut(text)
        result = " ".join(seg_list)
        return result
    '''
    POS Tagging
    '''
    def postag(self,text):
        words = pseg.cut(text)
        # for w in words:
        #     print w.word, w.flag
        return words


