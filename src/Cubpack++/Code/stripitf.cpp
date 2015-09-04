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
//File stripitf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//////////////////////////////////////////////
#include "stripitf.h"
#include "passbuck.h"
#include "E2interf.h"
#include "E2tostrp.h"
#include "error.h"
//////////////////////////////////////////////
INFINITE_STRIP::INFINITE_STRIP(const Point& a,const Point& b)
  :USERINTERFACE<InfiniteStrip>()
  {
  PLANE P;
  Error( a == b, "An INFINITE_STRIP is specified by two equal points.");
  StoreAtomic(new InfiniteStrip(a,b),
      new PassTheBuck<Plane ,InfiniteStrip,
               E2toIS>((AtomicRegion*)P));
  }
///////////////////////////////////////////////
