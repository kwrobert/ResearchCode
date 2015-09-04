//  Integral over the plane with an integrand that has a discontinuos
//  derivative on a circle.
//  Divide the plane or not, that is the question.

#include <cubpack.h>
#include <iostream.h>

real f(const Point& p)
 { real r=p.Length(), x=p.X() ;
   return exp(-fabs(r-1))*x*x; }

int main ()
 { Point origin(0,0);
   real radius=1;
   CIRCLE cir(origin,radius);
   OUT_CIRCLE ocir(origin,radius);
   REGION_COLLECTION divided_plane = cir + ocir;
   PLANE total;
   EvaluationCounter TikTak;

   TikTak.Start();
   cout <<"Consider the plane as a circle and an out_circle:"<<endl;
   cout <<"  The integral is " << Integrate(f, divided_plane , 0, 1.0e-6);
   cout <<" with absolute error " << divided_plane.AbsoluteError() << endl;
   TikTak.Stop(); cout<<"  Number of evaluations = "<<TikTak.Read()<<endl;

   TikTak.Reset(); TikTak.Start();
   cout <<"Consider the plane as given:"<<endl;
   cout <<"  The integral is " << Integrate(f, total, 0, 1.0e-6);
   cout <<" with absolute error " << total.AbsoluteError() << endl;
   TikTak.Stop(); cout<<"  Number of evaluations = "<<TikTak.Read()<<endl;
   

   return 0;
 }
