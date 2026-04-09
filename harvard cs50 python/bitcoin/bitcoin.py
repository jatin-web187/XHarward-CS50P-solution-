import requests
import sys
import json
try:
    if len(sys.argv)!=2:
        print("Missing command line-argument")
        sys.exit(1)
    else:
        sys.argv[1]=float(sys.argv[1])
except ValueError:
    print("Command line argument is not a number")
    sys.exit(1)
response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2f07fdd2d3ed2bc63642bfd34bf67e047337d90d35d0a6db459eace7ff6e9eb5")
object=response.json()
rate=float(object["data"]["priceUsd"])
num=sys.argv[1]
amount=num*rate
print(f"${amount:,.4f}")
