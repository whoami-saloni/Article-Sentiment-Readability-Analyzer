PROJECT_ROOT = "/content/drive/MyDrive/Black_Coffer"
INPUT_FILE = "/content/drive/MyDrive/Black_Coffer/20211030 Test Assignment/Input.xlsx"
ARTICLE_FOLDER = "/content/drive/MyDrive/Black_Coffer/Extracted_Articles_BS"
STOPWORDS_FOLDER = "/content/drive/MyDrive/Black_Coffer/20211030 Test Assignment/StopWords"
MASTER_DICT_FOLDER = "/content/drive/MyDrive/Black_Coffer/20211030 Test Assignment/MasterDictionary"
OUTPUT_FILE="/content/drive/MyDrive/Black_Coffer/Output.xlsx"

# OR use a dictionary
PATHS = {
    "root": PROJECT_ROOT,
    "input": INPUT_FILE,
    "articles": ARTICLE_FOLDER,
    "stopwords": STOPWORDS_FOLDER,
    "master_dict": MASTER_DICT_FOLDER,
    "output":OUTPUT_FILE

}
fieldnames = [
        'URL_ID',
        'URL',
        'POSITIVE SCORE',
        'NEGATIVE SCORE',
        'POLARITY SCORE',
        'SUBJECTIVITY SCORE',
        'AVG SENTENCE LENGTH',
        'PERCENTAGE OF COMPLEX WORDS',
        'FOG INDEX',
        'AVG NUMBER OF WORDS PER SENTENCE',
        'COMPLEX WORD COUNT',
        'WORD COUNT',
        'SYLLABLE PER WORD',
        'PERSONAL PRONOUNS',
        'AVG WORD LENGTH'
    ]
