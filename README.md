# Stock Prediction
Given today's stock data, predict whether the closing price tommorow will be higher or lower.
[![Build Status](https://travis-ci.org/UWCESEDUO/stock-prediction.svg?branch=master)](https://travis-ci.org/UWCESEDUO/stock-prediction)

## Workflow/Methodology
1. Data fetching and preprocessing 
2. Data Normalization
3. Feature extraction/selection
3. Analysis of various supervised learning methods
4. build AWS pipeline
5. Conclusions

## Structure of data
goal is to use adjusted daily historical data of S&P500 companies from the past 20 years. Each row of input feature consists of basic input features and technical indicators. We should use at least 15 input features.

## Project outline
### data fetching and preprocessing - done
in this phase, we fetch the basic features from [](https://www.alphavantage.co) given a list of input symbols, this is done in `fetch-stock-data.py`. then a preliminary clean of the data is performed to remove any incomplete data.

### data normalization

## Input Features
### Phase 1: Basic Features
daily open, daily high, daily low, daily close, daily volume, daily adjusted close

### Phase 2: Technical Indicators
not yet decided

## Models

## Future Improvements
