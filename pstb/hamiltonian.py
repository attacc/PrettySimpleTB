class Hamiltonian:
    def __init__(self):
        self.setup()

    def setup(self, parms = None):
        self.h_dim = None # Hamiltonian dimension 
        self.s_dim = None # Space dimension 1,2,3
        if parms != None:
            self.parms = parms
    
    def eval_Hk(self, kpoint):
        # to overriden in subclasses
        self.Hk = None
        return self.Hk


