from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snake_request_snakes_item import SnakeRequestSnakesItem


T = TypeVar("T", bound="SnakeRequest")


@_attrs_define
class SnakeRequest:
    """
    Attributes:
        snakes (Union[Unset, list['SnakeRequestSnakesItem']]):
    """

    snakes: Union[Unset, list["SnakeRequestSnakesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snakes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snakes, Unset):
            snakes = []
            for snakes_item_data in self.snakes:
                snakes_item = snakes_item_data.to_dict()
                snakes.append(snakes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snakes is not UNSET:
            field_dict["snakes"] = snakes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.snake_request_snakes_item import SnakeRequestSnakesItem

        d = src_dict.copy()
        snakes = []
        _snakes = d.pop("snakes", UNSET)
        for snakes_item_data in _snakes or []:
            snakes_item = SnakeRequestSnakesItem.from_dict(snakes_item_data)

            snakes.append(snakes_item)

        snake_request = cls(
            snakes=snakes,
        )

        snake_request.additional_properties = d
        return snake_request

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
