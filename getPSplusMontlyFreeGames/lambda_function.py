import json
import requests
import extract_data
from db import updateDb, deleteAllRecords, getAllRecords


def lambda_handler(event, context):
    table_name = 'PSPlusMonthlyFreeGames'

    res = None
    # command to update db .. it is only internal
    if 'extract' in event:
        extract_order = event['extract']
        if extract_order == "re_fill_monthly_data":
            free_games_list = extract_data.extract_monthly_plus_free_game()
            delete_First = deleteAllRecords(table_name)
            update_result = updateDb(table_name, free_games_list)
            res = update_result
    else:
        res = getAllRecords(table_name)

    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
