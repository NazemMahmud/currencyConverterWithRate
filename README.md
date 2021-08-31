# Currency Converter with Rate

This is a simple python package for currency conversion between any two or to multiple currency. Also, to get latest and historical currency exchange rates & crypto exchange rates. This is based on the free API [exchangerate](https://exchangerate.host).

## Features

- Conversion rate for one or multiple currency
For all or some specific currency:
- Get latest rates
- Get historical rates. Historical means on a speficifc date
- Get timeseries rates, between any two dates
- Get fluctuation rates,  between any two dates

## Installation

## Sources

For all currency symbols, language code for locale formatter, bank source codes, crypto-currency codes, check this  [Symbol & Code Sources](https://gist.github.com/NazemMahmud/1228e03fcc796cfbdba60069a1e6381e)

# Usage Example


### 1. Currency Conversion
- To convert one currency to another, you may chain method like this
```
from currency import *
currency = Currency()

data = currency.convert().base('USD').target('EUR').get()
```
- If you want only **converter** option, you may use like this:
```
from currency import CurrencyConverter
currency = CurrencyConverter()

data = currency.base('USD').target('EUR').get()
```
The output will be like this:
```
[
  {
    'from': 'USD', 
    'to': 'EUR', 
    'converted_amount': 0.846571, 
    'success': True
  }
]
```
here, `base()` and `target()` is required method. Other available methods you will see in following example are optional.

The following examples are given using main **Currency()** class

- **Multiple targets:** In above example, target currency is only one. If you want to convert to multiple targets, use like following: (send multiple currency code as a list)
```
data = currency.convert().base('USD').target(['EUR', 'BDT', 'CZK']).get()
```
#### Available methods:

- **amount()**: By default, base amount is 1.00, you can change it by using **amount()**
```
data = currency.convert().base('USD').target('EUR').amount(10).get()
```
