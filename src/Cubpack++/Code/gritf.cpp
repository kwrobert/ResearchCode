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
////////////////////////////////////////////////
//File gritf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//////////////////////////////////////////////
#include "gritf.h"
#include "passbuck.h"
#include "C2.h"
#include "C2interf.h"
#include "C2togr.h"
#include "point.h"
#include "error.h"
//////////////////////////////////////////////
GENERALIZED_RECTANGLE::GENERALIZED_RECTANGLE(Function f,const Point& a,const Point& b)
  :USERINTERFACE<GeneralizedRectangle>()
  {
  Point A(0,0),B(1,0),C(0,1);
  PARALLELOGRAM R(A,B,C);
  Error( a == b, "A GENERALIZED_RECTANGLE is specified by two equal points.");
  StoreAtomic(new GeneralizedRectangle(f,a,b),
      new PassTheBuck<Parallelogram,GeneralizedRectangle,
               C2toGR>((AtomicRegion*)R));
  }
///////////////////////////////////////////////
