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
//File boolean.cpp
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
////////////////////////////////////////////////

#include "boolean.h"
#include <iostream>


ostream& operator << (ostream& os, const Boolean& b)
  {
  if (b==False)
    {
    os<< "False ";
    }
  else
    {
    os<< "True ";
    };
  return os;
  }
