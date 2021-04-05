
1) first create 42 api application here:
https://profile.intra.42.fr/oauth/applications

2) then create .env file here and in ./node with the uid and secret

3) then do:

set -a; source .env; set +a

(cf https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-value-pairs/30969768#30969768)

4) you can then run the python code from python/main.py in an interactive python3 console.


