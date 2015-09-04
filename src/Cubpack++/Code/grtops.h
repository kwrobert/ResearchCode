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
// File : grtops.h
// History:
//   (date)          (version)
// 21 Jul 1996        V0.2 (first version)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
/////////////////////////////////////////////////////////
// DEFINITION OF CLASS GRtoPS
// -------------------------------------------------
//
// BASECLASSES:
//   Transformation
//
// PURPOSE:
//   transformation from generalized rectangle to 
//   parabolic segment
//
// TEMPLATES:
//   None
//
// METHODS:
//   CONSTRUCTORS:
//     1) GRtoPS(ParabolicSegment* g)
//     ------------
//     the target region has to be supplied
//
//   SELECTORS:
//     None
//
//   MODIFIERS:
//     None
//
//   OPERATORS:
//     None
//
//   SPECIAL:
//     1) void Transform(real & w, Point & p)
//     --------------------------------------
//     multiplies w by the Jacobian at p and then
//     replaces p by the transformed  point
//
/////////////////////////////////////////////////////////
#ifndef GRTOPS_H
#define  GRTOPS_H
/////////////////////////////////////////////////////////
#include "trnsfrm.h"
#include "ps.h"
#include "gr.h"
#include "pointer.h"
///////////////////////////////////////////////////
class GRtoPS : public Transformation
  {
  public:

  GRtoPS( ParabolicSegment*);
  void Transform(real& w, Point& p);

  private:

  Point O;
  real cs[2],a,b,c;
  };
//////////////////////////////////////////////////////
#endif
