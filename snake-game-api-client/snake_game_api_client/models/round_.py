import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.round_status import RoundStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Round")


@_attrs_define
class Round:
    """
    Attributes:
        name (Union[Unset, str]): Name of the game round Example: final-3.
        start_at (Union[Unset, datetime.datetime]): Round start time in ISO 8601 format Example: 2024-10-12T16:00:00Z.
        end_at (Union[Unset, datetime.datetime]): Round end time in ISO 8601 format Example: 2024-10-12T16:55:00Z.
        duration (Union[Unset, int]): Duration of the round in seconds Example: 3300.
        status (Union[Unset, RoundStatus]): Current status of the round Example: ended.
        repeat (Union[Unset, int]): Number of times the round repeats (0 for no repeat)
    """

    name: Union[Unset, str] = UNSET
    start_at: Union[Unset, datetime.datetime] = UNSET
    end_at: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    status: Union[Unset, RoundStatus] = UNSET
    repeat: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_at: Union[Unset, str] = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        duration = self.duration

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        repeat = self.repeat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if status is not UNSET:
            field_dict["status"] = status
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _start_at = d.pop("startAt", UNSET)
        start_at: Union[Unset, datetime.datetime]
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = isoparse(_start_at)

        _end_at = d.pop("endAt", UNSET)
        end_at: Union[Unset, datetime.datetime]
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at)

        duration = d.pop("duration", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RoundStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RoundStatus(_status)

        repeat = d.pop("repeat", UNSET)

        round_ = cls(
            name=name,
            start_at=start_at,
            end_at=end_at,
            duration=duration,
            status=status,
            repeat=repeat,
        )

        round_.additional_properties = d
        return round_

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
