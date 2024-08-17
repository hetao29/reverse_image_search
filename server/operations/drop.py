import sys

sys.path.append("..")
from config import DEFAULT_COLLECTION


def do_drop(collection, milvus_cli):
    if not collection:
        collection = DEFAULT_COLLECTION
    if not milvus_cli.has_collection(collection):
        return f"Milvus doesn't have a collection named {collection}"
    status = milvus_cli.delete_collection(collection)
    return status
