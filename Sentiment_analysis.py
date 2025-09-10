import os
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
from config import PATHS


def load_stop_words():
    STOPWORD_PATH=PATHS['stopwords']
    
    stop_words = set()
    for fname in os.listdir(STOPWORD_PATH):
        with open(os.path.join(STOPWORD_PATH, fname), 'r', encoding='ISO-8859-1') as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    stop_words.add(word)
    return stop_words

def load_master_dictionary(stop_words):
    pos_words = set()
    neg_words = set()
    MASTER_DICT_PATH= PATHS['master_dict']
    for fname in os.listdir(MASTER_DICT_PATH):
        path = os.path.join(MASTER_DICT_PATH, fname)
        if 'positive' in fname.lower():
            with open(path, 'r', encoding='ISO-8859-1') as f:
                for line in f:
                    word = line.strip().lower()
                    if word and word not in stop_words:
                        pos_words.add(word)
        elif 'negative' in fname.lower():
            with open(path, 'r', encoding='ISO-8859-1') as f:
                for line in f:
                    word = line.strip().lower()
                    if word and word not in stop_words:
                        neg_words.add(word)
    return pos_words, neg_words


def analyze_sentiment(text):
    doc = nlp(text)
    stop_words = load_stop_words()
    pos_words, neg_words = load_master_dictionary(stop_words)
    tokens = [t.text.lower() for t in doc if t.is_alpha and t.text.lower() not in stop_words]
    pos_score = sum(1 for t in tokens if t in pos_words)
    neg_score = sum(-1 for t in tokens if t in neg_words)
    neg_score = -1 * neg_score 
    polarity = (pos_score - neg_score) / ((pos_score + neg_score) + 1e-6)
    subjectivity = (pos_score + neg_score) / (len(tokens) + 1e-6)
    return {
        'POSITIVE SCORE': pos_score,
        'NEGATIVE SCORE': neg_score,
        'POLARITY SCORE': polarity,
        'SUBJECTIVITY SCORE': subjectivity
    }

