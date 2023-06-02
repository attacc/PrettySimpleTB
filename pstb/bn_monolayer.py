from hamiltonian import *
import numpy as np
from scipy.constants import physical_constants as pyc

class BN_Monolayer(Hamiltonian):

    def __init__(self):
        self.h_dim = None  # Hamiltonian dimension 
        self.s_dim = None  # Space dimension 1,2,3

    def setup(self, parms = None):
        
        self.s_dim=2
        self.h_dim=2

        if parms != None:
            self.t  = parms[0]  # Hopping term in atomic units
            self.de = parms[1]  # One-site energy difference in atomic units
        else:
            # default values taken from Phys. Rev. B 100, 195201 (2019)
            self.t  = 2.92 * pyc["electron volt-hartree relationship"][0]
            self.de = 2.81 * pyc["electron volt-hartree relationship"][0]

        self.a = 1.0
        self.a_vec[0] = self.a*np.array([3**0.5/2, 1/2])
        self.a_vec[1] = self.a*np.array([3**0.5/2, -1/2]) 
        
        hamiltonian.setup(2,2, a_vec, parms)

    def eval_Hk(self, kpoint, k_units=None):
        #
        if(k_units == 'crystal') 
            # transform in cartersial coordinates
            kpt=np.matmul(np.transpose(self.b),kpoint)    
        elif (k_units == 'cart')
            # nothing to do 
            kpt=kpoint
        else (k_units == None)
            print(' Error unknown units!!! ')
        #
        # First neighboar tight-binding for monolayer BN
        #
        Hk.fill(0)
        Hk[0,0]=-self.de/2.0
        Hk[1,1]= self.de/2.0
        #
        kx=kpt[0]
        ky=kpt[1]
        a= self.a
        #
        f_k = np.exp(-1j*kx*a/3.0**0.5)  + 2.0 * np.exp(1j*kx*a/3.0**0.5) * np.cos(a/2.0*ky)
        #
        Hk[1,0]=self.t*f_l
        Hk[0,1]=Hk[1,0].conjg()
        #
        return Hk
