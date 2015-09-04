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
/////////////////////////////////////////////////
//File samediv.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////
#include "samediv.h"
/////////////////////////////////////////////////
template <class GEOMETRY>
SameShapeDivisor<GEOMETRY>::SameShapeDivisor()
  :Divisor<GEOMETRY>()
  {
  }
//////////////////////////////////////////////////
template <class GEOMETRY>
SameShapeDivisor<GEOMETRY>::~SameShapeDivisor()
  {
  }
//////////////////////////////////////////////////
