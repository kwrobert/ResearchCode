/////////////////////////////////////////////////////////
//                                                     //
//    Cubpack++                                        //
//                                                     //
//        A Package For Automatic Cubature             //
//                                                     //
//        Authors : Ronald Cools                       //
//                  Dirk Laurie                        //
//                  Luc Pluym                          //
//                                                     //
/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////
// File : grtops.c
// History:
//   (date)          (version)
//   17 Jul 1996     V0.2 (first version)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
#include "grtops.h"
/////////////////////////////////////////////////////////

Point operator * (Point P, real* cs)
//  Rotate P by rotation matrix with first column cs
 { real x=P.X(), y=P.Y(), c=cs[0], s=cs[1];
   return Point(c*x-s*y,s*x+c*y);
 }

Point operator / (Point P, real* cs)
//  Rotate P by rotation matrix with first row cs
 { real x=P.X(), y=P.Y(), c=cs[0], s=cs[1];
   return Point(c*x+s*y,-s*x+c*y);
 }

//  1.  Change origin to midpoint of line.
//  2.  Rotate so that that A goes to (-a,-b),  
//      B to (a,b), P to (0,c).

GRtoPS::GRtoPS(ParabolicSegment* p)
  : Transformation(),
    O((p->A()+p->B())/2)
  { Point A=p->A()-O, B=p->B()-O, P=p->P()-O;
    c=P.Length();
    cs[0]=P.Y()/c; cs[1]=P.X()/c;
    Point X=B*cs; a=X.X(); b=X.Y();
  }
////////////////////////////////////////////////////////

// The integral is now
// int_{-1}^1 int_0^{(1-s^2)/2} a*c f(a*s,b*s+c*t) dt ds

void GRtoPS::Transform(real & w, Point& p)
  { real s=p.X(), t=p.Y();
    p=O+Point(a*s,b*s+c*t)/cs;
    w*=fabs(a*c);
  }
/////////////////////////////////////////////////////////
