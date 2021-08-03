# Research lab - Automated Detection of Model Transformations Intents

## Cleaning the ATL files

    python\ scripts/remove_duplicates_comments.py

## Reading ATL file and adding content to Excel file 'Intent_classification_filtered.xlsx'

    python\ scripts/read_intent_classification_and_filter.py

## Tokenizing, Training and testing using machine learning techniques

    - Stopwords 'from to' not removed
    - Sequence should be maintained
    - frequency word vector


    - Decision tree
    - KNN
    - Logistic regression
    - Naive bayes

    python\ scripts/tokenize_training.ipynb

## Requirements and Setup

### Commands

        python3 -m venv env
        source env/bin/activate
        pip install -r requirements.txt
