import json
import boto3


def initDb():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb


def deleteAllRecords(tableName):
    client = initDb()

    targetTable = client.Table(tableName)

    response = targetTable.scan()

    if 'Items' in response:
        items = response['Items']

        for i in items:
            targetTable.delete_item(Key={'id': i['id'], 'name': i['name']})
    else:
        items = ['No Items Deleted Or Error.']

    return items


def getAllRecords(tableName):
    client = initDb()

    targetTable = client.Table(tableName)

    response = targetTable.scan()

    if 'Items' in response:
        items = response['Items']
    else:
        items = ['No Items Found Or Error.']

    return items


def updateDb(tableName, obj):
    client = initDb()

    targetTable = client.Table(tableName)

    try:
        for item in obj:
            targetTable.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted new montyly games!')
        }
    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Error saving the free games')
        }