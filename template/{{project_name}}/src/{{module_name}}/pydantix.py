from datetime import timedelta
from typing import Any

import pendulum
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema


class DurationAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_wrap_validator_function(
            cls._validate,
            core_schema.timedelta_schema(),
        )

    @staticmethod
    def _validate(value: Any, _: core_schema.ValidatorFunctionWrapHandler) -> pendulum.Duration:
        if isinstance(value, pendulum.Duration):
            return value
        elif isinstance(value, timedelta):
            return pendulum.Duration(
                days=value.days,
                seconds=value.seconds,
                microseconds=value.microseconds,
            )
        elif isinstance(value, str):
            duration = pendulum.parse(value)
            if isinstance(duration, pendulum.Duration):
                return duration
        raise ValueError(f"Couldn't validate value {value} of type {type(value)}")
