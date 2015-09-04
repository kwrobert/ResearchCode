
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
using namespace std;

#include <gsl/gsl_integration.h>

// function prototypes
double my_integrand (double x, void *params);


double my_integrand (double x, void *params)
{
  // Mathematica form:  Log[alpha*x]/Sqrt[x]

  // The next line recovers alpha from the passed params pointer
  double alpha = *(double *) params;

  return (log (alpha * x) / sqrt (x));
  //return cos(x);
}




int main (void)
{
  gsl_integration_workspace *work_ptr
    = gsl_integration_workspace_alloc (1000);

  double lower_limit = 0;	/* lower limit a */
  double upper_limit = 1;	/* upper limit b */
  double abs_error = 1.0e-8;	/* to avoid round-off problems */
  double rel_error = 1.0e-8;	/* the result will usually be much better */
  double result;		/* the result from the integration */
  double error;			/* the estimated error from the integration */

  double alpha = 1.0;		// parameter in integrand
  double expected = -4.0;	// exact answer

  gsl_function My_function;
  void *params_ptr = &alpha;

  My_function.function = &my_integrand;
  My_function.params = params_ptr;

  gsl_integration_qags (&My_function, lower_limit, upper_limit,
			abs_error, rel_error, 1000, work_ptr, &result,
			&error);

  cout.setf (ios::fixed, ios::floatfield);	// output in fixed format
  cout.precision (18);		// 18 digits in doubles

  int width = 20;  // setw width for output
  cout << "result          = " << setw(width) << result << endl;
  cout << "exact result    = " << setw(width) << expected << endl;
  cout << "estimated error = " << setw(width) << error << endl;
  cout << "actual error    = " << setw(width) << result - expected << endl;
  cout << "intervals =  " << work_ptr->size << endl;

  return 0;
}

//*********************************************************************//


