# -*- coding: UTF-8 -*-

import platform
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
import db_config 

platform_os = platform.system()
config = db_config

uri = 'mongodb://' + config.user + ':' + config.pwd + '@' + config.server + ':' + config.port + '/' + config.db_name

def insert(path, data, operation='append'):
    client = MongoClient(uri)
    resources = client.tangdb.resources
    sequence = client.tangdb.sequence
    print(sequence)
    print(resources)
    seq = sequence.find.one({"_id": "version"})["seq"]
    sequence.update_one({"_id", "version"}, {"$inc": {"seq": 1}})
    post_data = {
            "_class": "com.gionee.smart.domain.entity.Resources", 
            "version": seq, 
            "path": path,
            "content": data, 
            "status": "enable", 
            "operation": operaion,
            "createtime": datetime.now(timezone(timedelta(hours=8)))
    }
    resources.insert(post_data)
