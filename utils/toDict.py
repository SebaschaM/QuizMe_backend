import json
from bson import json_util


def object_as_dict(obj):
    obj_dict = json.loads(json_util.dumps(obj))

    return obj_dict
