"""
Generated by open_horadric. DO NOT EDIT!
"""

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Tuple

from google.protobuf.internal.containers import MessageMap
from google.protobuf.message import Message

__all__ = ('TestMessage', 'TestEnum')


class TestMessage(Message):
    class TestNestedMessage(Message):
        def __init__(
                self,
                *,
                bar: str = '',
        ) -> None: ...

        bar: str

        @classmethod
        def FromString(cls, s: bytes) -> TestMessage.TestNestedMessage: ...
        def MergeFrom(self, other_msg: Message) -> None: ...
        def CopyFrom(self, other_msg: Message) -> None: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str) -> None: ...
        def WhichOneof(self, oneof_group: str) -> str: ...


    class TestNestedEnum:
        DEFAULT = 0

        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> int: ...
        @classmethod
        def keys(cls) -> List[str]: ...
        @classmethod
        def values(cls) -> List[int]: ...
        @classmethod
        def items(cls) -> List[Tuple[str, int]]: ...

    def __init__(
            self,
            *,
            double: float = 0,
            float: float = 0,
            int64: int = 0,
            uint64: int = 0,
            int32: int = 0,
            fixed64: int = 0,
            fixed32: int = 0,
            bool: bool = False,
            string: str = '',
            test_nested_message: TestNestedMessage = None,
            bytes: bytes = b'',
            uint32: int = 0,
            test_nested_enum: TestNestedEnum = None,
            sfixed32: int = 0,
            sfixed64: int = 0,
            sint32: int = 0,
            sint64: int = 0,
            pbt_message_map: Dict[int, TestNestedMessage] = None,
    ) -> None: ...

    double: float
    float: float
    int64: int
    uint64: int
    int32: int
    fixed64: int
    fixed32: int
    bool: bool
    string: str
    test_nested_message: TestNestedMessage
    bytes: bytes
    uint32: int
    test_nested_enum: TestNestedEnum
    sfixed32: int
    sfixed64: int
    sint32: int
    sint64: int
    pbt_message_map: MessageMap[int, TestNestedMessage]

    @classmethod
    def FromString(cls, s: bytes) -> TestMessage: ...
    def MergeFrom(self, other_msg: Message) -> None: ...
    def CopyFrom(self, other_msg: Message) -> None: ...
    def HasField(self, field_name: str) -> bool: ...
    def ClearField(self, field_name: str) -> None: ...
    def WhichOneof(self, oneof_group: str) -> str: ...


class TestEnum:
    DEFAULT = 0

    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> int: ...
    @classmethod
    def keys(cls) -> List[str]: ...
    @classmethod
    def values(cls) -> List[int]: ...
    @classmethod
    def items(cls) -> List[Tuple[str, int]]: ...