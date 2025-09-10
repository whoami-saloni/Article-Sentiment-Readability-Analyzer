# 📰 Article Sentiment & Readability Analyzer 

This project analyzes articles by extracting **sentiment scores** and **readability metrics** to evaluate content quality.  
It automates the workflow of scraping articles, cleaning text, performing sentiment analysis, and exporting results to Excel.  

---

## ✨ Features
- **Sentiment Analysis**
  - Positive & Negative Scores
  - Polarity
  - Subjectivity
- **Readability Metrics**
  - Average Sentence Length  
  - Percentage of Complex Words  
  - Average Number of Words Per Sentence  
  - Average Word Length  
  - Fog Index  
  - Complex Word Count  
  - Word Counts & Syllable Counts  
  - Personal Pronouns Detection  
- **Output:** Results saved in a clean **Excel file** (`Output.xlsx`)

---


## ⚙️ Setup

### 1️⃣ Install dependencies
Run the following in terminal / Colab:

```bash
pip install requests beautifulsoup4 nltk spacy pandas openpyxl
python -m spacy download en_core_web_sm
```
### Download NLTK stopwords:
```bash
import nltk
nltk.download('stopwords')
```
## How to Run
** Step 1 – Configure Paths

Modify config.py to specify correct input/output paths for your system.

** Step 2 – Extract & Analyze

Run the main script to scrape, analyze, and generate results:

```bash
python Main.py
```


This project analyzes articles by extracting **sentiment scores** and **readability metrics** to evaluate content quality.  
It automates the workflow of scraping articles, cleaning text, performing sentiment analysis, and exporting results to Excel.  

---

## 🚀 Workflow

This will:  
1. Use **Input.xlsx** to scrape all article URLs  
2. Save raw text files in the **Articles/** folder  
3. Analyze each article for **sentiment + readability metrics**  
4. Export results to **Output.xlsx**  

---

## 🔎 How It Works

| Step       | Details                                                                 |
|------------|-------------------------------------------------------------------------|
| **Scraping** | Uses `requests` + `BeautifulSoup` to fetch articles from URLs           |
| **Cleaning** | Applies **NLTK stopwords** + custom stopword removal                    |
| **Sentiment**| Uses **MasterDictionary** (positive/negative word lists) for polarity   |
| **Analysis** | Computes readability metrics (Fog Index, Avg. Sentence Length, etc.)    |
| **Export**   | Stores all computed scores in an **Excel file (`Output.xlsx`)**         |

---

## 📊 Example Output Fields

- Positive Score  
- Negative Score  
- Polarity  
- Subjectivity  
- Average Sentence Length  
- % of Complex Words  
- Fog Index  
- Average Word Length  
- Word Count, Syllable Count, Complex Word Count  
- Personal Pronouns  

---

## 📌 Notes

- Input URLs must be listed in **Input.xlsx** (`URL_ID`, `URL`).  
- **StopWords** and **MasterDictionary** folders must remain intact for analysis.  
- Final results are written to **Output.xlsx** (path configured in `config.py`).  

---

## 🛠️ Tech Stack

- **Python**: `requests`, `BeautifulSoup`, `pandas`, `nltk`, `spacy`, `openpyxl`  
- **NLP**: Stopword removal, sentiment scoring, readability metrics  
- **Output**: Automated **Excel export**  

---

## 📧 Author

**Saloni Sahal**  
🔗 [LinkedIn](https://www.linkedin.com/in/saloni-sahal/) | [GitHub](https://github.com/whoami-saloni)  

---
