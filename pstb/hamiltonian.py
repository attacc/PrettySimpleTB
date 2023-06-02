import math
from numpy.linalg import inv

class Hamiltonian
    def __init__(self):
        self.h_dim = None  # Hamiltonian dimension 
        self.s_dim = None  # Space dimension 1,2,3

    def setup(self, h_dim, s_dim, a_vec, parms = None):
        
        self.h_dim = h_dim
        self.s_dim = s_dim 

        self.a_vec=np.zeros((self.s_dim,self.s_dim),float)
        self.a_vec = a_vec # Lattice vectors in atomic units

        if parms != None:
            self.parms = parms
    
        self.Hk=np.zeros((self.h_dim, self.h_dim),complex)

        self.b_vec=np.zeros((self.s_dim),float)

        if self.s_dim == 3:
            self.b_vec[0]=np.cross(self.a_vec[1],self.a_vec[2])
            self.b_vec[1]=np.cross(self.a_vec[2],self.a_vec[0])
            self.b_vec[2]=np.cross(self.a_vec[0],self.a_vec[1])

            DL_vol =np.dot(self.a_vec[0],np.cross(self.a_vec[1],self.a_vec[2]))
            self.b_vec=self.b_vec*2.0*math.pi/DL_vol

        elif self.s_dim == 2:
            self.b_vec=2.0*math.pi*inv(self.a_vec)
            DL_vol =np.dot(self.a_vec[0],self.a_vec[1])

        elif self.s_dim == 1:
            self.b_vec[0] =2.0*math.pi/self.a_vec[0]
            DL_vol =self.a_vec[0]
     
        
        RL_vol= (2.0*math.pi)**2/DL_vol

        print(' Lattice vectors : \n')
        for a in self.a_vec:
            print('str(a) \n')
        print(' Reciprocal attice vectors : \n')
        for b in self.a_vec:
            print('str(b) \n')

        print('Volume str(DL_vol), Brillouin zone volume str(RL_vol) \n')
        print('Hamiltonian dimension str(self.h_dim) \n')

    def eval_Hk(self, kpoint):
        # to overriden in subclasses
        self.Hk = None
        return self.Hk


