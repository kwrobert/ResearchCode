// 20 vb20.c Lens-shaped parabolic region

#include <cubpack.h>
#include <iostream.h>

int alfa, beta;
real a, b;

real ipow(real x, int n)
  { if (n==0) return 1;
    if (n<0) return 1.0/ipow(x,-n);
    real xn = n%2 ? x : 1;
    return xn*ipow(x*x, n/2);
  }

real f0(const Point& p)
 { real x=p.X() , y=p.Y(), fv;
   fv=ipow(x,alfa)*ipow(y,beta);
   return fv;
 }

real f(const Point& p)
 { real x=p.X() , y=p.Y(), fv, rr=x*x+y*y;      
   fv= rr==0 ? 0 : ipow(x,alfa)*ipow(y,beta)/sqrt(rr)/4;
   return fv;
 }

real g0(const Point& p)
 { real u=p.X() , v=p.Y(), gv;
   gv=4*(u*u+v*v)*ipow(u*u-v*v,alfa)*ipow(2*u*v,beta);
   return gv;
 }

real g(const Point& p)
 { real u=p.X() , v=p.Y(), gv;      
   gv=ipow(u*u-v*v,alfa)*ipow(2*u*v,beta);
   return gv;
 }

int main ()
 {
   EvaluationCounter count;

   // Define the region of integration:
   // This comes from Stroud pp 224-225  "First parabolic region"
   // a^2-y^2/(4a^2) < x < y^2/(4*b*2) - b^2
   // Vertices are x=a^2-b^2;  y = +- 2*a*b
   // Tangents meet at x = +- a^2+b^2; y=0

 cout << "Lens-shaped parabolic region, weight function 1/r" << endl;  

 while (1) {
   cout << "Parameters of region (0 to exit): a, b = ? ";
   cin >> a; if (a==0) break;
   cin >> b; if (b==0) break;   
   cout << "Exponents alfa, beta in x^alfa*y^beta ? ";
   cin >> alfa >> beta;

   real x1=a*a-b*b, x0=a*a+b*b, y1=2*a*b;
   Point A(x1,y1), B(x1,-y1), C1(x0,0), C2(-x0,0);
   PARABOLIC_SEGMENT PAR1(A,B,C1), PAR2(A,B,C2);
   REGION_COLLECTION Lens=PAR1+PAR2;
   RECTANGLE Exact(Point(-a,0),Point(a,0),Point(-a,b));

   count.Start();
   cout <<"The integral is " << Integrate(f,Lens,0.5e-6,0.5e-6);
   cout <<" with estimated absolute error " << Lens.AbsoluteError() << endl;
   count.Stop();
   cout << count.Read() << " function evaluations were used." << endl;
   cout << "The exact result should be " << Integrate(g,Exact,0.0,1e-12) << endl;
 }
   return 0;
 }
