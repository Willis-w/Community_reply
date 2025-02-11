# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic.v1 import Field, StrictStr
from linebot.v3.messaging.models.rich_menu_batch_operation import RichMenuBatchOperation

class RichMenuBatchLinkOperation(RichMenuBatchOperation):
    """
    Replace the rich menu with the rich menu specified in the `to` property for all users linked to the rich menu specified in the `from` property.
    """
    var_from: StrictStr = Field(..., alias="from")
    to: StrictStr = Field(...)
    type: str = "link"

    __properties = ["type", "from", "to"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RichMenuBatchLinkOperation:
        """Create an instance of RichMenuBatchLinkOperation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RichMenuBatchLinkOperation:
        """Create an instance of RichMenuBatchLinkOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RichMenuBatchLinkOperation.parse_obj(obj)

        _obj = RichMenuBatchLinkOperation.parse_obj({
            "type": obj.get("type"),
            "var_from": obj.get("from"),
            "to": obj.get("to")
        })
        return _obj

