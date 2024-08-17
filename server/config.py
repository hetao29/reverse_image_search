import os

############### Milvus Configuration ###############
MILVUS_HOST = os.getenv("MILVUS_HOST", "10.30.108.248")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
VECTOR_DIMENSION = int(os.getenv("VECTOR_DIMENSION", "2048"))
METRIC_TYPE = os.getenv("METRIC_TYPE", "L2")
DEFAULT_COLLECTION = os.getenv("DEFAULT_COLLECTION", "milvus_img_search")

############### Data Path ###############
UPLOAD_PATH = os.getenv("UPLOAD_PATH", "tmp/search-images")
DATE_FORMAT = os.getenv("DATE_FORMAT", "%Y-%m-%d %H:%M:%S")

############### Number of log files ###############
LOGS_NUM = int(os.getenv("logs_num", "0"))
