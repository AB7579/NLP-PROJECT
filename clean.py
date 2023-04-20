import re
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove stopwords
    swahili_stopwords = stopwords.words('kiswahili')
    text = ' '.join([word for word in text.split() if word not in swahili_stopwords])

    # Stem the words
    stemmer = SnowballStemmer('english')
    text = ' '.join([stemmer.stem(word) for word in text.split()])

    return text
