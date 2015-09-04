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
//File gsitf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//////////////////////////////////////////////
#include "gsitf.h"
#include "point.h"
#include "gsprc.h"
#include "error.h"
//////////////////////////////////////////////
GENERALIZED_SECTOR::GENERALIZED_SECTOR(real (*F)(real),
     real a, real b, const Point& Center)
  :USERINTERFACE<GeneralizedSector>()
  {
  Error( a == b, "A GENERALIZED_SECTOR is specified by two equal angles.");
  StoreAtomic(new GeneralizedSector(F,a,b,Center),
  new GeneralizedSector_Processor);
  }
///////////////////////////////////////////////
