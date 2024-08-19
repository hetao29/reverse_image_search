import sys
import json

sys.path.append("..")

def do_update(uploadImagesModel, img_path, model, milvus_client):
    collection = uploadImagesModel.collection

    feat = model.resnet50_extract_feat(img_path)
    record = {
            'vectors': feat,
            'fileid': uploadImagesModel.fileid,
            'itemid': uploadImagesModel.itemid,
            'tags': uploadImagesModel.tags,
            'brief': uploadImagesModel.brief,
            }
    if uploadImagesModel.tags is None:
        record['tags'] = []
    if uploadImagesModel.brief is None:
        record['brief'] = {}
    try:
        return milvus_client.insert(collection, record)
    except Exception as e:
        milvus_client.delete(collection, "fileid in [%s]" % ids[0])
        raise e
