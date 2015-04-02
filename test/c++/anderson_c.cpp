#include "ctint.hpp"
#include <boost/mpi.hpp>
#include <boost/mpi/environment.hpp>

// Anderson model test
int main(int argc, char ** argv) { 

  boost::mpi::environment env(argc, argv);

  // set parameters
  double beta = 20.0;
  double U = 1.0;
  double delta = 0.1;
  int n_cycles = 10000;
  int n_iw = 200;

  // construct the ct-int solver
  auto ctqmc = ctint_solver{beta, n_iw};

  // parameters
  double mu = 1.3 - U/2.0; //mu=0 corresponds to half filling
  double epsilon = 0.2;

  // initialize g0(omega)
  triqs::clef::placeholder<0> om_;
  for (auto sig : {0,1}) ctqmc.G0_iw()[sig](om_) << 1.0 / (om_ + mu - 1.0 / (om_ - epsilon));

  // launch the Monte Carlo
  ctqmc.solve(U, delta, n_cycles);

  //to compare with ct_seg
  //gf<imfreq> gw = ctqmc.G0_iw()[0];
  //gw.singularity()(1)=1.0;
  //auto gt = make_gf_from_inverse_fourier(gw);

  // save the results
  triqs::h5::file G_file("anderson_c.output.h5",H5F_ACC_TRUNC);
  //h5_write(G_file, "G0", ctqmc.G0_iw()[0]); //not needed for the test
  h5_write(G_file, "G", ctqmc.G_iw()[0]);
  //h5_write(G_file, "Gt", gt);

}
