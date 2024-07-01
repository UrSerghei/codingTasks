# Sentiment Analysis of Amazon Product Reviews

## Project Overview
This project aims to analyze the sentiment of Amazon product reviews by using natural language processing (NLP) techniques and machine learning algorithms. The analysis involves preprocessing the text data, predicting sentiment, and evaluating the performance of the sentiment analysis model.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data](#data)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/UrSerghei/codingTasks/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Create and activate a virtual environment:**:
   ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**:
   ```sh
    pip install -r requirements.txt
   ```

4. **Download the spaCy model:**:
   ```sh
    python -m spacy download en_core_web_md
   ```

## Usage

To perform sentiment analysis on the Amazon product reviews dataset, run the following script:

   ```sh
    python sentiment_analysis.py
   ```

## Project Structure

sentiment-analysis/
│
├── amazon_product_reviews.csv  # Dataset
├── sentiment_analysis.py       # Main script for sentiment analysis
├── requirements.txt            # Required packages
├── README.md                   # Project documentation
└── plot.png                    # Distribution plot of predicted sentiments

## Data

The dataset used in this project is `amazon_product_reviews.csv`, which contains Amazon product reviews. The relevant columns are:

- `reviews.text`: The text of the review.
- `reviews.rating`: The numerical rating given by the reviewer.

## Model Evaluation

The sentiment analysis model's performance is evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score

These metrics are calculated based on the true sentiments derived from the ratings and the predicted sentiments from the model.

## Results

The first few rows of the data frame with predicted sentiments are displayed, along with a plot of the distribution of predicted sentiments. The similarity between the first two reviews is also calculated and printed.

The performance metrics and a detailed classification report are printed on the console.


## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.