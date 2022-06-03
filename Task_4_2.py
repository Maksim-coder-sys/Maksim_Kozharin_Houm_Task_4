




import requests



def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    """ we get the current rate by currency code from the site """

    if not (currency_code and url):
        return None

    currency_code = currency_code.upper()


    response = requests.get(url)

    if response.ok:

        cur = response.text.split(currency_code)


        if len(cur) == 1:
            return None


        value = cur[1].split("</Value>")[0].split("<Value>")[1]


        value = float(value.replace(",", "."))




        return (value)

    else:
        return None


print((currency_rates("Usd")))
print((currency_rates("eUR")))
