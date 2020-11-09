# Скрипт для получения списка подсетей определенной ASN

import bigdatacloudapi
import json

apiKey = '5abdae5f5a494859b11a266cf28a17f3' # XXX being your api key found at: https://www.bigdatacloud.net/customer/account

client = bigdatacloudapi.Client(apiKey)

resultObject,httpResponseCode = client.getPrefixesList({"bogonsOnly":"false","batchSize":"1000","offset":"0","asn":"16625"})

for item in resultObject['prefixes']:
    for key, value in item.items():
        if key=='bgpPrefix':
            print(value)
