# Currencies 💸

This is a small currency program, it will give you live currency rates along with the capability of currency conversion. This is my final project for CS50P. It is made by using various concepts including:-
- Functions, Variables
- Loops
- Conditionals
- Libraries
- Exceptions
- File I/O



#### Video Demo 📽️: https://www.youtube.com/watch?v=uGol0ZXmk50

## Author

- [@Iamnotnot2](https://github.com/Iamnotno2)


## 🚀 About Me
I'm a young programmer with the urge to learn more and new things.


## Acknowledgements

 - [Exchange Rate API](https://www.exchangerate-api.com)




## Features

- Currencies List.
- Live Currency Rate.
- Currency Conversion.




## Libraries Used 📚

- [tabulate](https://pypi.org/project/tabulate/)

```bash
from tabulate import tabulate

```
- [requests](https://pypi.org/project/requests/)

```bash
import requests

```

## Usage/ Examples
### Initial Message
- User will be first prompted with this message:-

[![IMG-20240331-162213-2.jpg](https://i.postimg.cc/NFpHBbhz/IMG-20240331-162213-2.jpg)](https://postimg.cc/dZZ192V2)

- Select one of the options by inputing 1, 2, or 3, as shown below:-
```python
Select one of the Options(1,2,3): 1
```
### Checking Supported Currencies 🪙
- In case Option 1 is selected which is "Check Supported Currencies", the program will output supported currencies.

[![IMG-20240331-164521.jpg](https://i.postimg.cc/SQtZP4Zz/IMG-20240331-164521.jpg)](https://postimg.cc/yWcXJMCV)

- After this, User will be prompted with this message:-

```python
Would you like to see the Options menu again? (Yes/No)
```
- If the input is "Yes", then the program will show the Options menu again, otherwise the program will be terminated.
### Getting Live Rates 📈
- In case Option 2 is selected which is "Get Live Rates", the program will output the current live rates of currencies. Following will be prompted first:-
```python
Would you like to see the supported currencies list first (Yes/No)
```
- If the input is "Yes", then the program will show the supported currencies list. In case "No" is selected then the program will prompt following message:-
```python
Input Currency:
```
- If the user inputs valid currency. The rate of the currency will be shown:-
```python
Input Currency: PKR
278.231207
```
- In case the user inputs invalid currency. Following message will be prompted, and the user will be asked to input again
```python
Invalid Currency - Try Again
```
### Currency Converter 💱
- In case Option 3 is selected which is "Currency Converter", the program will convert the desired currency into another currency.
- Following message will be prompted:-

[![Screenshot-2024-03-31-17-36-57-996-com-android-chrome-2.jpg](https://i.postimg.cc/VsVn6fdG/Screenshot-2024-03-31-17-36-57-996-com-android-chrome-2.jpg)](https://postimg.cc/w3D74d5L)
- The user will be asked to input first currency, such as:-
```python
Input First Currency: USD
```
- Incase the user inputs invalid currency, the program will prompt the user to input the first currency again. In case the user inputs valid currency, the program will ask for the value of first currency. The value can be an int or a float:-
```python
Input First Currency Value: 25.5
```
- Incase the user inputs invalid value, the program will prompt the user to input first currency value again. In case the user inputs valid value, the program will ask for the second currency in which the value of first currency is to be converted:-
```python
Input Second Currency: PKR
```
- Incase the user inputs invalid currency, the program will prompt user to input the second currency again. In case the user inputs valid currency, the program will convert the value of first currency into the equivalant value of second currency. The output would be as under:-
```python
25.5 USD to PKR = 7094.90 PKR
```




## FAQ 🙋

#### Are the Currency Rates live?

Currency Rates are live for which [Exchange Rate API](https://www.exchangerate-api.com) has been used. However, the authenticity of these cannot be confirmed.

#### What is the First Currency and Second Currency in Currency Converter

First Currency is the major currency whose value is to be converted into the equivalent value of Second Currency.

#### My program is not working properly. It is giving following error:-
```python
ModuleNotFoundError: No module named 'tabulate'
```


Install the required modules as per the pip install command. In this case before running the program execute following command in the terminal:-
```python
pip install tabulate
```


## Disclaimer

The author does not take any responsibility for losses or profits incurred due to the usage of this repository. This project is for educational purposes only.
