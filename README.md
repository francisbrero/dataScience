# financialliteracy
Weekend Project

# Strategy
Initially the goal is to start very basic and I mean really basic as a swing trading strategy:
- set some thresholds for buying and selling, these should be refreshed weekly but not necessarily
- whenever the price drops below the threshold for example $10k then buy
- whenever the price hits $10,250, sell 30%
- whenever the price hits $10,500 sell everything

# Architecture
python, Binance (https://pypi.org/project/python-binance/), 

# Getting Started
## Accounts
Binance: no longer available in the US :-(
Bittrex
## Technical setup
### python
for pyton, go [here](https://www.python.org/downloads/)

### pip
```
easy_install pip
```
or, for the latest verson
```
pip install --upgrade pip
```
### requirements
```
. setup_env.sh 
```
if you run into errors about ```Permission denied: ‘/Library/Python/2.7/site-packages/```, you might need to change permissions on your python folder. For that run:
```
sudo chown -R $USER /Library/Python/2.7/
```

# References
## Stock Trading
- https://medium.com/@wolfcrypto/how-to-setup-a-high-frequency-trading-bot-29a603a948cc
- https://medium.com/@mikkel250/trading-bot-complete-newbie-setup-guide-apitrade-bc221c5ba00e

## Crypto trading
- https://medium.com/@maxAvdyushkin/writing-crypto-trading-bot-in-python-with-telegram-and-ccxt-80632a00c637
- https://github.com/sammchardy/python-binance
- https://www.thebrokebackpacker.com/cryptocurrency-trading-bots/
- https://www.devteam.space/blog/how-to-build-a-crypto-trading-bot/
- https://www.reddit.com/r/BitcoinMarkets/comments/8h9abn/how_difficult_is_it_to_set_up_a_trading_bot/
- https://towardsdatascience.com/crypto-trading-bots-a-helpful-guide-for-beginners-60decb40e434
- https://github.com/topics/cryptocurrency-trading-bot?l=python
- https://github.com/MD3XTER/Arbitrage-Bot
- https://medium.com/@BlockchainEng/crypto-bitcoin-trading-bot-in-python-july-2018-update-e11b875933da
- https://github.com/bwentzloff/trading-bot

## Warnings
- https://hackernoon.com/things-i-wish-i-knew-when-i-started-crypto-trading-3ec33b59c3a5

## Learnings
- https://github.com/NathanEzraSchmidt/Binance-Arbitrage-Bot/blob/master/binance_arb_bot.py
- binance is no longer available