from Analysis_Functions import analyze_readability
from Sentiment_analysis import analyze_sentiment
from Data_Extraction import retreive_url,load_url_mapping_xlsx
from config import PATHS,fieldnames
import pandas as pd
import os
import csv



def score():
    results=[]
    retreive_url()
    for fname in os.listdir(PATHS['articles']):
        if fname.endswith(".txt"):

            url_id=fname.replace('.txt', '')
            with open(os.path.join(PATHS['articles'], fname), 'r', encoding='ISO-8859-1') as f:
                text = f.read()
            sentiment = analyze_sentiment(text)
            readability = analyze_readability(text)
            result = {
                    'url_id':url_id,
                    **sentiment,
                    **readability
                    }
            results.append(result)
    save_scores_to_file(results)
    return results


def save_scores_to_file(results):
    url_map=load_url_mapping_xlsx()
    output_file=PATHS['output']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for result in results:
            url_id = result.get('url_id', '')
            url = url_map.get(url_id, '')

            row = {
                'URL_ID': url_id,
                'URL': url,
                'POSITIVE SCORE': result.get('POSITIVE SCORE', ''),
                'NEGATIVE SCORE': result.get('NEGATIVE SCORE', ''),
                'POLARITY SCORE': result.get('POLARITY SCORE', ''),
                'SUBJECTIVITY SCORE': result.get('SUBJECTIVITY SCORE', ''),
                'AVG SENTENCE LENGTH': result.get('AVG SENTENCE LENGTH', ''),
                'PERCENTAGE OF COMPLEX WORDS': result.get('PERCENTAGE OF COMPLEX WORDS', ''),
                'FOG INDEX': result.get('FOG INDEX', ''),
                'AVG NUMBER OF WORDS PER SENTENCE': result.get('AVG NUMBER OF WORDS PER SENTENCE', ''),
                'COMPLEX WORD COUNT': result.get('COMPLEX WORD COUNT', ''),
                'WORD COUNT': result.get('WORD COUNT', ''),
                'SYLLABLE PER WORD': result.get('SYLLABLE PER WORD', ''),
                'PERSONAL PRONOUNS': result.get('PERSONAL PRONOUNS', ''),
                'AVG WORD LENGTH': result.get('AVG WORD LENGTH', ''),
            }
            writer.writerow(row)

    print(f"Final results saved to {output_file}")


    




