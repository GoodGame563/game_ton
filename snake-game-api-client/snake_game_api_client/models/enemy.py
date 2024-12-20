from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enemy_status import EnemyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Enemy")


@_attrs_define
class Enemy:
    """
    Attributes:
        geometry (Union[Unset, list[list[int]]]): Enemy body segments coordinates
        status (Union[Unset, EnemyStatus]):  Example: alive.
        kills (Union[Unset, int]): Number of kills by this enemy
    """

    geometry: Union[Unset, list[list[int]]] = UNSET
    status: Union[Unset, EnemyStatus] = UNSET
    kills: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geometry: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = []
            for geometry_item_data in self.geometry:
                geometry_item = geometry_item_data

                geometry.append(geometry_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        kills = self.kills

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if status is not UNSET:
            field_dict["status"] = status
        if kills is not UNSET:
            field_dict["kills"] = kills

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        geometry = []
        _geometry = d.pop("geometry", UNSET)
        for geometry_item_data in _geometry or []:
            geometry_item = cast(list[int], geometry_item_data)

            geometry.append(geometry_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EnemyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EnemyStatus(_status)

        kills = d.pop("kills", UNSET)

        enemy = cls(
            geometry=geometry,
            status=status,
            kills=kills,
        )

        enemy.additional_properties = d
        return enemy

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
