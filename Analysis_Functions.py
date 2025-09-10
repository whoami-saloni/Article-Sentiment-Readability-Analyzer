import os
import spacy
from nltk.corpus import stopwords
import en_core_web_sm
nlp = en_core_web_sm.load()
def count_syllables(word):
    word = word.lower()
    vowels = "aeiou"
    count = 0
    prev_char = False
    for c in word:
        if c in vowels:
            if not prev_char:
                count += 1
                prev_char = True
        else:
            prev_char = False
    if word.endswith("e"):
        count -= 1
    if word.endswith("es") or word.endswith("ed"):
        if count > 1:
            count -= 1
    return max(1, count)


def analyze_readability(text):
    doc = nlp(text)
    sents = list(doc.sents)
    num_sents = len(sents)
    stop_words = set(stopwords.words('english'))
    words = [t.text.lower() for t in doc if t.is_alpha and t.text.lower() not in stop_words]
    num_words = len(words)

    avg_sent_len = num_words / (num_sents + 1e-6)
    complex_words = [w for w in words if count_syllables(w) > 2]
    perc_complex = len(complex_words) / (num_words + 1e-6) * 100
    fog = 0.4 * (avg_sent_len + perc_complex)
    syllable_per_word = sum(count_syllables(w) for w in words) / (num_words + 1e-6)
    avg_word_len = sum(len(w) for w in words) / (num_words + 1e-6)
    personal_pronouns = sum(1 for t in doc if t.pos_ == "PRON" and t.text.lower() in {"i", "we", "my", "ours", "us"} and t.text != "US")

    return {
        'AVG SENTENCE LENGTH': avg_sent_len,
        'PERCENTAGE OF COMPLEX WORDS': perc_complex,
        'FOG INDEX': fog,
        'AVG NUMBER OF WORDS PER SENTENCE': avg_sent_len,
        'COMPLEX WORD COUNT': len(complex_words),
        'WORD COUNT': num_words,
        'SYLLABLE PER WORD': syllable_per_word,
        'PERSONAL PRONOUNS': personal_pronouns,
        'AVG WORD LENGTH': avg_word_len
    }
