def mptip(tipfromaddress, toaddress, amount, tokenname, fee, coindpass):
	#Please specify your counterparty-server below.
	counterparty_api = "https://api.monaparty.me/"

	tipto = str(to)
	tipamount = str(amount)
	tiptoken = str(tokenname)
	tipfromaddresses = '"' + tipfromaddress + '"'
	tiptoaddress = '"' + to + '"'
	tiptoken = '"' + tiptoken + '"'
	if fee == "":
		fee = "2000"
	if tipfromaddress == "" or toaddress == "" or amount == "" or tokenname == "":
		error = "Required argument not filled."
		return error
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Accept': 'application/json, text/javascript',
	}

	data = '{"jsonrpc":"2.0", "id":0, "method":"get_asset_info", "params":{"assets":[' + tiptoken + ']} }'

	asset_info = requests.post(counterparty_api, headers=headers, data=data)
	responsejson = asset_info.json()
	responseresult = responsejson['result']
	print(responseresult)
	isdivisible = responseresult[0]["divisible"]
	isdivisible = str(isdivisible)
	print(isdivisible)
	print("---Assetinfo compleate---")
	satoshivalue = "100000000"
	satoshivalue = int(satoshivalue)
	if isdivisible == "True":
		tipamount = float(tipamount)
		tipamount = tipamount * satoshivalue
		print(tipamount)
		tipamount = int(tipamount)
		tipamount = str(tipamount)

	data = '{\n \
		"method": "create_send",\n \
		"params": {"source": ' + tipfromaddresses + ', "destination": ' + tiptoaddress + ', "asset": ' + tiptoken + ', "quantity": ' + tipamount + ', "fee": ' + fee + ', "allow_unconfirmed_inputs": true, "use_enhanced_send": false },\n \
		"jsonrpc": "2.0",\n \
		"id": 1\n \
	}'
	print(data)
	repfrom = '"' + tipamount + '"'
	data = data.replace(repfrom, tipamount)



	print(data)
	response = requests.post(counterparty_api, headers=headers, data=data)
	print(response)
	print(response.text)
	print("---create_send request compleate---")
	print("")
	responsejson = response.json()
	rawtransaction = responsejson['result']
	print(rawtransaction)
	rawtransaction = str(rawtransaction)
	print("")
	if coindpass != "":
		cmd = "monacoin-cli walletpassphrase " + coindpass + " 30"
		rut = subprocess.check_output( cmd.split(" ") )
	cmd = "monacoin-cli signrawtransaction " + rawtransaction + ""
	rut = subprocess.check_output( cmd.split(" ") )
	rut = str(rut)
	rut = rut.replace('\\n', '')
	rut = rut.replace("b'", '')
	rut = rut.replace("'", '')
	if "true" in rut:
		rut = rut.replace("true", '"true"')
	if "false" in rut:
		rut = rut.replace("false", '"false"')
	print(rut)
	#m = json.dumps(rut)
	m = rut
	json_dict = json.loads(m)
	hex = str(json_dict['hex'])
	cmd = "monacoin-cli sendrawtransaction " + hex + ""
	txid = subprocess.check_output( cmd.split(" ") )
	tipamount = str(tipamount)
	tiptoken = str(tiptoken)
	userid = str(userid)
	tipto = str(tipto)
	txid = str(txid)
	deftipamount = str(deftipamount)
	return txid
def gettokenbalance(address):
	address = '"' + address + '"'
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Accept': 'application/json, text/javascript',
	}
	data = '{\
	"jsonrpc":"2.0",\
	"id":0,\
	"method":"get_normalized_balances",\
	"params":{\
	"addresses":[\
	' + address + '\
	]\
	}\
	}'
	response = requests.post('https://wallet.monaparty.me/_api', headers=headers, data=data)

	responsejson = response.json()
	responseresult = responsejson['result']
