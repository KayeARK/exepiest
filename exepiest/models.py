#
# ForwardModel Class
#
# This file is part of exepiest
# (https://github.com/se-tutorial/exepiest.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

# Add imports here! e.g. import numpy as np


class ForwardModel(object):
    """ForwardModel Class:
    Base class for the model classes included in the exepiest package.
    Classes inheriting from ``ForwardModel`` class can implement the methods
    directly in Python.

    Methods
    -------
    simulate: return model output for specified parameters and times.

    """

    def __init__(self):
        super(ForwardModel, self).__init__()

    def simulate(self, parameters, times):
        """
        Runs a forward simulation with the given ``parameters`` and returns a
        time-series with data points corresponding to the given ``times``.

        Returns a sequence of length ``n_times`` (for single output problems)
        or a NumPy array of shape ``(n_times, n_outputs)`` (for multi-output
        problems), representing the values of the model at the given ``times``.

        Parameters
        ----------
        parameters
            An ordered sequence of parameter values.
        times
            The times at which to evaluate. Must be an ordered sequence,
            without duplicates, and without negative values.
            All simulations are started at time 0, regardless of whether this
            value appears in ``times``.

        """
        raise NotImplementedError

#
# exepiestModel Class
#


class exModel(ForwardModel):
    r"""exepiestPosterior Class:
    Give overview of what the posterior class does. Check docstring structures
    online for ideas (e.g. template for listing parameters + types)

    Parameters
    ----------
    parameters
        (type) Definition.

    """

    def __init__(self, parameters):
        super(exModel, self).__init__()

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

    def get_serial_intervals(self):
        """
        Returns class properties / parameters.

        """
        # Reverse inverting of order of serial intervals
        return self.parameters

    def set_serial_intervals(self, parameters):
        """
        Updates parameters. Add list of parameters.

        """
        # Delete this line and replace with code
        # Add any Raise except ValueError, TypeError etc. with useful error
        # messages
        raise NotImplementedError

    def simulate(self, parameters, times):
        """
        Runs a forward simulation with the given ``parameters`` and returns a
        time-series with incidence numbers corresponding to the given ``times``
        . Add list of parameters.

        """
        # Delete this line and replace with code
        # Add any Raise except ValueError, TypeError etc. with useful error
        # messages
        raise NotImplementedError
