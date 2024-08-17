import sys

sys.path.append("..")
from config import DEFAULT_COLLECTION


def do_delete(fileid, collection, milvus_client):
    if not collection:
        collection = DEFAULT_COLLECTION
    milvus_client.delete(collection, "id in [%s]" % fileid)
    return "ok"
