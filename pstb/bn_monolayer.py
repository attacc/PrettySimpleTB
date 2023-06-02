import hamiltonian
import numpy as np
from scipy.constants import physical_constants as pyc

class bn_monolayer(hamiltonian):

    def __init__(self):
        self.h_dim = None  # Hamiltonian dimension 
        self.s_dim = None  # Space dimension 1,2,3

    def setup(self, a_vec = None, parms = None):
        
        self.s_dim=2
        self.h_dim=2

        if parms != None:
            self.t  = parms[0]  # Hopping term in atomic units
            self.de = parms[1]  # One-site energy difference in atomic units
        else:
            # default values taken from Phys. Rev. B 100, 195201 (2019)
            self.t  = 2.92 * pyc["electron volt-hartree relationship"][0]
            self.de = 2.81 * pyc["electron volt-hartree relationship"][0]
        
        hamiltonian.setup(2,2, a_vec, parms)

    def eval_Hk(self, kpoint):
        # kpoint is in crystal (reduced) units
        # First neighboar tight-binding for monolayer BN
        #
        Hk.fill(0)
        Hk[0,0]=0.0
        Hk[1,1]=self.de
        #
        Hk[1,0]=self.t*f
        Hk[0,1]=Hk[1,0].conjg()
        #
        return Hk
