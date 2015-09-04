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
//File T2prc.c
// History:
//   (date)          (version)
//    1 May 1999     V1.2 ( 2/4 division introduced  )
//   
////////////////////////////////////////////////////////////
#include "T2prc.h"
#include "T2rule13.h"
#include "T2dv2.h"
#include "T2dv4.h"
#include "error.h"
#include "atomic.h"
////////////////////////////////////////////////////////
Pointer < Triangle_Processor::RuleTriangle > 
  Triangle_Processor::TheRule = new Triangle_Rule13;
Pointer < Triangle_Processor::SameShapeDivisorTriangle > 
  Triangle_Processor::TheDivisor2 = new Triangle_Divide2;
Pointer < Triangle_Processor::SameShapeDivisorTriangle > 
  Triangle_Processor::TheDivisor4 = new Triangle_Divide4;
////////////////////////////////////////////////////////
Triangle_Processor::Triangle_Processor()
  :TimesCalled(0),
   Diffs(3)
   {
   }
/////////////////////////////////////////////////////////////
Triangle_Processor*
Triangle_Processor::Descendant()
const
  {
  Triangle_Processor* r = new Triangle_Processor;
  r->UseRule(TheRule); 
  return r;
  }
////////////////////////////////////////////////
void
Triangle_Processor::Process( Stack<AtomicRegion>&  Offspring)
  {
  TimesCalled ++;
  if (TimesCalled == 1)
    {
    TheRule->Apply(LocalIntegrand(),Geometry(),Integral(),AbsoluteError());
    Offspring.MakeEmpty();
    return;
    };
  if(TimesCalled == 2)
    {
    real NewVolume
          = Geometry().Volume()/2;
    Stack<Triangle> Parts;
    Vector<unsigned int> DiffOrder(Diffs.Size());
    const real difffac = real(1)/real(0.45);    
    const real difftreshold = 1e-3;

    TheRule->ComputeDiffs(LocalIntegrand(),Geometry(),Diffs); 

    // Sort the differences in descending order.
    for (unsigned int ik=0 ; ik<=2 ; ik++)  { DiffOrder[ik] = ik; }
    for (unsigned int i=0 ; i<=1 ; i++)  
      {
     for (unsigned int k=i+1 ; k<=2 ; k++)
         if (Diffs[DiffOrder[k]]>Diffs[DiffOrder[i]])
            {
            unsigned int h = DiffOrder[i];
            DiffOrder[i] = DiffOrder[k];
            DiffOrder[k] = h;
            }
      }

    if (Diffs[DiffOrder[0]] < difftreshold)
      {
      TheDivisor4->Apply(Geometry(),Parts,DiffOrder);
      NewVolume /=2;
      }
    else 
      {
      if (Diffs[DiffOrder[0]]>difffac*Diffs[DiffOrder[2]])
        {
        TheDivisor2->Apply (Geometry(),Parts,DiffOrder);
        }
      else 
        { 
        TheDivisor4->Apply(Geometry(),Parts,DiffOrder);
        NewVolume /=2;
        }	
      };

    unsigned int N = Parts.Size();
    for (unsigned int ii =0;ii<N;ii++)
      {
      Triangle* g = Parts.Pop();
      g->Volume(NewVolume);
      Processor<Triangle>* p = Descendant();
      Atomic<Triangle>* a = new Atomic<Triangle>(g,p);
      a->LocalIntegrand(&LocalIntegrand());
      Offspring.Push(a);
      };
    return;
    };
   Error(TimesCalled > 2,
     "Triangle_Processor : more than two calls of Process()");
   }
///////////////////////////////////////////////
Processor<Triangle>*
Triangle_Processor::NewCopy()
const
  {
  return new Triangle_Processor(*this);
  }
///////////////////////////////////////////////
void 
Triangle_Processor::UseRule(Rule<Triangle>* r) 
  { 
  TheRule = r; 
  } 
///////////////////////////////////////////////
void
Triangle_Processor::Divide(unsigned int N, Stack<AtomicRegion>&  Offspring)
  {
  Stack<Triangle> Parts;  
  Vector<unsigned int> DiffOrder(Diffs.Size());
  real NewVolume;
  
  switch(N)
    {
    case 2: 
    {    
    NewVolume = Geometry().Volume()/2;

    TheRule->ComputeDiffs(LocalIntegrand(),Geometry(),Diffs);

    // Sort the differences in descending order.
    for (unsigned int ik=0 ; ik<=2 ; ik++)  { DiffOrder[ik] = ik; }
    for (unsigned int i=0 ; i<=1 ; i++)  
      {
      for (unsigned int k=i+1 ; k<=2 ; k++)
         if (Diffs[DiffOrder[k]]>Diffs[DiffOrder[i]])
            {
            unsigned int h = DiffOrder[i];
            DiffOrder[i] = DiffOrder[k];
            DiffOrder[k] = h;
            }
      }
    TheDivisor2->Apply (Geometry(),Parts,DiffOrder);
    break;
    }
  
    case 4:
    {
    NewVolume = Geometry().Volume()/4;
    TheDivisor4->Apply (Geometry(),Parts,DiffOrder);
    break;
    }
  
    default:
      {
        NewVolume = Geometry().Volume()/N; 
        Error(True,"This kind of subdivision is not implemented");
      }
    }
  
  
  for (unsigned int i =0;i<N;i++)
    {
    Triangle* g = Parts.Pop();
    g->Volume(NewVolume);
    Processor<Triangle>* p = Descendant();
    Atomic<Triangle>* a = new Atomic<Triangle>(g,p);
    a->LocalIntegrand(&LocalIntegrand());
    Offspring.Push(a);
    };
    
  return;

  }
///////////////////////////////////////////////  
