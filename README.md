# Stock Prediction
Given today's stock data, predict whether the closing price tommorow will be higher or lower.

## Workflow/Methodology
1. Data fetching and preprocessing
fetch stock data from ![alphavantage](https://www.alphavantage.co) 
2. Data Normalization
3. Analysis of various supervised learning methods
4. build AWS pipeline
5. Conclusions

## Structure of data
goal is to use adjusted daily historical data of S&P500 companies from the past 20 years. Each row of input feature consists of basic input features and technical indicators. We should use at least 15 input features.

## Input Features
### Phase 1: Basic Features
daily open, daily high, daily low, daily close, daily volume, daily adjusted close

### Phase 2: Technical Indicators
not yet decided

## Models

## Future Improvements
