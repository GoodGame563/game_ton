from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SnakeRequestSnakesItem")


@_attrs_define
class SnakeRequestSnakesItem:
    """
    Attributes:
        id (str): Unique snake identifier Example: 6c1dfac6d106e6f4d0ffdddb665238253574ac1f.
        direction (list[int]): 3D direction [x, y, z] Example: [0, 0, 0].
    """

    id: str
    direction: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        direction = self.direction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "direction": direction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        direction = cast(list[int], d.pop("direction"))

        snake_request_snakes_item = cls(
            id=id,
            direction=direction,
        )

        snake_request_snakes_item.additional_properties = d
        return snake_request_snakes_item

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
