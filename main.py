from datetime import date

from pydantic import BaseModel, ConfigDict, ValidationError


class Event(BaseModel):
    model_config = ConfigDict(strict=True)

    when: date
    where: tuple[int, int]


json_data = '{"when": "1987-01-28", "where": [51, -1]}'
print(Event.model_validate_json(json_data))  

# import json
# from pprint import pprint
# import logfire
# from pydantic import BaseModel, ConfigDict, ValidationError

# class DCATBaseObj(BaseModel):
#     model_config = ConfigDict(strict=True)

#     conformsTo: str
#     datasets: list


# dcat = None
# json_data = '{"conformsTo": "some value", datasets: []}'
# dcat = DCATBaseObj.model_validate_json(json_data)
# with open("dcat_minimum.json", "r") as f:
#     dcat = DCATBaseObj.model_validate_json(json.load(f))

# pprint(dcat)

# logfire.configure()
# logfire.instrument_pydantic()  

# json_obj = None
# with open("dcat_minimum.json", "r") as f:
#     json_obj = json.load(f)


# class Delivery(BaseModel):
#     timestamp: datetime
#     dimensions: tuple[int, int]

# obj = type('DCAT', (object,), json_obj)
# obj_inst = obj()
# pprint(obj_inst)
# pprint(dir(obj_inst))