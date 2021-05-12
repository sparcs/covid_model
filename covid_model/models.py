"""Models for epidemic/infectious disease simulations."""
import numpy as np
import pymc3 as pm
import sunode
import sunode.wrappers.as_theano
from pymc3.ode import DifferentialEquation
import theano.tensor as tt
import theano


class SIR:
    """
    Epidemic simulation using the SIR model.

    S: Susceptible population
    I: Infected population
    R: Recovered population
    """

    def __init__(self, pop_total, df):
        """
        Initialise the SIR Model.

        pop_total: Total population count
        df: Pandas dataframe containing the following fields:
            confirmed
            active
            recovered
            deceased
        df has a datetime index
        """
        start_date = df.index.min()
        # end_date = df.index.max()
        self.inf_abs_0 = df[df.index == start_date].active[0]
        self.rec_abs_0 = df[df.index == start_date].recovered[0]
        self.sus_abs_0 = pop_total - self.rec_abs_0 - self.inf_abs_0
        self.sus_0 = self.sus_abs_0 / pop_total
        self.inf_0 = self.inf_abs_0 / pop_total

    def forecast(self, likelihood, prior):
        pass
