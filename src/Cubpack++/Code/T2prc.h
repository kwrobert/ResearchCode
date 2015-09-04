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
// File : T2prc.h
// History:
//   (date)          (version)
//    1 May 1999     V1.2 ( 2/4 division introduced  )
//   
/////////////////////////////////////////////////////////
// DEFINITION OF CLASS Triangle_Processor
// -------------------------------------------------
//
// BASECLASSES:
//   Processor<Triangle>
//
// PURPOSE:
//   A processor for two-dimensional triangles.
//   first a degree 13 rule is applied to the region
//   Fourth order divided differences along the axes are
//   computed. If they're very much different, the region
//   is cut in two, otherwise it is cut in four.
//
// TEMPLATES:
//   None
//
// METHODS:
//   CONSTRUCTORS:
//     1) Triangle_Processor();
//     -----------------------------
//
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
//     1) void Process(Stack<AtomicRegion>&);
//     --------------------------------------------------
//     see class Processor
//
//     2) virtual Processor<GEOMETRY>* NewCopy() const=0
//     -------------------------------------------------
//
//     makes a new copy (using the copy constructor) and
//     returns a pointer to it.
/////////////////////////////////////////////////////////
#ifndef T2PRC_H
#define T2PRC_H
//////////////////////////////////////////////
#include "pointer.h"
#include "rule.h"
#include "samediv.h"
#include "T2.h"
#include "regproc.h"
/////////////////////////////////////////////

class Triangle_Processor :
     public Processor<Triangle>
  {
  public:
  typedef Rule<Triangle> RuleTriangle;
  typedef SameShapeDivisor<Triangle> SameShapeDivisorTriangle;

  Triangle_Processor();
  void Process(Stack<AtomicRegion>&);
  Processor<Triangle>* NewCopy() const;
  void UseRule(RuleTriangle*); 
  void Divide(unsigned int,Stack<AtomicRegion>&);
  
  protected:

  static Pointer<RuleTriangle> TheRule;
  static Pointer<SameShapeDivisorTriangle> TheDivisor4;
  static Pointer<SameShapeDivisorTriangle> TheDivisor2;
  unsigned int TimesCalled;
  Triangle_Processor* Descendant() const;
  Vector<real> Diffs;

  };

/////////////////////////////////////////////
#endif
