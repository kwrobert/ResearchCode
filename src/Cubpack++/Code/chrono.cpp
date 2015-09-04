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
//File chrono.c
// History:
//   (date)          (version)
//   19 Aug 1994     V0.1 (first limited distribution)
//   28 Mar 1996     V0.1h(long instead of int)
//    1 Aug 1996     V1.0 (paper accepted by ACM TOMS)
//   19 Feb 1997     V1.1 (TIMES added)
//
/////////////////////////////////////////////////////////

#include "chrono.h"

#ifdef GETRUSAGE
#include <sys/time.h>
#include <sys/resource.h>
#endif

#ifdef TIMES
#include "real.h" 
#include <sys/times.h>
#include <sys/types.h>
#ifdef __ultrix
#define _POSIX_SOURCE
#endif // __ultrix
#include "time.h"
#ifdef __ultrix
#undef _POSIX_SOURCE
#endif // __ultrix
#endif

/////////////////////////////////////////////////////////
Chrono::Chrono()
  {
  Reset();
  }
/////////////////////////////////////////////////////////
void
Chrono::Start()
  {
  if ( !Running)
    {
    Time= OldTime = times_();
    Running =True;
    };
  }
/////////////////////////////////////////////////////////
void
Chrono::Stop()
  {
  if (Running)
    {
    Time = times_();
    Running =False;
    };
  }
/////////////////////////////////////////////////////////
void
Chrono::Reset()
  {
  Time=0;
  OldTime=0;
  Running = False;
  }
/////////////////////////////////////////////////////////
unsigned long   
Chrono::Read()
  {
  if (Running)
    {
    return (times_() - OldTime);
    }
  else
    {
    return (Time -OldTime);
    };
  }
/////////////////////////////////////////////////////////
long
Chrono::times_ ()
  {
  long t=0;
#ifdef GETRUSAGE
   struct rusage  info ;
   struct timeval *user_t = &(info.ru_utime), *sys_t  = &(info.ru_stime) ;

   getrusage (0, &info) ;

   // convert (seconds,microseconds) to milliseconds
   t += user_t->tv_sec * 1000 + user_t->tv_usec / 1000 ;
   t += sys_t->tv_sec  * 1000 + sys_t->tv_usec  / 1000 ;
#endif
#ifdef TIMES
  struct tms tms; 
  times(&tms); 

  t = tms.tms_utime + tms.tms_stime;   // this is in  clock_ticks 
  // conversion of clock_ticks to milliseconds
  t = long(real(t)*real(1000)/real(CLK_TCK));
#endif

  return t;
  }
/////////////////////////////////////////////////////////
