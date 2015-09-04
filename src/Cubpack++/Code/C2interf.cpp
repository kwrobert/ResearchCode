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
//File C2interf.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   25 Jan 1996     V0.1f(typedef introduced)
//    4 Jun 1996     V0.2 (detect degenerate regions)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//   19 Feb 1997     V1.1 (same treatment for PARALLELOGRAM and RECTANGLE)
/////////////////////////////////////////////////////////
#include "C2interf.h"
#include "s_adapt.h"
#include "C2rule13.h"
#include "C2prc.h"
#include "error.h"
#include "math.h"

/////////////////////////////////////////////////////////
typedef Rule<Parallelogram> RuleParallelogram;
typedef SameShapeDivisor<Parallelogram> SameShapeDivisorParallelogram;
PARALLELOGRAM::PARALLELOGRAM(const Point& p1,
                             const Point& p2,
                             const Point& p3)
  :USERINTERFACE<Parallelogram>()
{
 Error((p1==p2)||(p1==p3)||(p2==p3),
       "A PARALLELOGRAM has two equal points.");
  StoreAtomic(new Parallelogram(p1,p2,p3),
                new Parallelogram_Processor);
}
//////////////////////////////////////////////////////////
RECTANGLE::RECTANGLE(const Point& p1,
                             const Point& p2,
                             const Point& p3)
  :USERINTERFACE<Parallelogram>()
  {
  Error( fabs((p2-p1)*(p3-p1)) > 100*REAL_EPSILON,
    "Sides of RECTANGLE are not orthogonal.");
  StoreAtomic(new Parallelogram(p1,p2,p3),
              //new SimpleAdaptive<Parallelogram>(
                 //new Parallelogram_Rule13,
                 //new Parallelogram_Divide4));
                 new Parallelogram_Processor);
  }
//////////////////////////////////////////////////////////
