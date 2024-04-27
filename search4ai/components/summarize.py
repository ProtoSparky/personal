import re
import read_website as rd

from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.parsers.plaintext import PlaintextParser as parser

def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = text.lower()
  text = re.sub(r'\s+'," ",text)
  text = re.sub(r","," ",text)
  return text

cleaned_data = clean_data(rd.read_website("https://www.yr.no/nb/v%C3%A6rvarsel/daglig-tabell/1-72837/Norge/Oslo/Oslo/Oslo"))

stemmer = Stemmer(language= "norwegian")
summarizer = Summarizer(stemmer)
document = parser.document(cleaned_data)
summary = summarizer.summarize(document, 10)  # Generate a summary of 10 sentences
print(summary)