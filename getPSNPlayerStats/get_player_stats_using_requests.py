import json
import requests
import http.client
from lxml import html
import urllib.request


def lambda_handler(event, context):
    print(event)
    player_stats = {}
    status_code_res = 200

    player_id = event['player_id']
    stats_url = "https://psnprofiles.com/{0}/stats".format(player_id)

    req = None
    try:
        req = requests.get(stats_url)
        if req.status_code == 200:
            x = 0
            h = html.fromstring(req.text)
            elements = h.xpath('.//div[@class="stats flex"]/span')
            for ele in elements:
                ele = ele.xpath('.//text()')
                ele = [x.strip() for x in ele]
                ele = [x.strip() for x in ele if x != '']
                if len(ele) == 2:
                    player_stats[ele[1]] = ele[0]
                else:
                    print("Log error here")
        else:
            status_code_res = req.status_code
    except:
        status_code_res = req.status_code

    return {
        'statusCode': status_code_res,
        'body': json.dumps(player_stats)
    }
