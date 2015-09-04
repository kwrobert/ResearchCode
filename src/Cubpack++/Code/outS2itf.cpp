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
///////////
//File outs2itf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   17 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
////////////////
#include "passbuck.h"
#include "invert.h"
#include "outS2.h"
#include "outS2itf.h"
#include "S2.h"
#include "S2interf.h"
#include "error.h"
///////////////////////
OUT_CIRCLE::OUT_CIRCLE(const Point& c,const Point& b)
  {
  Error( b == c,"An OUT_CIRCLE is specified by two equal points.");
  StoreAtomic(new OutCircle(c,b),
   new PassTheBuck<Circle,OutCircle,Invert>((AtomicRegion*)CIRCLE(c,b)));
  }
//////////////////////////////////////////////
OUT_CIRCLE::OUT_CIRCLE(const Point& c, real Radius)
  {
  Error(Radius<=0,"An OUT_CIRCLE is specified with radius zero or negative.");
  StoreAtomic(new OutCircle(c,Radius),
   new PassTheBuck<Circle,OutCircle,Invert>((AtomicRegion*)CIRCLE(c,Radius)));
  }
//////////////////////////////////////////////
