from datetime import timedelta
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from whenever import TimeDelta as TimeDelta


class TimeDeltaAnnotation:

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.no_info_wrap_validator_function(
            cls._validate,
            core_schema.timedelta_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: instance.format_common_iso(),
                when_used="json-unless-none",
            ),
        )

    @staticmethod
    def _validate(value: Any, _: core_schema.ValidatorFunctionWrapHandler) -> TimeDelta:
        if isinstance(value, TimeDelta):
            return value
        elif isinstance(value, timedelta):
            value = TimeDelta.from_py_timedelta(value)
            return value
        elif isinstance(value, str):
            value = TimeDelta.parse_common_iso(value)
            return value
        else:
            raise ValueError(f"Couldn't validate value {value} of type {type(value)}")
