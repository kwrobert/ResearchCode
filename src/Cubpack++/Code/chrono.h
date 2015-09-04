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
// File : chrono.h
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   28 Mar 1996     V0.1h(long instead of int)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//   19 Feb 1997     V1.1 (TIMES added)
/////////////////////////////////////////////////////////
// DEFINITION OF CLASS Chrono
// --------------------------
//
// BASECLASSES:
//   Counter
//
// PURPOSE:
//   Chrono implements a simple stop-watch; it can be used for
//   all sorts of timings. At the moment it will only give
//   useful results when compiled with an appropriate flag.
//   If no such flag is provided, Read() will always return 0.
//
//   On a system that has a getrusage() system call, one must
//   compile using -DGETRUSAGE.
//
//   On a system that has a times() system call, one must compile
//   using -DTIMES.
//
// TEMPLATES:
//   None
//
// METHODS:
//   CONSTRUCTORS:
//     1) Chrono()
//     -----------
//     Default constructor. The stop-watch isn't running after
//     construction.
//   SELECTORS:
//     1) unsigned long Read()
//     ----------------
//     Read reads out the time in milliseconds. Currently it
//     is accurate up to one millisecond.
//   MODIFIERS:
//     1) void Start()
//     ---------------
//     Start() makes the stop-watch running. Successive calls
//     of Start() have no effect.
//     2) void Stop()
//     ---------------
//     Stops the stop-watch. After Stop(), Read() will always
//     read out the same value, until the stop-watch is started
//     again. Stopping a stopped stop-watch has no effect.
//     3) void Reset()
//     ---------------
//     After a call of Reset(), Read() will read out zero,
//     until the stop-watch is started again. A running
//     stop-watch should not be Reset().
//
//   OPERATORS:
//     None
//   SPECIAL:
//     None
//////////////////////////////////////////////////////////

#ifndef CHRONO_H
#define CHRONO_H

//////////////////////////////////////////////////////////
#include "counter.h"
#include "boolean.h"

//////////////////////////////////////////////////////////

class Chrono :public Counter
  {
  public:

  Chrono();
  void Start();
  void Stop();
  void Reset();
  unsigned long Read();

  private:

  long Time;
  long OldTime;
  Boolean Running;
  long times_();
  };
/////////////////////////////////////////////////////////
#endif
