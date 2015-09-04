/*
  -------------------------------------------------------------------
  
  Copyright (C) 2006-2014, Andrew W. Steiner
  
  This file is part of O2scl.
  
  O2scl is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.
  
  O2scl is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with O2scl. If not, see <http://www.gnu.org/licenses/>.

  -------------------------------------------------------------------
*/

/* Example: ex_table.cpp
   -------------------------------------------------------------------
*/

#include <iostream>
#include <o2scl/table.h>
#include <o2scl/constants.h>
#include <o2scl/test_mgr.h>
#ifdef O2SCL_HDF
#include <o2scl/hdf_file.h>
#include <o2scl/hdf_io.h>
#endif

using namespace std;
using namespace o2scl;
#ifdef O2SCL_HDF
using namespace o2scl_hdf;
#endif

int main(void) {

  cout.setf(ios::scientific);
  
  test_mgr t;
  t.set_output_level(1);

  // Create a table with two columns. It is usually best to
  // specify in the constructor, the number of rows you will 
  // need before hand, i.e. table dat(100), but we do not
  // do so here for demonstration purposes.
  table<> dat;
  dat.line_of_names("x y");
  
  for(int i=0;i<11;i++) {
    dat.set("x",i,((double)i)/10.0);
    dat.set("y",i,sin(dat.get("x",i)));
  }
  
  // We demonstrate interpolation and differentiation and 
  // compare with the exact answers
  cout << " Result        Expected" << endl;
  cout << "----------------------------" << endl;
  cout << " " << dat.interp("y",0.5,"x") << "  " << asin(0.5) << endl;
  cout << " " << dat.deriv("x",0.5,"y") << "  " << cos(0.5) << endl;
  cout << dat.deriv2("x",0.5,"y") << " " << -sin(0.5) << endl;
  cout << endl;

  dat.new_column("cx");
  dat.new_column("sx");
  for(size_t i=0;i<dat.get_nlines();i++) {
    dat.set("sx",i,dat["y"][i]);
    dat.set("cx",i,sqrt(1.0-pow(dat["sx"][i],2.0)));
  }

  dat.add_constant("pi",acos(-1.0));

  dat.new_column("s2");
  for(size_t i=0;i<dat.get_nlines();i++) {
    dat.set("s2",i,sin(dat["x"][i]*acos(-1.0)/2.0));
  }

  // We get approximate derivatives for an entire column
  dat.deriv("x","sx","cx2");

#ifdef O2SCL_HDF
  hdf_file hf;
  hf.open_or_create("ex_table.o2");
  hdf_output(hf,dat,"table");
  hf.close();
#endif
  
  t.report();
  return 0;
}
// End of example