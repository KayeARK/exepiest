#
# exepiestPosterior Class
#
# This file is part of exepiest
# (https://github.com/se-tutorial/exepiest.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

# Add imports here! e.g. import numpy as np


class exPosterior(object):
    r"""exepiestPosterior Class:
    Give overview of what the posterior class does. Check docstring structures
    online for ideas (e.g. template for listing parameters + types)

    Parameters
    ----------
    parameters
        (type) Definition.

    """

    def __init__(self, parameters):
        super(exPosterior, self).__init__()

        # Delete this line and replace with code
        self.parameters = parameters

    def _check_parameters(self, parameters):
        """
        Checks parameters format. Add list of parameters.
        """
        # Delete this line and replace with code
        # Add any Raise except ValueError, TypeError etc. with useful error
        # messages
        raise NotImplementedError

    def get_parameters(self):
        """
        Returns class properties / parameters.

        """
        # Reverse inverting of order of serial intervals
        return self.parameters

    def set_parameters(self, parameters):
        """
        Updates parameters. Add list of parameters.

        """
        # Delete this line and replace with code
        # Add any Raise except ValueError, TypeError etc. with useful error
        # messages
        raise NotImplementedError

    def run_inference(self, tau):
        """
        Runs the inference. Add list of parameters,

        """
        # Delete this line and replace with code
        # Add any Raise except ValueError, TypeError etc. with useful error
        # messages
        raise NotImplementedError
