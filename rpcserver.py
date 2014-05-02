'''
JSON RPC Server Created For EloiPool By Ahmed Bodiwala
This Project is CLOSED SOURCE and MAY NOT be copied
'''

from jsonrpctcp.server import Server
from jsonrpctcp import config
import config as eloipool_config

config.verbose = True

def change_coin(address, code, uri, p2p_port, network_id, upstream_port):
	try:
		f.open(config.py, w)
		f.write("Server Name = 'CryptoPools.com'")
		f.write("ShareTarget = 0x0000ffff00000000000000000000000000000000000000000000000000000000")
		f.write("DynamicTargetting = 1")
		f.write("DynamicTargetGoal = 10")
		f.write("DynamicTargetWindow = 300")
		f.write("WorkQueueSizeRegular = (0x100, 0x1000)")
		f.write("WorkQueueSizeClear = (0x1000, 0x2000)")
		f.write("WorkQueueSizeLongpoll = (0x1000, 0x2000)")
		f.write("MinimumTxnUpdateWait = 5")
		f.write("TxnUpdateRetryWait = 1")
		f.write("IdleSleepTime = 0.1")
		f.write("TrackerAddr = {}".format(address))
		f.write("UpstreamURI = {}".format(uri))
		f.write("DelayLogForUpstream = True")
		f.write("UpstreamBitcoindNode = ('127.0.0.1', {})".format(p2p_port))
		f.write("UpstreamNetworkId = b'{}'".format(network_id))
		f.write("SecretUser = ''")
		f.write("GotWorkURI = ''")
		f.write("GotWorkTarget = 0x0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
		f.write("POT = 0")
		f.write("Greedy = False")
		f.write("JSONRPCAddresses = (('::ffff:176.119.27.170', 8344),)")
		f.write("StratumAddresses = (('::ffff:176.119.27.170', 3333),)")
		f.write("BitcoinNodeAddresses = (('::ffff:176.119.27.170', {}),)".format(upstream_port))
		f.write("TrustedForwarders = ('::ffff:127.0.0.1',)")
		f.write("ShareLogging = ({'type': 'logfile', 'filename': 'share-logfile', 'format': "{time} {Q(remoteHost)} {username} {YN(not(rejectReason))} {dash(YN(upstreamResult))} {dash(rejectReason)} {solution}\n),)")
		f.write("Authentication =  ({'module': 'allowall',},)")
		f.write("LogFile = 'filename.log')
		f.close()
		return True
	except:
		return False
		
rpcsrv = Server(('127.0.0.1':9001))
rpcsrv.add_handler(change_coin)
rpcsrv.serve_forever()
