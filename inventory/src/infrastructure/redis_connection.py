from redis_om import get_redis_connection

redis_connection = get_redis_connection(
    host="redis-15017.c15.us-east-1-2.ec2.cloud.redislabs.com",
    port=15017,
    password="2kGzWkmPpH7FHkxBxSFSiLVMBIWUHwNJ",
    decode_responses=True
)