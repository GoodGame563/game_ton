from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enemy import Enemy
    from ..models.food import Food
    from ..models.snake import Snake
    from ..models.special_food import SpecialFood


T = TypeVar("T", bound="GameState")


@_attrs_define
class GameState:
    """
    Attributes:
        map_size (Union[Unset, list[int]]): Map dimensions [width, height, depth] Example: [180, 180, 30].
        name (Union[Unset, str]): Game instance name Example: CleanCrib envious.
        points (Union[Unset, int]): Current score Example: 275.
        fences (Union[Unset, list[list[int]]]): Array of fence coordinates
        snakes (Union[Unset, list['Snake']]): Array of snakes in the game
        enemies (Union[Unset, list['Enemy']]): Array of enemies in the game
        food (Union[Unset, list['Food']]): Array of regular food items
        special_food (Union[Unset, SpecialFood]):
        turn (Union[Unset, int]): Current game turn number Example: 1548.
        revive_timeout_sec (Union[Unset, int]): Seconds until snake revival Example: 5.
        tick_remain_ms (Union[Unset, int]): Milliseconds remaining in current turn Example: 60.
        errors (Union[Unset, list[str]]): Array of error messages if any
    """

    map_size: Union[Unset, list[int]] = UNSET
    name: Union[Unset, str] = UNSET
    points: Union[Unset, int] = UNSET
    fences: Union[Unset, list[list[int]]] = UNSET
    snakes: Union[Unset, list["Snake"]] = UNSET
    enemies: Union[Unset, list["Enemy"]] = UNSET
    food: Union[Unset, list["Food"]] = UNSET
    special_food: Union[Unset, "SpecialFood"] = UNSET
    turn: Union[Unset, int] = UNSET
    revive_timeout_sec: Union[Unset, int] = UNSET
    tick_remain_ms: Union[Unset, int] = UNSET
    errors: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_size: Union[Unset, list[int]] = UNSET
        if not isinstance(self.map_size, Unset):
            map_size = self.map_size

        name = self.name

        points = self.points

        fences: Union[Unset, list[list[int]]] = UNSET
        if not isinstance(self.fences, Unset):
            fences = []
            for fences_item_data in self.fences:
                fences_item = fences_item_data

                fences.append(fences_item)

        snakes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snakes, Unset):
            snakes = []
            for snakes_item_data in self.snakes:
                snakes_item = snakes_item_data.to_dict()
                snakes.append(snakes_item)

        enemies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enemies, Unset):
            enemies = []
            for enemies_item_data in self.enemies:
                enemies_item = enemies_item_data.to_dict()
                enemies.append(enemies_item)

        food: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.food, Unset):
            food = []
            for food_item_data in self.food:
                food_item = food_item_data.to_dict()
                food.append(food_item)

        special_food: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.special_food, Unset):
            special_food = self.special_food.to_dict()

        turn = self.turn

        revive_timeout_sec = self.revive_timeout_sec

        tick_remain_ms = self.tick_remain_ms

        errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_size is not UNSET:
            field_dict["mapSize"] = map_size
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if fences is not UNSET:
            field_dict["fences"] = fences
        if snakes is not UNSET:
            field_dict["snakes"] = snakes
        if enemies is not UNSET:
            field_dict["enemies"] = enemies
        if food is not UNSET:
            field_dict["food"] = food
        if special_food is not UNSET:
            field_dict["specialFood"] = special_food
        if turn is not UNSET:
            field_dict["turn"] = turn
        if revive_timeout_sec is not UNSET:
            field_dict["reviveTimeoutSec"] = revive_timeout_sec
        if tick_remain_ms is not UNSET:
            field_dict["tickRemainMs"] = tick_remain_ms
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.enemy import Enemy
        from ..models.food import Food
        from ..models.snake import Snake
        from ..models.special_food import SpecialFood

        d = src_dict.copy()
        map_size = cast(list[int], d.pop("mapSize", UNSET))

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        fences = []
        _fences = d.pop("fences", UNSET)
        for fences_item_data in _fences or []:
            fences_item = cast(list[int], fences_item_data)

            fences.append(fences_item)

        snakes = []
        _snakes = d.pop("snakes", UNSET)
        for snakes_item_data in _snakes or []:
            snakes_item = Snake.from_dict(snakes_item_data)

            snakes.append(snakes_item)

        enemies = []
        _enemies = d.pop("enemies", UNSET)
        for enemies_item_data in _enemies or []:
            enemies_item = Enemy.from_dict(enemies_item_data)

            enemies.append(enemies_item)

        food = []
        _food = d.pop("food", UNSET)
        for food_item_data in _food or []:
            food_item = Food.from_dict(food_item_data)

            food.append(food_item)

        _special_food = d.pop("specialFood", UNSET)
        special_food: Union[Unset, SpecialFood]
        if isinstance(_special_food, Unset):
            special_food = UNSET
        else:
            special_food = SpecialFood.from_dict(_special_food)

        turn = d.pop("turn", UNSET)

        revive_timeout_sec = d.pop("reviveTimeoutSec", UNSET)

        tick_remain_ms = d.pop("tickRemainMs", UNSET)

        errors = cast(list[str], d.pop("errors", UNSET))

        game_state = cls(
            map_size=map_size,
            name=name,
            points=points,
            fences=fences,
            snakes=snakes,
            enemies=enemies,
            food=food,
            special_food=special_food,
            turn=turn,
            revive_timeout_sec=revive_timeout_sec,
            tick_remain_ms=tick_remain_ms,
            errors=errors,
        )

        game_state.additional_properties = d
        return game_state

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
