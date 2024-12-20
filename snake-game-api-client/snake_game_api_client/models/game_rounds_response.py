import datetime
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.round_ import Round


T = TypeVar("T", bound="GameRoundsResponse")


@_attrs_define
class GameRoundsResponse:
    """
    Attributes:
        game_name (str): Name of the game Example: snake3d.
        rounds (list['Round']): List of game rounds
        now (datetime.datetime): Current server time in ISO 8601 format Example: 2024-12-19T10:45:45.632269185Z.
    """

    game_name: str
    rounds: list["Round"]
    now: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_name = self.game_name

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        now = self.now.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gameName": game_name,
                "rounds": rounds,
                "now": now,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.round_ import Round

        d = src_dict.copy()
        game_name = d.pop("gameName")

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = Round.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        now = isoparse(d.pop("now"))

        game_rounds_response = cls(
            game_name=game_name,
            rounds=rounds,
            now=now,
        )

        game_rounds_response.additional_properties = d
        return game_rounds_response

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
