# Generated automatically using the command :
# c++2py.py ../c++/ctint.hpp -p -m pytriqs.applications.impurity_solvers.ctint_tutorial -o ctint_tutorial
from wrap_generator import *

# The module
module = module_(full_name = "pytriqs.applications.impurity_solvers.ctint_tutorial", doc = "")

# All the triqs C++/Python modules
module.use_module('gf')

# Add here all includes beyond what is automatically included by the triqs modules
module.add_include("../c++/ctint.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
using namespace triqs::gfs;
""")

# The class ctint_solver
c = class_(
        py_type = "CtintSolver",  # name of the python class
        c_type = "ctint_solver",   # name of the C++ class
)

c.add_constructor("""(double beta_, int n_iw = 1024, int n_tau = 100001)""",
                  doc = """ """)

c.add_method("""void solve (double U, double delta, int n_cycles, int length_cycle = 50, int n_warmup_cycles = 5000, std::string random_name = "", int max_time = -1)""",
             doc = """ """)

c.add_property(name = "G0_iw",
               getter = cfunction("block_gf_view<imfreq> G0_iw ()"),
               doc = """ """)

c.add_property(name = "G0_tau",
               getter = cfunction("block_gf_view<imtime> G0_tau ()"),
               doc = """ """)

c.add_property(name = "G_iw",
               getter = cfunction("block_gf_view<imfreq> G_iw ()"),
               doc = """ """)

module.add_class(c)

module.generate_code()