import boto3
import sys
from config import *

rekognition_client = boto3.client('rekognition',region_name=Region.US_EAST_1,
                           aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=Config.AWS_SECERT_ACCESS_KEY)
response = dict()

if len(sys.argv)>1:
    if sys.argv[1] == 'create_collection':
        if sys.argv[2] is not None or sys.argv[2]!='':
            response = rekognition_client.create_collection(
                CollectionId=sys.argv[2]
            )
            print('response >>',response)
        else:
            print('error : collection name is not in args.')
    elif sys.argv[1] == 'delete_collection':
        if sys.argv[2] is not None or sys.argv[2]!='':
            response = rekognition_client.delete_collection(
                CollectionId=sys.argv[2]
            )
            print('response >>',response)
        else:
            print('error : collection name is not in args.')
    elif sys.argv[1] == 'list_faces':
        if sys.argv[2] is not None or sys.argv[2]!='':
            c = 0
            for i in (rekognition_client.list_faces(CollectionId=sys.argv[2]))['Faces']:
                c = c + 1
                print(i)
            print('\nTOTAL FACES INDEXED = ',c)
        else:
            print('error : collection name is not in args.')
    elif sys.argv[1] == 'list_collection':
        print(rekognition_client.list_collections()['CollectionIds'])
    else:
        print('Please enter a valid arguments......\n Example: \n list_collection\n list_faces <collection_name> \n create_collection <collection_name>\n delete_collection <collection_name>\n ')
else:
    print('Please enter a valid arguments......\n Example: \n list_collection\n list_faces <collection_name> \n create_collection <collection_name>\n delete_collection <collection_name>\n ')
