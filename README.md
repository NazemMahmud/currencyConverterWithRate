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

For all currency symbols, language code for locale formatter, bank source codes, crypto-currency codes, check this  [sources](https://gist.github.com/NazemMahmud/1228e03fcc796cfbdba60069a1e6381e)

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

here, `base()` and `target()` is required method. Other available methods you will see in following example are optional
