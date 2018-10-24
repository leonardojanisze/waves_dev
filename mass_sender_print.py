
import argparse
import os.path
import json
import pywaves as pw

#----------------CONFIG - START
P_KEY = ''  #Privat key wallet
assetID = "" #asset for airdrop
textoattachment = '' #attachment
DEFAULT_TX_FEE = '100000' #Default fee
#----------------CONFIG - END
pw.setNode("http://149.28.240.181:6869","mainnet")
parser = argparse.ArgumentParser(description='Order tool')
parser.add_argument('file', type=str, help='file with the list of recipients, and amount (wallet:amount) ')

args = parser.parse_args()
filename = args.file
soma_amount = 0
soma_wallet = 0
soma_amount_total = 0
soma_wallet_total = 0
tx_number = 0
soma_fee_total = 0
fee = 0
if not os.path.exists(filename):
    print("File not found!")
else:
    with open(filename) as json_file:
        print '\033[47m'+'\033[1m'+'\033[30m'+'Airdrop For Wavess Plataform \n'+'\033[0;0m'

        json_data = json.load(json_file)
        print('\033[47m'+'\033[1m'+'\033[31m')
        print(json_data[0])
        print('\n'+'\033[0;0m')
        #----SET PRIVATEKEY - START
        address = pw.Address(privateKey = P_KEY)
        #----SET PRIVATEKEY - END
        for transfer in json_data[1]:
            tx_number += 1
            soma_amount = 0
            soma_wallet = 0

            print('\n \n \n --------- Calculating TX # %i ---------' % tx_number)
            for txs in transfer:
                if txs['recipient'] != None:
                    soma_wallet += 1
                    pass
                soma_amount += txs['amount']

                pass


            try:

                fee = address.massTransferAssets(transfer, pw.Asset(assetID) ,attachment=textoattachment)['fee']

                print('fee spent TX: %8f' % (fee / 1e8))
                print('Total assets TX: %i' % soma_amount)
                print('Total Wallets received asset in TX: %i' % soma_wallet)
                soma_amount_total += soma_amount
                soma_wallet_total += soma_wallet
                soma_fee_total += fee
                print('--------- Send TX # %i ---------' % tx_number)
                pass
            except Exception as e:
                print('\033[41m'+'\033[1m'+'\033[37m'+'Unfortunately some error occured!! \n'+'\033[0;0m')
                raise
            pass

        pass
    print('\n \n \nTotal assets sended: %i' % soma_amount_total)
    print('Number of Wallets received asset:  %i' % soma_wallet_total)
    print('Total of fee in waves:  %8f' % (soma_fee_total / 1e8))
    print('Airdrop completed! \n')
