import yfinance as yf
import pandas as pd


from src.lookup import LookupMarketCap


# import and clean deata
df = pd.read_csv('../Data/20201124_scraped_upstream_companies.csv')
input_df = df.loc[~df['Ticker'].isna()][['Company Name', 'Ticker']]

# export ticker results
input_df[['marketCap',
		  'sharesOutstanding',
		  'fullTimeEmployees',
		  'enterpriseToEbitda',
		  'bookValue',
		  'regularMarketPrice',
		  'netIncomeToCommon',
		  'website',
		  'phone',
		  'zipCode']] = input_df['Ticker'].apply(LookupMarketCap)


# save to csv
input_df.to_csv('../Data/scraped_marketcap.csv', index=False)