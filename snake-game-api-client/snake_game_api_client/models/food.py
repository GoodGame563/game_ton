from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Food")


@_attrs_define
class Food:
    """
    Attributes:
        c (Union[Unset, list[int]]): 3D point coordinates [x, y, z] Example: [152, 51, 10].
        points (Union[Unset, int]): Points value of this food Example: 6.
    """

    c: Union[Unset, list[int]] = UNSET
    points: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        c: Union[Unset, list[int]] = UNSET
        if not isinstance(self.c, Unset):
            c = self.c

        points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c is not UNSET:
            field_dict["c"] = c
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        c = cast(list[int], d.pop("c", UNSET))

        points = d.pop("points", UNSET)

        food = cls(
            c=c,
            points=points,
        )

        food.additional_properties = d
        return food

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
