import hamiltonian

    class bn_monolayer(hamiltonian):

        def setup(self, parms = None):
            self.s_dim=2
            self.h_dim=2
            if parms != None:
                self.t  = parms[0]  # Hopping term
                self.de = parms[1]  # One-site energy difference
            else:
                # default values taken from Phys. Rev. B 100, 195201 (2019)
                self.t  = 2.92 *
                self.de = 2.81 * 
