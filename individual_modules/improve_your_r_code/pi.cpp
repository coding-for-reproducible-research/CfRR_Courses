#include "Rcpp.h" 

using namespace Rcpp;

// [[Rcpp::export]]
double pi_cpp(int n) {
  int count_inside = 0;
  
  for (int i = 0; i < n; ++i) {
    double x = static_cast<double>(rand()) / RAND_MAX;
    double y = static_cast<double>(rand()) / RAND_MAX;
    
    if (std::sqrt(x * x + y * y) < 1) {
      count_inside++;
    }
  }
  
  return (static_cast<double>(count_inside) / n) * 4.0;
}