# Shared Wallet Bitcoin RPC Plugin

Bitcoin RPC plugin for the Deginner Shared Wallet project. Allows sending, receiving, and other generic wallet functionality using Bitcoind over RPC.

# Installation

This plugin requires 2 installation steps. The first installs the python package and the second inserts empty balance records into the database.

```
python setup.py install
python install.py
```

# Configuration

This plugin expects a desw.ini configuration file. See `example_cfg.ini` for an example. Like other TAPPs, this file is expected to be in `/etc/tapp` on *nix systems.

The most relevant part for this plugin is the bitcoin configuration, which includes the RPC connection URL, a confirmation requirement, the transaction fee, and supported currencies.

```
[bitcoin]
RPCURL: http://bitcoinrpc:pass@127.0.0.1:8332
CONFS: 3
FEE: 0.0001
CURRENCIES: ["BTC"]
```

### Bitcoin.conf

Additionally, you will need to configure dashd to accept RPC requests, and to notify `desw_bitcoin` about blocks and transactions. Below is an example `bitcoin.conf` file.

```
rpcuser=bitcoinrpc
rpcpassword=testbitcoin
allowip=127.0.0.1
rpcport=19332
listen=1
server=1
daemon=1
testnet=1
walletnotify=/usr/bin/python /desw-install-location/desw-bitcoin/desw_bitcoin.py transaction %s
blocknotify=/usr/bin/python /desw-install-location/desw-bitcoin/desw_bitcoin.py block %s
```

Remember that the bitcoind process also needs to be configured like the rest of desw. Most importantly, the desw.ini file must be accessible.

# Testing

This project requires 2 bitcoin testnet nodes. The first should be configured for normal `desw_bitcoin` use, and the second in the `BITCOIN` variable of the `test` section in the config file. Both should have a nominal (>0.5 coin) balance.

```
[test]
BITCOIN: http://bitcoinrpc:testpass@remote.server.com:18332
```