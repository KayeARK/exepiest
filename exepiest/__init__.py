#
# Root of the exepiest module.
# Provides access to all shared functionality (models, simulation, etc.).
#
# This file is part of exepiest
# (https://github.com/se-tutorial/exepiest.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
"""Give brief overview of the package.
"""

# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .models import ForwardModel, exModel  # noqa
from .posterior import exPosterior  # noqa
