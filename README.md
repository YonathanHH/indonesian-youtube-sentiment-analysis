# Indonesian YouTube Sentiment Analysis

This project explores sentiment analysis on Indonesian YouTube comments using Natural Language Processing.  
It includes a Python script for scraping comments from YouTube and a dataset in CSV format that was parsed from the collected comments.

## Overview

The goal of this project is to classify Indonesian YouTube comments into sentiment categories such as:

- Positive
- Neutral
- Negative

The workflow includes:
- Scraping YouTube comments with Python
- Cleaning and preprocessing Indonesian text
- Performing sentiment analysis using a pre-trained Hugging Face model
- Visualizing sentiment distribution
- Manually validating model predictions

## Dataset

The `v-1YabkN-pM_comments.csv` file in this repository contains the raw parsed dataset collected from YouTube comments.

Because this is raw data, it may include:
- duplicate comments
- spam
- emojis
- links
- informal Indonesian language
- slang and abbreviations

## Files

- `youtube.py`  
  Python script used to scrape comments from YouTube

- `v-1YabkN-pM_comments.csv`  
  Raw parsed dataset containing YouTube comments

- `Indonesian_Politics_Sentiment.ipynb`  
  Notebook with the description of the workflow from preprocessing to wordclouds viz.

## Tech Stack

- Python
- Pandas
- Sastrawi
- Hugging Face Transformers
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Scrape YouTube comments
2. Save the comments into a CSV file
3. Clean and preprocess the text
4. Run sentiment classification
5. Analyze sentiment distribution
6. Validate results manually
7. Compare model predictions with human labels

## Key Insight

A pretrained NLP model can perform well on benchmark data, but real-world performance may vary depending on the topic, domain, and language style.  
In this project, manual validation showed that model predictions were not always reliable for political comments, which highlights the importance of evaluating models on domain-specific data.

## Notes

This project is intended for learning and portfolio purposes.  
It demonstrates an end-to-end NLP workflow, from data collection to model evaluation.

## License

This project is shared for educational purposes.

## Author

Yonathan Hary Hutagalung
