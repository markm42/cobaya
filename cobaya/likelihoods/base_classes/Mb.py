r"""
.. module:: H0

:Synopsis: Prototype class for local Hubble parameter measurements
:Author: Jesus Torrado

This is a simple gaussian likelihood for the latest local :math:`H_0` measurements
using a combination of different data.

It defines the following likelihoods

- ``H0.riess2018a``: A legacy local measurement of :math:`H_0`, used in the analysis of
  Planck data for the Planck 2018 release.
  `(arXiv:1801.01120) <https://arxiv.org/abs/1801.01120>`_
- ``H0.riess2018b``: Updated local measurement of :math:`H_0`.
  `(arXiv:1804.10655) <https://arxiv.org/abs/1804.10655>`_
- ``H0.riess201903``:  Riess et al. 2019 constraint
  `(arXiv:1903.07603) <https://arxiv.org/abs/1903.07603>`_


Using a different measurement
-----------------------------

If you would like to use different values for the :math:`H_0` constraint, as a mean and a
standard deviation, simply add the following likelihood, substituting ``mu_H0`` and
``sigma_H0`` for the respective values:

.. literalinclude:: ./src_examples/H0/custom_likelihood.yaml
   :language: yaml

"""

# Local
from cobaya.likelihood import Likelihood


class Mb(Likelihood):
    # Data type for aggregated chi2 (case sensitive)
    type = "Mb"

    # variables from yaml
    Mb_mean: float
    Mb_std: float

    def initialize(self):
        self.minus_half_invvar = - 0.5 / self.Mb_std ** 2

    def get_requirements(self):
        return {}

    def logp(self, **params_values):
        Mb_theory = params_values.get("Mb",None)
        return self.minus_half_invvar * (Mb_theory - self.Mb_mean) ** 2
