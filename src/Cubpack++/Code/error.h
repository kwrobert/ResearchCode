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
// File : error.h
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
// PURPOSE
//  void Error(Boolean b,char* message) is an error
//  checking and reporting routine. if b is true then
//  message is printed on stderr and the program is
//  aborted.
/////////////////////////////////////////////////////////
#ifndef ERROR_H
#define ERROR_H
////////////////////////////////////////
#include "boolean.h"
#include <iostream>

////////////////////////////////////////
inline void Error(int b,char* message)
  {
  if (b)
    {
    std::cerr << message <<std::endl;
    std::cerr.flush();
    abort();
    };
  }
////////////////////////////////////////
#endif
