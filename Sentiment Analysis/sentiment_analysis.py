# import libraries
import pandas as pd
import spacy
import re
from spacytextblob.spacytextblob import SpacyTextBlob
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# With copy-on-write mode enabled, pandas will try to ensure that changes are only
# made to the copy when necessary, helping to prevent accidental modifications to the original data.
pd.options.mode.copy_on_write = True

# Load spaCy model and add SpacyTextBlob to the pipeline
nlp = spacy.load('en_core_web_md')
nlp.add_pipe('spacytextblob')

# Read the CSV file
df = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Removing all missing values from this columns
clean_data = df.dropna(subset=['reviews.text', 'reviews.rating'])

# Selecting the 'reviews.text' column from the dataset
reviews_data = clean_data['reviews.text']


def rating_to_sentiment(rating):
    '''Convert numerical ratings to sentiment labels'''
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else:
        return 'neutral'


# Apply rating_to_sentiment function to the reciews.reting column
clean_data['true_sentiment'] = clean_data['reviews.rating'].apply(rating_to_sentiment)


def preprocess_text(text):
    """Preprocess the text by lowering case, stripping whitespace, removing stopwords, punctuation, and lemmatizing."""
    text = text.lower().strip()
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    cleaned_text = ' '.join(tokens)
    return cleaned_text


def remove_unwanted(document):
    """Remove user mentions, URLs, hashtags, punctuation, and double spaces."""
    document = re.sub("@[A-Za-z0-9_]+"," ", document)
    document = re.sub(r'http\S+', ' ', document)
    document = re.sub("#[A-Za-z0-9_]+","", document)
    document = re.sub("[^0-9A-Za-z ]", "" , document)
    document = document.replace('  ',"")
    return document.strip()


# Apply preprocessing functions to the reviews
reviews_data = clean_data['reviews.text'].apply(preprocess_text).apply(remove_unwanted)


def predict_sentiment(review):
    """Predict the sentiment of the review using SpacyTextBlob."""
    doc = nlp(review)
    sentiment_score = doc._.blob.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'


# Add sentiment predictions to the dataframe
clean_data['predicted_sentiment'] = [predict_sentiment(review) for review in reviews_data]

# Calculate accuracy, precision, recall, and F1-score
accuracy = accuracy_score(clean_data['true_sentiment'], clean_data['predicted_sentiment'])
precision = precision_score(clean_data['true_sentiment'], clean_data['predicted_sentiment'], average='weighted')
recall = recall_score(clean_data['true_sentiment'], clean_data['predicted_sentiment'], average='weighted')
f1 = f1_score(clean_data['true_sentiment'], clean_data['predicted_sentiment'], average='weighted')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Display the first few rows of the dataframe with sentiments
print(clean_data[['predicted_sentiment', 'reviews.text']].head())

# Calculate and print similarity between the first two reviews
doc1 = nlp(reviews_data[0])
doc2 = nlp(reviews_data[1])
similarity = doc1.similarity(doc2)
print("Similarity between the sentences:",similarity)

# Detailed classification report
print(classification_report(clean_data['true_sentiment'], clean_data['predicted_sentiment']))

# Plot and save the distribution of sentiments
sns.countplot(data=clean_data,x='predicted_sentiment')
plt.savefig('plot.png')
plt.show()