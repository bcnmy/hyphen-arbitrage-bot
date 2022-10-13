# -*- coding: utf-8 -*-

# -- Sheet --

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json

ethereum = {
    "bico": "0xf17e65822b568b3903685a7c9f496cf7656cc6c2",
    "usdc": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "usdt": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "eth": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
}
    
polygon = {
    "usdc": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "eth" : "0x7ceb23fd6bc0add59e62ac25578270cff1b9f619",
    "bico": "0x91c89a94567980f0e9723b487b0bed586ee96aa7",
    "usdt": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
}

avalanche = {
    "eth": "0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab",
    "usdc": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664"
}

binance = {
    "bico": "0x06250a4962558f0f3e69fc07f4c67bb9c9eac739",
    "eth": "0x2170ed0880ac9a755fd29b2688956bd959f933f8",
    "usdt": "0x55d398326f99059ff775485246999027b3197955",
    "usdc": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"
}

optimism = {
    "usdc": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
    "bico": "0xd6909e9e702024eb93312b989ee46794c0fb1c9d",
    "eth": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" 
}

arbitrum = {
    "bico": "0xa68ec98d7ca870cf1dd0b00ebbb7c4bf60a8e74d",
    "eth": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
    "usdc": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8"
}

fantom = {
    "usdc": "0x04068da6c83afcfa0e13ba15a6696662335d5b75",
    "bico": "0x524cabe5b2f66cbd6f6b08def086f18f8dde033a"
}

async def queries(chain):
    url=f"https://api.thegraph.com/subgraphs/name/shantanu-bico/hyphenv2-liquidity-pool-{chain}"
    transport = AIOHTTPTransport(url)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    hourlyIncentivePoolBalanceLogEntry = gql(
        """
        query hourlyIncentivePoolBalanceLogEntry{
          hourlyIncentivePoolBalances(orderBy: timestamp, orderDirection: desc){
            tokenAddress
            poolBalance
            timestamp
          }
       } 
    """ 
    )
    
    poolbalance_result = await client.execute_async(hourlyIncentivePoolBalanceLogEntry)
    print("Graph calls executed for", chain)
    return poolbalance_result
 
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

poolbalance_result_ethereum = await queries('ethereum')
poolbalance_result_polygon = await queries('polygon')
poolbalance_result_avalanche = await queries('avalanche')
poolbalance_result_binance = await queries('bsc')
poolbalance_result_optimism = await queries('optimism')
poolbalance_result_arbitrum = await queries('arbitrum')
poolbalance_result_fantom = await queries('fantom')

eth_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_ethereum['hourlyIncentivePoolBalances'])):
    for j in ethereum:
        if(poolbalance_result_ethereum['hourlyIncentivePoolBalances'][i]['tokenAddress'] == ethereum[j]):
            if (j=='bico' or j=='eth'):
                eth_dict['Token'].append(j)
                eth_dict['TokenAddress'].append(poolbalance_result_ethereum['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                eth_dict['PoolBalance'].append(float(poolbalance_result_ethereum['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                eth_dict['Token'].append(j)
                eth_dict['TokenAddress'].append(poolbalance_result_ethereum['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                eth_dict['PoolBalance'].append(float(poolbalance_result_ethereum['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

poly_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_polygon['hourlyIncentivePoolBalances'])):
    for j in polygon:
        if(poolbalance_result_polygon['hourlyIncentivePoolBalances'][i]['tokenAddress'] == polygon[j]):
            if (j=='bico' or j=='eth'):
                poly_dict['Token'].append(j)
                poly_dict['TokenAddress'].append(poolbalance_result_polygon['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                poly_dict['PoolBalance'].append(float(poolbalance_result_polygon['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                poly_dict['Token'].append(j)
                poly_dict['TokenAddress'].append(poolbalance_result_polygon['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                poly_dict['PoolBalance'].append(float(poolbalance_result_polygon['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

avax_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_avalanche['hourlyIncentivePoolBalances'])):
    for j in avalanche:
        if(poolbalance_result_avalanche['hourlyIncentivePoolBalances'][i]['tokenAddress'] == avalanche[j]):
            if (j=='eth'  or j=='bico'):
                avax_dict['Token'].append(j)
                avax_dict['TokenAddress'].append(poolbalance_result_avalanche['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                avax_dict['PoolBalance'].append(float(poolbalance_result_avalanche['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                avax_dict['Token'].append(j)
                avax_dict['TokenAddress'].append(poolbalance_result_avalanche['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                avax_dict['PoolBalance'].append(float(poolbalance_result_avalanche['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

bsc_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_binance['hourlyIncentivePoolBalances'])):
    for j in binance:
        if(poolbalance_result_binance['hourlyIncentivePoolBalances'][i]['tokenAddress'] == binance[j]):
            if (j=='eth'  or j=='bico'):
                bsc_dict['Token'].append(j)
                bsc_dict['TokenAddress'].append(poolbalance_result_binance['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                bsc_dict['PoolBalance'].append(float(poolbalance_result_binance['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                bsc_dict['Token'].append(j)
                bsc_dict['TokenAddress'].append(poolbalance_result_binance['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                bsc_dict['PoolBalance'].append(float(poolbalance_result_binance['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
                                                       

opt_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_optimism['hourlyIncentivePoolBalances'])):
    for j in optimism:
        if(poolbalance_result_optimism['hourlyIncentivePoolBalances'][i]['tokenAddress'] == optimism[j]):
            if (j=='eth'  or j=='bico'):
                opt_dict['Token'].append(j)
                opt_dict['TokenAddress'].append(poolbalance_result_optimism['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                opt_dict['PoolBalance'].append(float(poolbalance_result_optimism['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                opt_dict['Token'].append(j)
                opt_dict['TokenAddress'].append(poolbalance_result_optimism['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                opt_dict['PoolBalance'].append(float(poolbalance_result_optimism['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

arb_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'])):
    for j in arbitrum:
        if(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'][i]['tokenAddress'] == arbitrum[j]):
            if (j=='eth'  or j=='bico'):
                arb_dict['Token'].append(j)
                arb_dict['TokenAddress'].append(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                arb_dict['PoolBalance'].append(float(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                arb_dict['Token'].append(j)
                arb_dict['TokenAddress'].append(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                arb_dict['PoolBalance'].append(float(poolbalance_result_arbitrum['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

ftm_dict={"Token":[], "TokenAddress":[], "PoolBalance":[]}

for i in range(len(poolbalance_result_fantom['hourlyIncentivePoolBalances'])):
    for j in fantom:
        if(poolbalance_result_fantom['hourlyIncentivePoolBalances'][i]['tokenAddress'] == fantom[j]):
            if (j=='eth'  or j=='bico'):
                ftm_dict['Token'].append(j)
                ftm_dict['TokenAddress'].append(poolbalance_result_fantom['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                ftm_dict['PoolBalance'].append(float(poolbalance_result_fantom['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e18)
            elif (j=='usdc' or j=='usdt'):
                ftm_dict['Token'].append(j)
                ftm_dict['TokenAddress'].append(poolbalance_result_fantom['hourlyIncentivePoolBalances'][i]['tokenAddress'])
                ftm_dict['PoolBalance'].append(float(poolbalance_result_fantom['hourlyIncentivePoolBalances'][i]['poolBalance'])/1e6)
                                                       

from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('abitragebot-hyphen-d01f28f9449b.json', scope)
client = gspread.authorize(creds)
sheet = client.open('ArbitrageBotData')

#Update Ethereum
current_sheet = sheet.get_worksheet(0)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(eth_dict['TokenAddress'])):
    cell = current_sheet.find(eth_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), eth_dict['PoolBalance'][i])
    
#Update Polygon
current_sheet = sheet.get_worksheet(1)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(poly_dict['TokenAddress'])):
    cell = current_sheet.find(poly_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), poly_dict['PoolBalance'][i])
    
#Update Avalanche
current_sheet = sheet.get_worksheet(2)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(avax_dict['TokenAddress'])):
    cell = current_sheet.find(avax_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), avax_dict['PoolBalance'][i])
    
#Update Binance
current_sheet = sheet.get_worksheet(3)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(bsc_dict['TokenAddress'])):
    cell = current_sheet.find(bsc_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), bsc_dict['PoolBalance'][i])
    
#Update Optimism
current_sheet = sheet.get_worksheet(4)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(opt_dict['TokenAddress'])):
    cell = current_sheet.find(opt_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), opt_dict['PoolBalance'][i])

#Update Arbitrum
current_sheet = sheet.get_worksheet(5)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(arb_dict['TokenAddress'])):
    cell = current_sheet.find(arb_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), arb_dict['PoolBalance'][i])
    
#Update Fantom
current_sheet = sheet.get_worksheet(6)
row=len(current_sheet.get_all_values())+1
next_row = next_available_row(current_sheet)
for i in range(len(ftm_dict['TokenAddress'])):
    cell = current_sheet.find(ftm_dict['TokenAddress'][i])
    col_value=chr(ord('@')+cell.col)
    current_sheet.update_acell(col_value+"{}".format(row), ftm_dict['PoolBalance'][i])

import pandas as pd
df = pd.DataFrame({'Chains':['Ethereum','Polygon', 'Avalanche', 'Binance', 'Optimism', 'Arbitrum', 'Fantom'],
                   '$BICO':[0,0,0,0,0,0,0],
                   '$ETH':[0,0,0,0,0,0,0], 
                   '$USDC':[0,0,0,0,0,0,0],
                   '$USDT':[0,0,0,0,0,0,0]})


df = df.set_index(['Chains'])
df=df.astype(float)

import time
chain_sheet = {"Ethereum": 0, "Polygon": 1, "Avalanche": 2, "Binance": 3, "Optimism": 4, "Arbitrum": 5, "Fantom": 6}
bico_cutoff = 300
eth_cutoff = 0.05
usd_cutoff = 200
pct_cutoff = 20

sheet = client.open('ArbitrageBotData')


def get_arb_values_eth_poly_bsc(chain, df):
    if (chain!="Ethereum" and chain!="Polygon" and chain!="Binance"):
        print("Please enter either Ethereum, Polygon or Binance to continue")
    else: 
        sheet_id = chain_sheet[chain]
        current_sheet = sheet.get_worksheet(sheet_id)

        bico_last = float(current_sheet.acell('I4').value)
        df['$BICO'][sheet_id]=bico_last
        time.sleep(5)
        # bico_pct = float(current_sheet.acell('I5').value)
        eth_last = float(current_sheet.acell('J4').value)
        df['$ETH'][sheet_id]=eth_last
        time.sleep(5)
        # eth_pct = float(current_sheet.acell('J5').value)
        usdc_last = float(current_sheet.acell('K4').value)
        df['$USDC'][sheet_id]=usdc_last
        time.sleep(5)
        # usdc_pct = float(current_sheet.acell('K5').value)
        usdt_last = float(current_sheet.acell('L4').value)
        df['$USDT'][sheet_id]=usdt_last
        time.sleep(5)
        # usdt_pct = float(current_sheet.acell('L5').value)
            
        return df
    
    
def get_arb_values_opt_arb(chain, df):
    if (chain!="Optimism" and chain!="Arbitrum") :
        print("Enter either Optimism or Arbitrum to proceed")
    else:
        sheet_id = chain_sheet[chain]
        current_sheet = sheet.get_worksheet(sheet_id)

        bico_last = float(current_sheet.acell('H4').value)
        df['$BICO'][sheet_id]=bico_last
        time.sleep(5)
        # bico_pct = float(current_sheet.acell('H5').value)
        eth_last = float(current_sheet.acell('I4').value)
        df['$ETH'][sheet_id]=eth_last
        time.sleep(5)
        # eth_pct = float(current_sheet.acell('I5').value)
        usdc_last = float(current_sheet.acell('J4').value)
        df['$USDC'][sheet_id]=usdc_last
        time.sleep(5)
        # usdc_pct = float(current_sheet.acell('J5').value)
            
        return df
    
    
def get_arb_values_ftm(chain, df):
    if (chain!="Fantom") :
        print("Enter Fantom to proceed")
    else:
        sheet_id = chain_sheet[chain]
        current_sheet = sheet.get_worksheet(sheet_id)

        bico_last = float(current_sheet.acell('G4').value)
        df['$BICO'][sheet_id]=bico_last
        time.sleep(5)
        # bico_pct = float(current_sheet.acell('G5').value)
        usdc_last = float(current_sheet.acell('H4').value)
        df['$USDC'][sheet_id]=bico_last
        time.sleep(5)
        # usdc_pct = float(current_sheet.acell('H5').value)
    
        return df
    
    
def get_arb_values_avax(chain, df):
    if (chain!="Avalanche"):
        print("Enter Avalanche to proceed")
    else:
        sheet_id = chain_sheet[chain]
        current_sheet = sheet.get_worksheet(sheet_id)

        eth_last = float(current_sheet.acell('G4').value)
        df['$ETH'][sheet_id]=eth_last
        time.sleep(5)
        # eth_pct = float(current_sheet.acell('G5').value)
        usdc_last = float(current_sheet.acell('H4').value)
        df['$USDC'][sheet_id]=usdc_last
        time.sleep(5)
        # usdc_pct = float(current_sheet.acell('H5').value)
        
        return df

import time
time.sleep(60)
get_arb_values_eth_poly_bsc("Ethereum", df)
time.sleep(60)
get_arb_values_eth_poly_bsc("Polygon", df)
time.sleep(60)
get_arb_values_eth_poly_bsc("Binance", df)
time.sleep(60)
get_arb_values_opt_arb("Optimism", df)
time.sleep(60)
get_arb_values_opt_arb("Arbitrum", df)
time.sleep(60)
get_arb_values_avax("Avalanche", df)
time.sleep(60)
get_arb_values_ftm("Fantom", df)

def myround(x, base):
    return base * round(x/base)

import tweepy
  
# personal details
client_id="WFNRcERtdUo5RHJlWWY3dGNrR1M6MTpjaQ"
client_secret="cRgZAiKr7_MyTw0DE6xtoZDBXWzyFHuzDD7GaP5oGNxSTOKglF"

apikey="AD5XE19ltxaAMTiy7IMTBgPR3"

apikey_secret="oP8qyd7SMrg94iKgxieR6p6hoGWYDiGzh40axOoJfRIWell5Qn"
consumer_key ="NIPqP0WPHIdvCprYw04cOpnNC"
consumer_secret ="kWe7sVb7U7fhvchNJ1XWRqnADDo7uC0CvemzqQ1JEXNP9hXLoN"

access_token ="1550527166664024065-uqYiAFhduUQTBpy8TFxlR3AUU5mzac"
access_token_secret ="iP3pAUFAwD5S3QZ4ExkBuCsuDUvlISO5Rn1dhHJcUQhV0"

bearer_token="AAAAAAAAAAAAAAAAAAAAAAQkgQEAAAAAQpDaqAXCTzilYZhXCicpN7NLs1w%3DHPTZ12FeCbnam3tf9ijTd5NOSd0Csm7W7TisZqRLCThmt40wHk"
  
auth = tweepy.OAuthHandler(apikey, apikey_secret)
  
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
  

alarm = '\U0001F6A8'
hand = '\U0001F449'
moneymouth = '\U0001F911'
chain_id = {"Ethereum": 1, "Polygon": 137, "Avalanche":43114, "Binance":56, "Optimism":10,"Arbitrum":42161, "Fantom":250 }

for i in range(len(df['$BICO'])):
    if (df['$BICO'][i]>bico_cutoff):
        x=list(chain_sheet.keys())[list(chain_sheet.values()).index(i)]
        x=chain_id[x]
        hyphen_link_bico = "https://hyphen.biconomy.io/bridge/{}/{}/BICO".format(x,x)
        msg="{} Arbitrage Opportunity {} \n\n{} Earn upto {} $BICO tokens!! \n\nGo to Hyphen & bridge $BICO from {} to any chain \n\n{} {} \n\nP.S. To check your potential reward amount, hover over ‘total fee’ on the bottom left corner.".format(alarm, alarm, moneymouth, myround(df['$BICO'][i],1), list(chain_sheet.keys())[list(chain_sheet.values()).index(i)], hand, hyphen_link_bico)
        api.update_status(status=msg)
        print(msg)
        
for i in range(len(df['$ETH'])):
    if (df['$ETH'][i]>eth_cutoff):
        x=list(chain_sheet.keys())[list(chain_sheet.values()).index(i)]
        x=chain_id[x]
        hyphen_link_eth = "https://hyphen.biconomy.io/bridge/{}/{}/ETH".format(x,x)
        msg="{} Arbitrage Opportunity {} \n\n{} Earn upto {} $ETH tokens!! \n\nGo to Hyphen & bridge $ETH from {} to any chain \n\n{} {} \n\nP.S. To check your potential reward amount, hover over ‘total fee’ on the bottom left corner.".format(alarm, alarm, moneymouth, myround(df['$ETH'][i],0.05), list(chain_sheet.keys())[list(chain_sheet.values()).index(i)], hand, hyphen_link_eth)
        api.update_status(status=msg)
        print(msg)

        
for i in range(len(df['$USDC'])):
    if (df['$USDC'][i]>usd_cutoff):
        x=list(chain_sheet.keys())[list(chain_sheet.values()).index(i)]
        x=chain_id[x]
        hyphen_link_usdc = "https://hyphen.biconomy.io/bridge/{}/{}/USDC".format(x,x)
        msg="{} Arbitrage Opportunity {} \n\n{} Earn upto {} $USDC tokens!! \n\nGo to Hyphen & bridge $USDC from {} to any chain \n\n{} {} \n\nP.S. To check your potential reward amount, hover over ‘total fee’ on the bottom left corner.".format(alarm, alarm, moneymouth, myround(df['$USDC'][i],1), list(chain_sheet.keys())[list(chain_sheet.values()).index(i)], hand, hyphen_link_usdc)
        api.update_status(status=msg)
        print(msg)
        
for i in range(len(df['$USDT'])):
    if (df['$USDT'][i]>usd_cutoff):
        x=list(chain_sheet.keys())[list(chain_sheet.values()).index(i)]
        x=chain_id[x]
        hyphen_link_usdt = "https://hyphen.biconomy.io/bridge/{}/{}/USDT".format(x,x)
        msg="{} Arbitrage Opportunity {} \n\n{} Earn upto {} $USDT tokens!! \n\nGo to Hyphen & bridge $USDT from {} to any chain \n\n{} {} \n\nP.S. To check your potential reward amount, hover over ‘total fee’ on the bottom left corner.".format(alarm, alarm, moneymouth, myround(df['$USDT'][i],1), list(chain_sheet.keys())[list(chain_sheet.values()).index(i)], hand, hyphen_link_usdt)
        api.update_status(status=msg)
        print(msg)


