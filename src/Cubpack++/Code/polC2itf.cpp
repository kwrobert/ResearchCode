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
//File polC2itf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   19 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
#include "polC2itf.h"
#include "polC2prc.h"
/////////////////////////////////////////////////////////
POLAR_RECTANGLE::POLAR_RECTANGLE
  (const Point& A, const Point& B,const Point& C)
  {
  Error( A == B,
       "A POLAR_RECTANGLE has A == B, i.e. InnerRadius == OuterRadius.");
  Error( (C != B) && (((C-B)*(A-B)) == 0.0),
       "A POLAR_RECTANGLE has its centre at infinity.");
  StoreAtomic(new PolarRectangle(A,B,C),new PolarRectangle_Processor);
  }
/////////////////////////////////////////////////////////
POLAR_RECTANGLE::POLAR_RECTANGLE
  (const Point& O, real r1, real r2, real t1, real t2)
  {
  Error( t1 == t2,"A POLAR_RECTANGLE has Beta == Alpha.");
  Error( r1 == r2,"A POLAR_RECTANGLE has OuterRadius == InnerRadius");
  StoreAtomic(new PolarRectangle(O,r1,r2,t1,t2),new PolarRectangle_Processor);
  }
/////////////////////////////////////////////////////////
