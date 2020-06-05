#include<stdio.h>
#include<math.h>
#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_errno.h>
int func (double t, const double y[], double f[],
      void *params)
{
	f[0]=32.*y[0]+66.*y[1]+2*t/3.+2/3.;
	f[1]=-66.*y[0]-133*y[1]-t/3.-1/3.;
	return GSL_SUCCESS;
}
int jacob(double t, const double y[], double *dfdy,
     double dfdt[], void *params)
{
	dfdy[0]=32.;
	dfdy[1]=66.;
	dfdy[2]=-66.;
	dfdy[3]=-133;
	
	dfdt[0]=2/3.;
	dfdt[1]=-1/3.;
	return GSL_SUCCESS;
}
int main()
{
	int dim=2; // dimension of IVP
	gsl_odeiv2_system sys={func, jacob, dim};
	const gsl_odeiv2_step_type *T=gsl_odeiv2_step_rk4; // RK4 method
	double eps_abs,eps_rel;
	eps_abs=1.e-6;
	eps_rel=0.;
	double h_start=1.e-3;
	gsl_odeiv2_driver *d=gsl_odeiv2_driver_alloc_y_new(&sys,T,h_start,eps_abs,eps_rel);
	
	double ti,tf;	
	ti=0.;
	tf=0.5;
	double y[]={1/3.,1/3.};
	for (int i=0;i<=100;++i)
	{
		double t=i*tf/100;
		int status;
		status=gsl_odeiv2_driver_apply(d,&ti,t,y);
		if (status != GSL_SUCCESS)
			break;
		printf("%.5e\t%.5e\t%.5e\n",ti,y[0],y[1]);
		t=ti;
	}
	gsl_odeiv2_driver_free(d);
}
