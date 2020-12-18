# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import YahooScraper
import DataBase
import pandas as pd

create_profile = """ 
            CREATE TABLE IF NOT EXISTS profile
            (
            symbol text PRIMARY KEY,
            sector text,
            industry text,
            employee int
            )
                """
create_holder = """
            CREATE TABLE IF NOT EXISTS holder
            (
            symbol text PRIMARY KEY,
            todays_date text,
            holder text,
            shares int,
            date_reported date,
            percent_out float,
            value int
            )
            """
stock_symbols = []
with open('S&P500Symbols.txt') as sp:
    securities = sp.readlines()
    for s in securities:
        stock_symbols.append(s.strip())

institutional_holders = pd.DataFrame()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for stocks in stock_symbols:
        try:
       #append each dataframe to the original dataframe
            institutional_holders = institutional_holders.append(YahooScraper.get_institutional_holders(stocks))
            print(stocks)
        except IndexError:
            pass
    # create connection and insert the final df to the stocks database.
    conn = DataBase.create_connection('stocks.db')
    DataBase.insert_to_table(conn, 'institutional_holders', institutional_holders)
    conn.close()

  #  print(institutional_holders)