import requests
from lxml import html
import urllib.request


def get_psn_player_stats(player_id):

    player_stats = {}
    stats_url = "https://psnprofiles.com/{0}/stats".format(player_id)

    req = None
    try:
        req = requests.get(stats_url)
        if req.status_code == 200:
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
            print("Log status_code error here")
            return req.status_code
    except:
        print("Log fatel error here")
        return req.status_code

    return player_stats


if __name__ == '__main__':
    stats = get_psn_player_stats("lxzero13")
    print(stats)