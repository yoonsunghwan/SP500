# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import YahooScraper
import sqlite3
import DataBase

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

create_profile = """ 
            CREATE TABLE IF NOT EXISTS profile
            (
            stock text PRIMARY KEY,
            sector text,
            industry text,
            employee int
            )
                """
create_holder = """
            CREATE TABLE IF NOT EXISTS holder
            (
            stock text PRIMARY KEY
            )
            """
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(YahooScraper.get_profile('A'))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


