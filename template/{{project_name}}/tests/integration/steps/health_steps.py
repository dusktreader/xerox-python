"""Step definitions for health.feature."""

import pytest
from pytest_bdd import scenarios

scenarios("../health.feature")

pytestmark = pytest.mark.integration
