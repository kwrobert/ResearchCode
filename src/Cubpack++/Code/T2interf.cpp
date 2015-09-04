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
//File T2interf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jan 1996     V0.1f(typedef introduced)
//    4 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//    1 May 1999     V1.2 ( 2/4 division introduced  )
////////////////////////////////////////////////
#include "T2interf.h"
#include "s_adapt.h"
#include "T2rule13.h"
#include "T2dv2.h"
#include "T2dv4.h"
#include "T2prc.h"
#include "error.h"

///////////////////////////////////////////////
typedef Rule<Triangle> RuleTriangle;
typedef SameShapeDivisor<Triangle> SameShapeDivisorTriangle;
TRIANGLE::TRIANGLE(const Point& p1,const  Point&  p2,
                   const Point& p3)
  { 
    Error( (p1==p2)||(p1==p3)||(p2==p3) ,
           "A TRIANGLE has two equal points.");
    Pointer<RuleTriangle> R13 (new Triangle_Rule13);
    Pointer<SameShapeDivisorTriangle> D2 (new Triangle_Divide2);  
    Pointer<SameShapeDivisorTriangle> D4 (new Triangle_Divide4);
 
//    StoreAtomic(new Triangle(p1,p2,p3),
//       new SimpleAdaptive<Triangle>(R13,DN2) );
    
//    StoreAtomic(new Triangle(p1,p2,p3),
//       new SimpleAdaptive<Triangle>(R9,D4,DN) );
   
//    StoreAtomic(new Triangle(p1,p2,p3),
//       new SimpleAdaptive<Triangle>(R13,D4,DN) );

//    StoreAtomic(new Triangle(p1,p2,p3),
//       new SimpleAdaptive<Triangle>(R13,D2) ); 

//    StoreAtomic(new Triangle(p1,p2,p3),
//       new SimpleAdaptive<Triangle>(R13,D9) );
    
  StoreAtomic(new Triangle(p1,p2,p3),
       new Triangle_Processor);
  }
///////////////////////////////////////////////
