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
//File sttosmt.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
////////////////////////////////////////////////
#include "sttosmst.h"
#include "point.h"
#include "math.h"
#include <iostream>
////////////////////////////////////////////
void
IStoSIS::Transform(real& w, Point& p)
      {
//    std::cout << p;
      SemiInfiniteStrip& s = *SIS_ptr;
      Point D  = s.B()- s.A();
      Point C(-D.Y(),D.X());
//    if (p.Y() > 600)   // goed voor double
//    if (p.Y() > 60)
      if (p.Y() > log(REAL_MAX)*6.0/7.0)
        {
        w = 0;
        return;
        };
      C = C/C.Length();
      w *= D.Length()*exp(p.Y());
      p = s.A() + exp(p.Y())*C + p.X()*D;
 //   std::cout << p << endl;
      }
///////////////////////////////////////////////////
IStoSIS::IStoSIS(SemiInfiniteStrip* g)
  : Transformation(),SIS_ptr(g)
  {
  }
//////////////////////////////////////////////////
