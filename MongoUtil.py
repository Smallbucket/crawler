# -*- coding: UTF-8 -*-

import platform
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
import db_config 

platform_os = platform.system()
config = db_config

uri='mongodb://tang:123456@127.0.0.1:27017/?authSource=tangdb&authMechanism=SCRAM-SHA-256'
#uri = 'mongodb://' + config.user + ':' + config.pwd + '@' + config.server + ':' + config.port + '/?authSource=' + config.db_name + '&authMechanism=SCRAM-SHA-256'
print(uri)
def insert(path, data, operation='append'):
    client = MongoClient(uri)
    db = client.tangdb
    resources = db.resources
    sequence = db.sequence
    print(sequence)
    print(resources)
    seq = sequence.find_one({"_id": "version"})["seq"]
    print(seq)
    sequence.update_one({"_id": "version"}, {"$inc": {"seq": 1}})
    post_data = {
            "_class": "com.gionee.smart.domain.entity.Resources", 
            "version": seq, 
            "path": path,
            "content": data, 
            "status": "enable", 
            "operation": operation,
            "createtime": datetime.now(timezone(timedelta(hours=8)))
    }
    resources.insert(post_data)
