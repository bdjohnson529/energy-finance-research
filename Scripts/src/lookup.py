"""
lookup.py
"""
import yfinance as yf
import pandas as pd

def LookupMarketCap(ticker):
    """
    Lookups up financial information about a public traded stock.
    """
    print(ticker)
    msft = yf.Ticker(ticker)
    
    try:
        # convert output to pandas dataframe
        info = msft.info
        df = pd.DataFrame(list(info.items()), columns=['key','value'])

        # write to csv
        df.to_csv(f'../Data/YFinance/{ticker}.csv', index=False)
        
        # extract data
        marketCap = df.loc[df['key'] == 'marketCap']['value'].values[0]
        sharesOutstanding = df.loc[df['key'] == 'sharesOutstanding']['value'].values[0]
        fullTimeEmployees = df.loc[df['key'] == 'fullTimeEmployees']['value'].values[0]
        enterpriseToEbitda = df.loc[df['key'] == 'enterpriseToEbitda']['value'].values[0]
        bookValue = df.loc[df['key'] == 'bookValue']['value'].values[0]
        regularMarketPrice = df.loc[df['key'] == 'regularMarketPrice']['value'].values[0]
        netIncomeToCommon = df.loc[df['key'] == 'netIncomeToCommon']['value'].values[0]
        website = df.loc[df['key'] == 'website']['value'].values[0]
        phone = df.loc[df['key'] == 'phone']['value'].values[0]
        zipCode = df.loc[df['key'] == 'zip']['value'].values[0]


        data = {'marketCap': marketCap,
                'sharesOutstanding': sharesOutstanding,
                'fullTimeEmployees': fullTimeEmployees,
                'enterpriseToEbitda': enterpriseToEbitda,
                'bookValue': bookValue,
                'regularMarketPrice': regularMarketPrice,
                'netIncomeToCommon': netIncomeToCommon,
                'website': website,
                'phone': phone,
                'zipCode': zipCode}

        print(data)
        return pd.Series(data)
    except:
        data = {'marketCap': None,
                'sharesOutstanding': None,
                'fullTimeEmployees': None,
                'enterpriseToEbitda': None,
                'bookValue': None,
                'regularMarketPrice': None,
                'netIncomeToCommon': None,
                'website': None,
                'phone': None,
                'zipCode': None}

        print(data)
        return pd.Series(data)