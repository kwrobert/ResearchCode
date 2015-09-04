/////////////////////////////////////////////////////////
//                                                     //
//    Cubpack++                                        //
//                                                     //
//        A Package For Automatic Cubature             //
//                                                     //
//        Authors : Ronald Cools                       //
//                  Dirk Laurie                        //
//                  Bart Maerten                       //
//                                                     //
/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////
// File : T2dv2.h
// History:
//   (date)          (version)
//    1 May 1999     V1.2 ( 2/4 division introduced  )
//
/////////////////////////////////////////////////////////
// DEFINITION OF CLASS Triangle_Divide4
// ------------------------------------------
//
// BASECLASSES:
//   SameShapeDivisor<Triangle>
//
//
// PURPOSE:
//   provides a means to cut Triangles in 2.
//
// TEMPLATES:
//   None
//
// METHODS:
//   CONSTRUCTORS:
//     1) Triangle_Divide2()
//     ---------------------
//
//   SELECTORS:
//     1) NumberOfParts() const
//     ------------------------
//     returns 2
//
//   MODIFIERS:
//     None
//   OPERATORS:
//     None
//   SPECIAL:
//     1) void Apply(Triangle& H,
//     Stack<Triangle>& S,const Vector<unsigned int>& D)
//     --------------------------------
//     divides H into parts and returns them in S
//
///////////////////////////////////////////////////////////
#ifndef T2DV2_H
#define T2DV2_H
//////////////////////////////////////////
#include "samediv.h"
#include "T2.h"
////////////////////////////////////////

class Triangle_Divide2 :public SameShapeDivisor<Triangle>
  {

  public:

  Triangle_Divide2();
  void Apply(const Triangle&, Stack<Triangle>&, const Vector<unsigned int>&);
  void Apply(unsigned int N, const Triangle& t, 
             Stack<Triangle>& Offspring, const Vector<unsigned int>& D) 
                {  Apply(t,Offspring,D);  };  
  int NumberOfParts() const {return 2;};

  };

//////////////////////////////////////////
#endif
