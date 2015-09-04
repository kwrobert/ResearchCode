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
// File : psitf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   21 Jul 1996     V0.2 (transforms to generalized rectangle)
//   25 Jul 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
#include "psitf.h"
#include "passbuck.h"
#include "gritf.h"
#include "grtops.h"
/////////////////////////////////////////////////////////
real parabola(const Point& P)
  { real s=P.X(); return (1-s*s)/2; }

PARABOLIC_SEGMENT::PARABOLIC_SEGMENT(const Point& A,
                                     const Point& B,
                                     const Point& P)
  :USERINTERFACE<ParabolicSegment>()
  {
  Point p(-1,0),q(1,0);
  GENERALIZED_RECTANGLE GR(parabola,p,q);
  Error( A == B, "A PARABOLIC_SEGMENT is specified by two equal points");
  Error( (P.X()-A.X())*(P.Y()-B.Y()) == (P.X()-B.X())*(P.Y()-A.Y()),
       "A PARABOLIC_SEGMENT has P on the line AB");
  StoreAtomic
    (
    new ParabolicSegment(A,B,P),
    new PassTheBuck<GeneralizedRectangle,ParabolicSegment,GRtoPS>
      (
      (AtomicRegion*) GR
      )
    );
  }
//////////////////////////////////////////////////////////
