from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snake_status import SnakeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Snake")


@_attrs_define
class Snake:
    """
    Attributes:
        id (Union[Unset, str]): Unique snake identifier Example: db59f7bff43351d69b540c666fa8ff9f1c81f05c.
        direction (Union[Unset, list[int]]): Current direction vector [x, y, z] Example: [1, 0, 0].
        old_direction (Union[Unset, list[int]]): Previous direction vector [x, y, z] Example: [0, 0, -1].
        geometry (Union[Unset, list[list[int]]]): Snake body segments coordinates
        death_count (Union[Unset, int]): Number of times snake died Example: 16.
        status (Union[Unset, SnakeStatus]): Current snake status Example: alive.
        revive_remain_ms (Union[Unset, int]): Milliseconds remaining until revival if dead
    """

    id: Union[Unset, str] = UNSET
    direction: Union[Unset, list[int]] = UNSET
    old_direction: Union[Unset, list[int]] = UNSET
    geometry: Union[Unset, list[list[int]]] = UNSET
    death_count: Union[Unset, int] = UNSET
    status: Union[Unset, SnakeStatus] = UNSET
    revive_remain_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        direction: Union[Unset, list[int]] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction

        old_direction: Union[Unset, list[int]] = UNSET
        if not isinstance(self.old_direction, Unset):
            old_direction = self.old_direction

        geometry: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = []
            for geometry_item_data in self.geometry:
                geometry_item = geometry_item_data

                geometry.append(geometry_item)

        death_count = self.death_count

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        revive_remain_ms = self.revive_remain_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if old_direction is not UNSET:
            field_dict["oldDirection"] = old_direction
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if death_count is not UNSET:
            field_dict["deathCount"] = death_count
        if status is not UNSET:
            field_dict["status"] = status
        if revive_remain_ms is not UNSET:
            field_dict["reviveRemainMs"] = revive_remain_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        direction = cast(list[int], d.pop("direction", UNSET))

        old_direction = cast(list[int], d.pop("oldDirection", UNSET))

        geometry = []
        _geometry = d.pop("geometry", UNSET)
        for geometry_item_data in _geometry or []:
            geometry_item = cast(list[int], geometry_item_data)

            geometry.append(geometry_item)

        death_count = d.pop("deathCount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SnakeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SnakeStatus(_status)

        revive_remain_ms = d.pop("reviveRemainMs", UNSET)

        snake = cls(
            id=id,
            direction=direction,
            old_direction=old_direction,
            geometry=geometry,
            death_count=death_count,
            status=status,
            revive_remain_ms=revive_remain_ms,
        )

        snake.additional_properties = d
        return snake

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
