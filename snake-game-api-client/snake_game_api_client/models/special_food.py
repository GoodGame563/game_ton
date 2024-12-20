from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpecialFood")


@_attrs_define
class SpecialFood:
    """
    Attributes:
        golden (Union[Unset, list[list[int]]]): Array of golden food items
        suspicious (Union[Unset, list[list[int]]]): Array of suspicious food items
    """

    golden: Union[Unset, list[list[int]]] = UNSET
    suspicious: Union[Unset, list[list[int]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        golden: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.golden, Unset):
            golden = []
            for golden_item_data in self.golden:
                golden_item = golden_item_data

                golden.append(golden_item)

        suspicious: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.suspicious, Unset):
            suspicious = []
            for suspicious_item_data in self.suspicious:
                suspicious_item = suspicious_item_data

                suspicious.append(suspicious_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if golden is not UNSET:
            field_dict["golden"] = golden
        if suspicious is not UNSET:
            field_dict["suspicious"] = suspicious

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        golden = []
        _golden = d.pop("golden", UNSET)
        for golden_item_data in _golden or []:
            golden_item = cast(list[int], golden_item_data)

            golden.append(golden_item)

        suspicious = []
        _suspicious = d.pop("suspicious", UNSET)
        for suspicious_item_data in _suspicious or []:
            suspicious_item = cast(list[int], suspicious_item_data)

            suspicious.append(suspicious_item)

        special_food = cls(
            golden=golden,
            suspicious=suspicious,
        )

        special_food.additional_properties = d
        return special_food

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
