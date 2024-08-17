import sys

sys.path.append("..")
from config import DEFAULT_COLLECTION


def do_create(collection, milvus_client):
    if not collection:
        collection = DEFAULT_COLLECTION
    try:
        milvus_client.create_collection(collection)
        milvus_client.create_index(collection)
    except Exception as e:
        raise e
