import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle


# Model Training
def preprocess_train(dataset_filepath, test_size, random_state):
    dataset = pd.read_csv(dataset_filepath, delimiter='\t', quoting=3)
    corpus = clean(dataset)
    cv = CountVectorizer(max_features=1420)

    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    bow_path = 'c1_BoW_Sentiment_Model.pkl'
    pickle.dump(cv, open(bow_path, "wb"))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return [X_train, X_test, y_train, y_test]


def preprocess_inference(dataset_filepath, pickle_file):
    # Multiple Datapoints
    if dataset_filepath.endswith('.tsv'):
        dataset = pd.read_csv(dataset_filepath, delimiter='\t', quoting=3)
        return clean(dataset, pickle_file)
    # Single Datapoint (direct)
    else:
        datapoint = dataset_filepath
        cv = pickle.load(open(pickle_file, "rb"))
        return cv.transform([datapoint]).toarray()[0]


def clean(dataset, pickle_file=None):
    nltk.download('stopwords')
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    corpus = []
    for i in range(0, int(dataset.shape[0])):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    if pickle_file is not None:
        cv = pickle.load(open(pickle_file, "rb"))
        X_fresh = cv.transform(corpus).toarray()
        return X_fresh
    return corpus
