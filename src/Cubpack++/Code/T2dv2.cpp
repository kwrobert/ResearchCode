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
//////////////////////////////////////////////////
//File T2dv2.cpp
// History:
//   (date)          (version)
//    1 May 1999     V1.2 ( 2/4 division introduced  )
//
/////////////////////////////////////////////////
#include "point.h"
#include "stack.h"
#include "T2dv2.h"
//////////////////////////////////////////////////
void
Triangle_Divide2::Apply (const Triangle& t,Stack<Triangle>& Offspring,
                         const Vector<unsigned int>& D)
  {

  Point m = (t.Vertex((D[0]+1)%3)+t.Vertex((D[0]+2)%3))/2;

//  std::cout << t.Vertex(0) << " " << t.Vertex(1) << " " << t.Vertex(2) << endl;

  Vector<Point> VP(3);
  
  for (unsigned int i=0 ; i<=2 ; i++)  { VP[i] = t.Vertex(i); };
  VP[(D[0]+1)%3] = m;
  Triangle* t1 =  new Triangle(VP[0],VP[1],VP[2]);

//  std::cout << VP[0] << " " << VP[1] << " " << VP[2] << endl;

  for (unsigned int l=0 ; l<=2 ; l++)  { VP[l] = t.Vertex(l); };
  VP[(D[0]+2)%3] = m;
  Triangle* t2 =  new Triangle(VP[0],VP[1],VP[2]);

//  std::cout << VP[0] << " " << VP[1] << " " << VP[2] << endl;

  Offspring.Push(t1);
  Offspring.Push(t2);
  }
//////////////////////////////////////////////////
Triangle_Divide2::Triangle_Divide2()
  :SameShapeDivisor<Triangle>()
  {
  }
//////////////////////////////////////////////////
