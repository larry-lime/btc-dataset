# Project Notes
[Project Link](https://docs.google.com/document/d/1C2lyHeIPJA2I4QPfz0SOv1lIj86oaogqGy9ZbJR0iRw/edit?usp=sharing)

## Research Questions:
- Are the outliers really invalid? 
    + Just check them 
- Geographic distribution of Bitcoin mining 
    + A bit difficult
    Can only determine correlation and not causation
- Correlation with stocks
    + Which non-tech stock is most strongly correlated with the price of Bitcoin
    + And why?
- Most hyped crypto
    + Use Google Trends
- Tell a story about how world events manifests itself in bitcoin block and price data
- If we want to we now have a systematic way of finding out what is the most hyped crypto
    - Gather historical price data
    - Gather historical trends data
    - Gather BTC dataset numerical datapoints
    - Min-max scale all the data and graph it
    - Calculate the correlation
    - Try and predict a future outcome
        
### Interesting Topics to Explore
- Look into that ML algorithm that used the news to conduct sentiment analysis and make projections for the future of bitcoin's price
- Look into the correlation between the location of the bitcoin mining pools and the search results per region
- 

### Interesting Relations

## Analysis
### Resources
- Python Packages
    - 
- Websites
    - [Open Blender](https://www.openblender.io/#/welcome)

### Data Analysis Methods
1. Using pytrends to import Google Trends data
- [Pytrends Tutorial](https://www.thepythoncode.com/article/extract-google-trends-data-in-python)
- [Pytrends Github Repo](https://github.com/GeneralMills/pytrends)

### Statistical Analysis Checklist
- Min-Max scaling for the graphing
- User Linear regression to predict the future bitcoin price and other numerical data

### Data Sets
- Google Trends Data
    - Imported with pytrends 
- Crypto Price Data
    - Imported from yfinance 
- BTC Dataset
    - Provided by Prof. Zhang 

### Sequence of Analysis
- [ ] Correlation
    - [x] Block & Price Data
    - [x] Price & Block Data
    - [ ] Search & Block Data
        - Have to make it one data point per month 
- [ ] Regression
- [ ] ML Bonus?

### Interesting Findings
- ETH search data is heavily correlated with BTC price

### To-Do
- Use web scraping to search the internet for the mining pools
    - [Geekg2Geeks Tutorial](https://www.geeksforgeeks.org/performing-google-search-using-python-code/)

# Limitations
- I'm the only person in the group that is familiar with using python for data science
- The process for this project was a little bit unclear. It was quite unique
    1. First we had to explore our btc dataset
    2. Then we had to explore additional data like Google Trends and Crypto Price data
    3. Take our findings and figure out which of our research questions these findings can solve
 - When compressing the data for the datasets, make sure to take the average and not just one sample from the dataset

# Notebook Outline
- [x] Introduction
- [x] Import Data
    - [ ] Block Data
        - [ ] Save as .pk file
    - [ ] Search Data
        - [ ] Save as .pk file
    - [ ] Price Data
        - [ ] Save as .pk file
- [x] Block & Search Data
    - [x] Import Packages
    - [x] Import Data
        - Save Original Data
        - Plot Original Data
    - [x] Clean and Scale Data 
    - [x] Analyze Data
    - [x] Plot Data
    - [ ] Regression Lines
- [ ] Price & Block Data
    - [ ] Import Packages
    - [ ] Import Data
        - Save Original Data
        - Plot Original Data
    - [ ] Clean and Scale Data 
    - [ ] Analyze Data
    - [ ] Plot Data
- [ ] Search & Price Data
    - [ ] Import Packages
    - [ ] Import Data
        - Save Original Data
        - Plot Original Data
    - [ ] Clean and Scale Data 
    - [ ] Analyze Data
    - [ ] Plot Data
- Other Data Imports
    - [ ] Regional Trends Data
    - [ ] Exchange Data