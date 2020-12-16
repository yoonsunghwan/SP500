import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_profile(symbol):
    """
        From Yahoo finance get the profile of a company using its symbol
        symbol = Stocks symbol/ Symbol of security
        Returns dictionary with the stocks profile
    """
    # url from yahoo finance
    url = "https://finance.yahoo.com/quote/{0}/profile?p={0}"
    # get requests and create soup
    page = requests.get(url.format(symbol))
    soup = BeautifulSoup(page.content, 'html.parser')

    # from the soup get the text from the div element and class 'asset-profile-container'
    # split the string value into a list of values which will be the values for the dictionary
    values = [i.get_text(separator='| ', strip=True) for i in
              soup.find_all('div', {'class': 'asset-profile-container'})]
    values = values[0].split('| ')

    # create a dictionary with the following keys
    profile = dict.fromkeys(
        ["Symbol", "Security", "Location", "Todays_Date", "Sector", "Industry", "FullTimeEmployees"])
    # from the values variable map the corresponding values to its respective keys
    profile["Symbol"] = symbol
    profile["Security"] = values[0]
    profile["Location"] = values[2]
    profile["Sector"] = values[8]
    profile["Industry"] = values[11]
    profile["FullTimeEmployees"] = int(values[14].replace(',', ''))
    profile["Todays_Date"] = datetime.today().strftime("%m/%d/%y")

    return profile


def get_financial(symbol):
    """imcomplete
    url = "https://finance.yahoo.com/quote/{0}/key-statistics?p={0}"

    page = requests.get(url.format(company))
    soup = BeautifulSoup(page.content, 'html.parser')
    values = [i.get_text() for i in soup.find_all('td', {'class': "Fw(500) Ta(end) Pstart(10px) Miw(60px)"})]
    keys = [i.get_text() for i in soup.find_all('td', {
        'class': "Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px)  Miw(140px)"})]
    return values, keys

    """
    url = "https://finance.yahoo.com/quote/{0}/key-statistics?p={0}"

    page = requests.get(url.format(symbol))
    soup = BeautifulSoup(page.content, 'html.parser')
    values = [i.get_text(separator= '|' ,strip = True) for i in soup.find_all('div', {'class': "Fl(start) W(50%) smartphone_W(100%)"})]

    return values[0]


def get_institutional_holders(symbol):
    """
        From yahoo finance get the TOP institutional holders of a company
        symbol = Stocks symbol/ Symbol of security

        Returns a dictionary with the stocks institutional holders, shares, date, etc
    """
    url = "https://finance.yahoo.com/quote/{0}/holders?p={0}"
    page = requests.get(url.format(symbol))
    soup = BeautifulSoup(page.content, 'html.parser')

    values = [i.get_text(separator='|',strip = True) for i in soup.find_all('table', {'class': 'W(100%) BdB Bdc($seperatorColor)'})]
    values = values[0].split('|')

    institutional_holders = {}
    holder = [values[i] for i in range(0,len(values),5)][1:]
    shares = [values[i] for i in range(1,len(values),5)][1:]
    date_reported = [values[i] for i in range(2,len(values),5)][1:]
    percent_out = [values[i] for i in range(3,len(values),5)][1:]
    val = [values[i] for i in range(4,len(values),5)][1:]

    institutional_holders['Symbol'] = symbol
    institutional_holders['Todays_Date'] = datetime.today().strftime("%m/%d/%y")
    institutional_holders['Holder'] = holder
    institutional_holders['Shares'] = shares
    institutional_holders['Date_Reported'] = date_reported
    institutional_holders['Percent_Out'] = percent_out
    institutional_holders['Value'] = val

    return institutional_holders


def get_mutual_fund_holders(symbol):
    """
        From yahoo finance get the TOP mutual fund holders of a company
        symbol = Stocks symbol/ Symbol of security

        Returns a dictionary with the stocks mutual fund holders, shares, date, etc
    """
    url = "https://finance.yahoo.com/quote/{0}/holders?p={0}"
    page = requests.get(url.format(symbol))
    soup = BeautifulSoup(page.content, 'html.parser')

    values = [i.get_text(separator='|',strip = True) for i in soup.find_all('table', {'class': 'W(100%) BdB Bdc($seperatorColor)'})]
    values = values[1].split('|')

    mutualfund_holders = {}
    holder = [values[i] for i in range(0,len(values),5)][1:]
    shares = [values[i] for i in range(1,len(values),5)][1:]
    date_reported = [values[i] for i in range(2,len(values),5)][1:]
    percent_out = [values[i] for i in range(3,len(values),5)][1:]
    val = [values[i] for i in range(4,len(values),5)][1:]

    mutualfund_holders['Symbol'] = symbol
    mutualfund_holders['Todays_Date'] = datetime.today().strftime("%m/%d/%y")
    mutualfund_holders['Holder'] = holder
    mutualfund_holders['Shares'] = shares
    mutualfund_holders['Date_Reported'] = date_reported
    mutualfund_holders['Percent_Out'] = percent_out
    mutualfund_holders['Value'] = val

    return mutualfund_holders


def list_to_dict(values, number_of_values):
    """

    :param values: a list from the command
    :param number_of_values:
    :return:
    """
    number_of_values = number_of_values - 1
    list_in_list = [values[i:i + number_of_values] for i in range(0, len(values), number_of_values)]
    key_values = {}
    for l in list_in_list:
        key_values[l[0]]] = l[1:]
    return key_values

def get_income_statement(company):

    url = "https://finance.yahoo.com/quote/{0}/financials?p={0}"
    page = requests.get(url.format(company))
    soup = BeautifulSoup(page.content, 'html.parser')

    values = [i.get_text(separator= '|') for i in soup.find_all('div', {'class': 'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})]
    values = values[0].split('|')


def get_balance_sheet(company):
    url = "https://finance.yahoo.com/quote/{0}/balance-sheet?p={0}"
    page = requests.get(url.format(company))
    soup = BeautifulSoup(page.content, 'html.parser')
    _values = [i.get_text(separator='**') for i in soup.find_all('div', {'data-test': 'fin-row'})]
    # list of dicts with columns and values
    col_values = [{_values[i].split('**')[0]: _values[i].split('**')[1:]} for i in range(len(_values))]
    _dates = [i.get_text() for i in soup.find('div', {'class': 'D(tbr) C($primaryColor)'})][1:]

    return col_values, _dates


def get_cash_flow(company):
    url = "https://finance.yahoo.com/quote/{0}/cash-flow?p={0}"
    page = requests.get(url.format(company))
    soup = BeautifulSoup(page.content, 'html.parser')
    _values = [i.get_text(separator='**') for i in soup.find_all('div', {'class': 'D(tbrg)'})][0]
    # list of dicts with columns and values
    col_values = [{_values.split('**')[i:i + 6][0]: _values.split('**')[i:i + 6][1:]} for i in
                  range(0, len(_values.split('**')), 6)]
    _dates = [i.get_text() for i in soup.find('div', {'class': 'D(tbr) C($primaryColor)'})][1:]

    return col_values, _dates


print(get_income_statement("A"))
