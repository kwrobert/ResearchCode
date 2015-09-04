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
//File S2interf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   17 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
#include "S2interf.h"
#include "S2adapt.h"
#include "S2rule13.h"
#include "error.h"
/////////////////////////////////////////////////////////
CIRCLE::CIRCLE(const Point& c,const Point& b)
  {
        Error( b == c,"A CIRCLE is specified by two equal points.");
        StoreAtomic(new Circle(c,b),new CircleAdaptive(new Circle_Rule13));
  }
/////////////////////////////////////////////////////////
CIRCLE::CIRCLE(const Point& c, real Radius)
  {
        Error(Radius<=0,"A CIRCLE is specified with radius zero or negative.");
        StoreAtomic(new Circle(c,Radius),new CircleAdaptive(new Circle_Rule13));
  }
/////////////////////////////////////////////////////////
