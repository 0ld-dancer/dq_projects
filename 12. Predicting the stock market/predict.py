if __name__ == '__main__':
    import pandas as pd
    from datetime import datetime

    stock_market = pd.read_csv('sphist.csv')
    stock_market['Date'] = pd.to_datetime(stock_market['Date'],
                                          format='%Y-%m-%d')

    date_mask = stock_market['Date'] > datetime(year=2015,
                                                month=4,
                                                day=1)

    # stock_market_filtred = stock_market[date_mask]

    stock_market.sort_values(by='Date', inplace=True)

    stock_market = stock_market.assign(avg_5=0,
                                       avg_30=0,
                                       ratio_5_30=0)

    stock_market.reset_index(drop=True, inplace=True)

    for index, row in stock_market.iterrows():
        if index >= 5:
            avg_5v = stock_market.iloc[(index - 5):index]['Close'].mean()
            stock_market.loc[index, 'avg_5'] = avg_5v

        if index >= 30:
            avg_30v = stock_market.iloc[(index - 30):index]['Close'].mean()
            stock_market.loc[index, 'avg_30'] = avg_30v
            stock_market.loc[index, '5_30_ratio'] = avg_5v / avg_30v

    print(stock_market.head(10))
