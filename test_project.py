from project import option, get_currency_rate, program_continue
import requests

def test_option():
    assert option("1") == 1
    assert option("2") == 2
    assert option("3") == 3

def test_get_currency_rate():
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    o = response.json()
    assert get_currency_rate("PKR") == o["rates"]["PKR"]
    assert get_currency_rate("USD") == o["rates"]["USD"]
    assert get_currency_rate("EUR") == o["rates"]["EUR"]

def test_program_continue():
    assert program_continue("YES") == True
    assert program_continue("No") == False
    assert program_continue("1234") == False
