import json
import http.client
from lxml import html


def lambda_handler(event, context):
    print(event)
    player_stats = {}
    status_code_res = 200

    player_id = event['player_id']
    coco = 'psnprofiles.com'
    stats_url = "/{0}/stats".format(player_id)

    req = None

    try:

        conn = http.client.HTTPSConnection(coco)
        conn.request("GET", stats_url)
        r1 = conn.getresponse()
        data = r1.read()

        h = html.fromstring(data)
        elements = h.xpath('.//div[@class="stats flex"]/span')
        for ele in elements:
            ele = ele.xpath('.//text()')
            ele = [x.strip() for x in ele]
            ele = [x.strip() for x in ele if x != '']
            if len(ele) == 2:
                player_stats[ele[1]] = ele[0]
            else:
                print("Log error here")

    except:
        status_code_res = req.status_code

    return {
        'statusCode': status_code_res,
        'body': json.dumps(player_stats)
    }
