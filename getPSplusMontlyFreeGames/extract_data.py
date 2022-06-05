import json
import requests


def extract_monthly_plus_free_game():

    free_games_list = []
    target_url = "https://psprices.com/api/v1/game/?region_id=2&platforms=PS5%2CPS4&limit=18&ordering=-last_update_date&is_plus_free_game=true&top_category=game&filter_user=false"

    req = requests.get(target_url)
    if req.status_code == 200:
        json_res = json.loads(req.text)
        if 'results' in json_res:
            results = json_res['results']
            for result in results:

                free_game = dict()
                free_game['id'] = str(result['id'])
                free_game['name'] = result['name']
                free_game['platforms'] = result['platforms']
                free_game['cover'] = result['cover']
                free_game['end_date'] = result['last_update']['end_date']
                free_game['old_price'] = result['last_update']['price_old']
                free_games_list.append(free_game)

        else:
            return ['Results not found']
    else:
        return ['Error:' + req.status_code]

    return free_games_list


if __name__ == '__main__':
    stats = extract_monthly_plus_free_game()
    print(stats)
