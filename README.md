<h1>Blockchain API</h1>
API and blockchain generator developed with 
Python and Flask. After generated each block can be writen
to a json file that looks like <a href=https://github.com/Andersonsr/blockchain/blob/main/output_example.json>this</a>.
After creating some blockchains the API can be hosted locally 
to query the generated data.

<h2>Prerequisites</h2> 
the following commands will install any dependencies needed 
to run the application
```
pip install pycryptodome
pip install flask
pip install flask_api
pip install base58
```


<h2>Usage</h2>
First of all <a href=https://github.com/Andersonsr/blockchain/blob/main/user.py>user.py</a> 
needs to be executed to create 50 random users, 
these users will be needed afterwards to create 
transactions. Users are stored in a directory named 
users, each user is composed of a private key used
to sign each transaction and a public key needed to 
validate the signature, each user is identified by
a hash of the public key (address).

```
python user.py
```

To generate a blockchain the file <a href=https://github.com/Andersonsr/blockchain/blob/main/main.py>main.py</a>
should be executed, by default a blockchain with 10 blocks 
is generated, to persist the generated blockchain the flag -o must 
be used and a name for the generated blockchain must
be given as show bellow.

```
python main.py -o blockchain_example
```

To run the API the following command line need to be issued.


```
python main.py --app
```

