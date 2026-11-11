"""Step definitions for info.feature."""

import pytest
from pytest_bdd import scenarios

scenarios("../info.feature")

pytestmark = pytest.mark.integration
