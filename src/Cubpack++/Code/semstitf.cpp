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
//File stripitf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//   17 Aug 2001     V1.2.1 (name of variable changed for CC)
/////////////////////////////////////////////////////////
#include "semstitf.h"
#include "passbuck.h"
#include "stripitf.h"
#include "sttosmst.h"
#include "error.h"
/////////////////////////////////////////////////////////
SEMI_INFINITE_STRIP::SEMI_INFINITE_STRIP(const Point& a,const Point& b)
  :USERINTERFACE<SemiInfiniteStrip>()
  {
  Point origin(0,0),one(1,0);
  INFINITE_STRIP I(origin,one);
  Error( a == b,"A SEMI_INFINITE_STRIP is specified by two equal points.");
  StoreAtomic(new SemiInfiniteStrip(a,b),
      new PassTheBuck<InfiniteStrip,SemiInfiniteStrip,
               IStoSIS>((AtomicRegion*)I));
  }
////////////////////////////////////////////////////////
