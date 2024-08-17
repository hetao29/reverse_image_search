import sys

sys.path.append("..")
from config import DEFAULT_COLLECTION


def do_delete(fileid, collection, milvus_client):
    if not collection:
        collection = DEFAULT_COLLECTION
    milvus_client.delete(collection, "fileid in [%s]" % fileid)
    return "ok"
