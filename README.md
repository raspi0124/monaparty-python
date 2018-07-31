
# monaparty-python
Wrapper for Monaparty.

# Usage
BEFORE YOU USE THIS, PLEASE SPECIFY API'S ADDRESS AT "counterparty_api" VARIABLE AT TOP OF INSIDE A "mptip" FUNCTION.
DEFAULT IS "api.monaparty.me"BUT IT SEEMS LIKE GETTING DOWN OFTEN.

    mptip(tipfromaddress, toaddress, amount, tokenname, fee, coindpass)

> tipfromaddress = required. str. From-address for sending token. 
> 
> toaddress = required. str. To-address for sending token. amount =
> required. str. amount of token you are going to send. This wrapper
> will automatically change value internally depends on either if is
> divisible or not, so please do not manually change it. Please note
> that you can't specify an decimal number if token are indivisible.
> 
> tokenname = required. str. Name of the token you are going to send.
> Please note that this wrapper doesn't include any of checking balance
> system internally, and incase there is not enough balance for token,
> API server will return error.
> 
> fee = optional, str. Total-fee for each transaction. Please enter here
> with Watanabe-unit (Known as satoshi in BTC) So, if you want to set a
> total fee of 0.01mona, set this to 1000000. Please note that this is
> not fee per kb. Default is 2000 watanabe. coindpass = optional, str.
> Incase your wallet needs a password, please specify it here.
> Otherwise, this wrapper are unable to sign transaction and send it.

mptip will return TXID if process succeeded.

    gettokenbalance(address):

> address = address you want to check balance.

gettokenbalance will return json incase of succeed.


