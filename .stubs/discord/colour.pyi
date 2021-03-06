from typing import Any, Tuple, TypeVar, Type

_C = TypeVar('_C', bound=Colour)

class Colour:
    value: int

    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def r(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def b(self) -> int: ...
    def to_rgb(self) -> Tuple[int, int, int]: ...
    @classmethod
    def from_rgb(cls: Type[_C], r: int, g: int, b: int) -> _C: ...
    @classmethod
    def default(cls: Type[_C]) -> _C: ...
    @classmethod
    def teal(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_teal(cls: Type[_C]) -> _C: ...
    @classmethod
    def green(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_green(cls: Type[_C]) -> _C: ...
    @classmethod
    def blue(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_blue(cls: Type[_C]) -> _C: ...
    @classmethod
    def purple(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_purple(cls: Type[_C]) -> _C: ...
    @classmethod
    def magenta(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_magenta(cls: Type[_C]) -> _C: ...
    @classmethod
    def gold(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_gold(cls: Type[_C]) -> _C: ...
    @classmethod
    def orange(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_orange(cls: Type[_C]) -> _C: ...
    @classmethod
    def red(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_red(cls: Type[_C]) -> _C: ...
    @classmethod
    def lighter_grey(cls: Type[_C]) -> _C: ...
    @classmethod
    def dark_grey(cls: Type[_C]) -> _C: ...
    @classmethod
    def light_grey(cls: Type[_C]) -> _C: ...
    @classmethod
    def darker_grey(cls: Type[_C]) -> _C: ...
    @classmethod
    def blurple(cls: Type[_C]) -> _C: ...
    @classmethod
    def greyple(cls: Type[_C]) -> _C: ...

Color = Colour
