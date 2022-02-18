#! /usr/bin/env python3

#https://developer.okta.com/docs/reference/api/system-log/#polling-requests
#https://developer.okta.com/docs/reference/api/system-log/#transferring-data-to-a-separate-system


import json
import requests
from datetime import datetime, timezone
import urllib3
from time import sleep
from loggingHelper import logger
import configparser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()
config.read('okta.conf')

headers = {'Authorization': f"SSWS {config['okta']['token']}"}

since = datetime.isoformat(datetime.utcnow())
jsonLogsFile = open('log.json','a')

urlLogsAPI = config['okta']['host'] + f'/api/v1/logs?since={since}'

def get_next_link(header):
    return header['link'].split(',')[1].split(';')[0][2:-1]

while True:
    r = requests.get(urlLogsAPI, headers=headers, verify=False)
    logger.info(f"Request endpoint URL={urlLogsAPI} Status code={r.status_code}")

    for log in r.json():
        logger.info(f"New log, date={str(log['published'])}") 
        jsonLogsFile.write(f'{json.dumps(log)}\n')
    urlLogsAPI = get_next_link(r.headers)
    sleep(60)
