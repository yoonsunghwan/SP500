import requests
from bs4 import BeautifulSoup
from datetime import datetime

def create_text_from_url(url , html_element, css):
    """
    :param html_element: html element in quotes, "table","tr","span"
    :param css: css in dictionary format "class":"W(100%) BdB Bdc($seperatorColor)"
    :return:
        list(s) of "text" separated with "|"
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    list_of_text = [i.get_text(separator= '|', strip = True) for i in soup.find_all(html_element, css)]
    return list_of_text


def list_to_dict(list_of_text, i_html_element, n_columns):
    """

    :param values: a list from the command
    :param number_of_values:
    :return:
    """
    #
    values = list_of_text[i_html_element].split('|')

    list_in_list = [{values[i:i + n_columns+1][0]:values[i:i + n_columns+1][1:]} for i in range(0, len(values), n_columns+1)]

    return list_in_list


def get_income_statement(company):

  """  url = "https://finance.yahoo.com/quote/{0}/financials?p={0}"
    page = requests.get(url.format(company))
    soup = BeautifulSoup(page.content, 'html.parser')

    values = [i.get_text(separator= '|') for i in soup.find_all('div', {'class': 'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})]
    values = values[0].split('|')



    #turn a list with this pattern [ k , v, v, v, v, v, k2,v2,v2...] a key followed by 5 values into a dictionary {k:[v*],}
    a = {}
    x = [{a[n[0]]:a[1:]} n for values[i:i+6] for i in range(0,len(values),6)]

    income_statement = [values[i:i+6] for i in range(0,len(values),6)]
    a ={}

    for i in income_statement:
        a[i[0]] = i[1:]
    return values
#    return income_statement"""
list_of_text = create_text_from_url("https://finance.yahoo.com/quote/GM/financials?p=GM",'div', {'class': 'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})
print(list_to_dict(list_of_text, 0,5))

#
#print(list_of_text)
