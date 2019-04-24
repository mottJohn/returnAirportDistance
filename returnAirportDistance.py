import pandas as pd
from requests_html import HTMLSession
session = HTMLSession()

#read excel
df_input = pd.read_excel("input.xlsx")


def getDistance(from_destination, to_destination):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'} #to avoid bad response

    html = "https://www.world-airport-codes.com/distance/?a1={}&a2={}&code=IATA".format(from_destination, to_destination) #parse the link with from and to
    r = session.get(html, verify = False, headers = headers) #request turn ssl false and headers = headers

    xpath = '/html/body/div[1]/div[4]/div/div/div/div/div[1]/main/article/div/div[1]/p/strong/text()' #path to the html tag containing distance
    return r.html.xpath(xpath)[0]

df_input["Distance"] = df_input.apply(lambda row: getDistance(row['from_destination'], row['to_destination']), axis=1)

print(df_input)

df_input.to_excel("output.xlsx", index = False)