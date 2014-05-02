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
		settings.TracketAddr = address
		settings.name = code
		settings.uri = uri
		settings.UpstreamBitcoinNode = ('127.0.0.1', p2p_port)
		settings.UpstreamNetworkId = b + str(network_id)
		settings.BitcoinNodeAddresses = ('', upstream_port)
		return True
	except:
		return False
		
rpcsrv = Server((eloipool_config.rpchost:eloipool_config.rpcport))
rpcsrv.add_handler(change_coin)
