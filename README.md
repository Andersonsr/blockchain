<h1>Blockchain API</h1>
API and blockchain generator developed with 
Python and Flask.

<h2>Usage</h2>
First of all <a href=https://github.com/Andersonsr/blockchain/blob/main/user.py>user.py</a> 
needs to be executed to create 50 random users, 
these users will be needed afterwards to create 
transactions. Users are stored in a directory named 
users, each user is composed of a private key used
to sign each transaction and a public key needed to 
validate the signature, each user is identified by
a hash of the public key (address).

To generate a blockchain the file <a href=https://github.com/Andersonsr/blockchain/blob/main/main.py>main.py</a>
should be executed, by default a blockchain with 10 blocks 
is generated, to persist the generated blockchain the flag -o must 
be used and a name for the generated blockchain must
be given. 

Run main.py --help for more details.


