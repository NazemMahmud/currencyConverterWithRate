# Currency Converter with Rate

This is a simple python package for currency conversion between any two or to multiple currency. Also, to get latest and historical currency exchange rates & crypto exchange rates. This is based on the free API [exchangerate](https://exchangerate.host).

## Features

- Conversion rate for one or multiple currency
For all or some specific currency:
- Get latest rates
- Get historical rates. Historical means on a speficifc date
- Get timeseries rates, between any two dates
- Get fluctuation rates,  between any two dates


## Sources [Currency symbols, Bank sources, Language code formatter, crypto-currencies]

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
here, `base()` and `target()` is required method. Other available methods you will see in following examples are optional. 

You can find all the currency symbols to pass in base() and target() method for conversion in the above source link, under the file named *currency-symbols.txt*

The following examples are given using main **Currency()** class

- **Multiple targets:** In above example, target currency is only one. If you want to convert to multiple targets, use like following: (send multiple currency code as a list)
```
data = currency.convert().base('USD').target(['EUR', 'BDT', 'CZK']).get()
```
#### Available methods:

- **`amount()`**: By default, base amount is 1.00, you can change it by using **amount()**
```
data = currency.convert().base('USD').target('EUR').amount(10).get()
```
- **`places()`**: for rounding currency value upto specific decimal point. The following example will round to 2 decimal point of the target currency value
```
data = currency.convert().base('USD').target('EUR').amount(100).places(2).get()
```
- **`format_language()`**: to format the price according to a locale formatter, such as if you want to format currency as United Kingdom's format
```
data = currency.convert().base('USD').target('EUR').amount(10).places(2).format_language('en-gb').get()
```
- **`date()`**: to convert currency on a rate of a specific date. In this method, date paremeter must be in YYYY-MM-DD format 
```
data = currency.convert().base('USD').target('EUR').amount(10).date('2019-08-01').get()
```

- **`source()`**: There are 2 different types of source.
1. **Bank source**: Currency conversion according to a bank reference. In this case, you have to pass the bank's code in the **source()**. You can find all bank source code, in the above source link, under the file named *bank_sources.txt*
```
data = currency.convert().base('USD').target('EUR').amount(10).source('ecb').get()
```

2. **Crypto Currency**: Untill now, we are converting physical currency. If you want conversion between two crypto-currency, you have to use `source(crypto)` for all kind of crypto currency. 

And in both `base()` and `target()` method, you have to pass any crypto-currency symbols, instead of physical currency, like following:
```
data = currency.convert().base('BTC').target('PAC').amount(10).source('crypto').get()
```
The above example convert from bitcoin (BTC) to PAC Protocol (PAC). You can find all crypto-currency symbols, in the above source link, under the file named *crypto-currencies.txt*

##### Note: You don't have to follow any chaining sequence to use or call the optional methods. Just make sure, you call any of them before `get()`. `get()` must be last method in the chain.

Such as, you can call `places()` before `amount()`, like,
```
data = currency.convert().base('USD').target('EUR').places(2).amount(100).get()
```

### 2. Rates
There are 4 types of rates option. 
- 2.1 For latest rate: use `latest()`
- 2.2 for historical rate: use `historical("2021-05-24")`: here date is required, and format must be **YYYY-MM-DD**
- 2.3 for fluctuations rate: use `fluctuations("2021-01-01", "2021-01-03")`: here **start_date** & **end_date** is required, and both format must be **YYYY-MM-DD**
- 2.4 for timeseries rate: use `timeseries("2021-01-01", "2021-01-03")`: here **start_date** & **end_date** is required, and both format must be **YYYY-MM-DD**

For all those rates, 
- you may use `rates()` method of **Currency** class like following:
```
from currency import *
currency = Currency()

data = currency.rates().latest().get()
```
- Or, you may use only **Rates** class like following:
```
from currency import Rates
currency = Rates()

data = currency.latest().get()
```

Based on which type of rates, you want to get, the methods will be different. But all these rate types, have some common available methods. These are following:

    1. base(): for changing the base currency (by default EUR, i.e. euro): Enter 3-letter currency code for preferred base currency
    2. target(): for target currency: Enter 3-letter currency code, to get multiple target currency, send a comma separated string with 3 digit symbol, without any whitespace, 
                 like  currency.rates().latest().target("USD,EUR,BDT").get()
    3. amount(): to set amount to convert, default it is 1.00 from EURO
    4. places(): to set how many decimal point to show for target amount
    5. source(): to set source for bank view or crypto-currency
          - for bank, give any bank code (3 letter code) as a cource
          - for crypto, source will always be `crypto`, like, source('crypto')
        This is same as above source() method in currency conversion.
    6. format(): to set local currency format language code

Note: You don't have to follow any chaining sequence to use or call the optional methods. Just make sure, you call any of them before get(). Just like explained above examples

The following examples are given using main **Currency()** class.

### 2.1 Get Latest Rates
- To get all latest rates (convert from, by default euro, based on amount 1.00)
```
rate = currency.rates().latest().get()
```
The output will be like this:

      {
          "rates": {
              "AED": 4.338675,
              "AFN": 101.678441,
              "ALL": 121.876549,
              "AMD": 581.637933,
              "ANG": 2.119571,
              "AOA": 749.461213,
              "ARS": 115.296454,
              "AUD": 1.613746,
              "AWG": 2.126898,
              "AZN": 2.008353,
              "BAM": 1.958162,
              "BBD": 2.362678,
              "BDT": 100.615467,
              "BGN": 1.956466,
              "BHD": 0.446148,
              "BIF": 2342.930853,
              "BMD": 1.181473,
              "BND": 1.589243,
              "BOB": 8.13793,
              "BRL": 6.12316,
              "BSD": 1.181635,
              ...
          },
          "success": true
      }

- an example with all available optional methods, for single target symbol
```
rate = currency.rates().latest().base('USD').target("EUR").get()
```
- an example with all available optional methods, for multiple target symbol
```
rate = currency.rates().latest().base('USD').target("EUR,CZK,USD").amount(100).places(2).source('ecb').format('en-za').get()
```

### 2.2 Get Historical Rates
- an example with all available optional methods, multiple target symbol
```
rate = currency.rates().historical("2021-08-30").base('USD').target("USD,EUR,CZK").amount(100).places(2).source('ecb').format('en').get()
```
as explained above, a date must be passed as a parameter inside `historical()` in YYYY-MM-DD format. This date indicates that, the rates were for that specific day.

Output will look like following:

    {
        "rates": {
            "CZK": "$2,166.43",
            "EUR": "$84.74",
            "USD": "$100.00"
        },
        "success": true
    }


### 2.3 Get Fluctuation Rates
- an example with all available optional methods, multiple target symbol

    2 required parameters for `fluctuations()`:
    start_date: in YYYY-MM-DD format
    end_date: in YYYY-MM-DD format

```
rate = currency.rates().fluctuations("2021-01-01", "2021-01-03").base('USD').target("EUR,CZK").amount(100).places(2).source('ecb').format('en').get()
```
Output will look like following:

    {
        "rates": {
            "CZK": {
                "change": 0,
                "change_pct": 0,
                "end_rate": "$2,138.54",
                "start_rate": "$2,138.54"
            },
            "EUR": {
                "change": 0,
                "change_pct": 0,
                "end_rate": "$81.49",
                "start_rate": "$81.49"
            }
        },
        "success": true
    }

### 2.4 Get Timeseries Rates
- an example with all available optional methods, multiple target symbol

    2 required parameters:
    start_date: in YYYY-MM-DD format
    end_date: in YYYY-MM-DD format
```
rate = currency.rates().timeseries("2021-01-01", "2021-01-03").base('USD').target("EUR,CZK").amount(100).places(3).source('ecb').format('en').get()
```
Output will look like following:

    {
        "rates": {
            "2021-01-01": {
                "CZK": "$2,138.54",
                "EUR": "$81.49",
                "USD": "$100.00"
            },
            "2021-01-02": {
                "CZK": "$2,138.54",
                "EUR": "$81.49",
                "USD": "$100.00"
            },
            "2021-01-03": {
                "CZK": "$2,138.54",
                "EUR": "$81.49",
                "USD": "$100.00"
            }
        },
        "success": true
    }
