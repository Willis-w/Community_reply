# coding: utf-8

"""
    Webhook Type Definition

    Webhook event definition of the LINE Messaging API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic.v1 import BaseModel, Field, conlist
from linebot.v3.webhooks.models.mentionee import Mentionee

class Mention(BaseModel):
    """
    Mention
    """
    mentionees: conlist(Mentionee) = Field(..., description="Array of one or more mention objects. Max: 20 mentions")

    __properties = ["mentionees"]

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
    def from_json(cls, json_str: str) -> Mention:
        """Create an instance of Mention from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in mentionees (list)
        _items = []
        if self.mentionees:
            for _item in self.mentionees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mentionees'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Mention:
        """Create an instance of Mention from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Mention.parse_obj(obj)

        _obj = Mention.parse_obj({
            "mentionees": [Mentionee.from_dict(_item) for _item in obj.get("mentionees")] if obj.get("mentionees") is not None else None
        })
        return _obj

