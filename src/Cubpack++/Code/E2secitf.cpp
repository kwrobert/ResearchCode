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
//File E2secitf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   30 Jul 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//   19 Feb 1997     V1.1 (error message text changed)
/////////////////////////////////////////////////////////
#include "E2secitf.h"
#include "E2secprc.h"
/////////////////////////////////////////////////////////
PLANE_SECTOR::PLANE_SECTOR
  (const Point& A, const Point& B,const Point& C)
  {
  Error( A == B,
       "A PLANE_SECTOR has A == B, i.e. InnerRadius == OuterRadius.");
  Error( (C != B) && (((C-B)*(A-B)) == 0.0),
       "A PLANE_SECTOR has its centre at infinity.");
  StoreAtomic(new PlaneSector(A,B,C),new PlaneSector_Processor);
  }
/////////////////////////////////////////////////////////
PLANE_SECTOR::PLANE_SECTOR
  (const Point& O, real r  , real theta1, real theta2)
  {
  Error( theta1 == theta2,"A PLANE_SECTOR has Beta == Alpha.");
  StoreAtomic(new PlaneSector(O,r,theta1,theta2),
              new PlaneSector_Processor);
  }
/////////////////////////////////////////////////////////
