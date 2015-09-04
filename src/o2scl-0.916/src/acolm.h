/*
  -------------------------------------------------------------------
  
  Copyright (C) 2006-2012, Andrew W. Steiner
  
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
/** \file acolm.h
    \brief The \ref o2scl_acol::acol_manager class header
*/
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <string>
#include <vector>
#include <fnmatch.h>
#include <o2scl/misc.h>
#include <o2scl/cli.h>
#include <o2scl/fit_nonlin.h>
#include <o2scl/table_units.h>
#include <o2scl/table3d.h>
#include <o2scl/format_float.h>
#include <o2scl/hdf_file.h>
#include <o2scl/hdf_io.h>
#include <o2scl/lib_settings.h>

#ifdef O2SCL_READLINE
#include <o2scl/cli_readline.h>
#else
#include <o2scl/cli.h>
#endif

/// A namespace for objects associated with the command-line utility 'acol'
namespace o2scl_acol {

  /** \brief The driver for 'acol' command-line utility
      \nothing

      \comment
      There was some concern about the confusion b/w the commands
      "get row by index" (get-row) and "get row by function"
      (find-row) and "select rows by function" (select-rows),
      but it might be ok.
      \endcomment

      \todo Rework so that the error handler isn't called prematurely.
      Ensure table::make_cols() and table::calc() don't call the error 
      handler.
      
      \todo Ensure add() copies constants and interpolation type,
      and units. 

      \future Stack-like operations (push, pop, swap, stack-list, etc.)

      \future Use get_input() in comm_create?

      \future Add functionality to ensure that three digit exponents
      are still handled gracefully (do this by creating a new boolean
      setting which, if true, always makes three spaces for
      exponents?)

      \future Fix insert and insert_full so that it automatically
      renames columns
      
      \future Allow "insert" commands to be restrictive, avoiding
      extrapolation
      
      \future Replace ~ with $HOME in filenames (this might be best
      done inside the \ref o2scl::cli class). (Some progress made.
      Function cli::expand_tilde() is written but not yet
      implemented.)
      
      \future New 3d commands: extract, transpose, contours, find_grid_x,
      find_grid_y, create-3d, etc.

      \hline
  */
  class acol_manager {

#ifndef DOXYGEN_INTERNAL

  protected:

#ifdef DOXYGEN
    /// A pointer to the table
    table_units<> *tabp;
#else
    o2scl::table_units<> *tabp;
#endif

#ifdef DOXYGEN
    /// The number formatter for html output
    format_float ffl;
#else
    o2scl::format_float ffl;
#endif

#ifdef DOXYGEN
    /// Pointer to the three dimensional table
    table3d *t3p;
#else
    o2scl::table3d *t3p;
#endif

    /// Convert units object (initialized by constructor to global object)
    o2scl::convert_units &cng;

    /// \name Parameters modifiable by the user
    //@{
    /// The output precision (default 6)
    int prec;

    /// The verbosity level (default 1)
    int verbose;

    /// True if we should make the output into neat columns (default true)
    bool pretty;
    
    /// True if we should output column names
    bool names_out;

    /// The name of the table
    std::string table_name;
  
    /// Filename for units command
    std::string unit_fname;

    /// Default arguments from environment
    std::string def_args;

    /// The number of columns requested by the user
    int user_ncols;

    /// True for scientific output mode
    bool scientific;
    //@}

    /// \name The parameter objects
    //@{
    o2scl::cli::parameter_string p_table_name;
    o2scl::cli::parameter_string p_unit_fname;
    o2scl::cli::parameter_string p_def_args;
    o2scl::cli::parameter_int p_verbose;
    o2scl::cli::parameter_int p_prec;
    o2scl::cli::parameter_int p_ncols;
    o2scl::cli::parameter_bool p_scientific;
    o2scl::cli::parameter_bool p_pretty;
    o2scl::cli::parameter_bool p_names_out;
    //@}

    /// Number of columns in screen
    int ncols;

    /// If true, the \table is 3d
    bool threed;

    /// Dummy cli object for cli::cli_gets()
#ifdef DOXYGEN
    cli *cl;
#else
    o2scl::cli *cl;
#endif

#endif

  public:

    acol_manager();

    virtual ~acol_manager() {}

    /** \brief True if we should run interactive mode after parsing
	the command-line
    */
    bool post_interactive;

    /// The environment variable to read from 
    std::string env_var_name;

    /// String parameters
    std::map<std::string,std::string *> str_params;

    /// Integer parameters
    std::map<std::string,int *> int_params;

  protected:

    /// Ensure \c col is unique from entries in \c cnames
    int make_unique_name(std::string &col, std::vector<std::string> &cnames);

  public:
    
    /** \brief Main run function

	Process command-line options using cli object, interface with
	the operating system via getenv(), instantiate and call the
	acol_manager object.
    */
    virtual int run(int argv, char *argc[]);

    /// Create the cli object (with readline support if available)
    virtual int setup_cli();

    /// Add the options to the cli object
    virtual int setup_options();

    /// Add the help text to the cli object
    virtual int setup_help();

    /// Add the parameters for 'set' to the cli object
    virtual int setup_parameters();

    /// Assign a constant
    virtual int comm_assign(std::vector<std::string> &sv, bool itive_com);

    /// Compute a scalar value
    virtual int comm_calc(std::vector<std::string> &sv, bool itive_com);

    /// Create a table from a column of equally spaced values
    virtual int comm_create(std::vector<std::string> &sv, bool itive_com);

    /// Delete a column
    virtual int comm_delete_col(std::vector<std::string> &sv, bool itive_com);

    /// Delete rows specified by a function
    virtual int comm_delete_rows(std::vector<std::string> &sv, bool itive_com);

    /// Create a column which is the derivative of another
    virtual int comm_deriv(std::vector<std::string> &sv, bool itive_com);

    /// Create a column which is the second derivative of another
    virtual int comm_deriv2(std::vector<std::string> &sv, bool itive_com);

    /// Parameters for iterate_func()
    typedef struct {
      std::string tname;
      o2scl_hdf::hdf_file *hf;
      bool found;
      std::string type;
      int verbose;
    } iter_parms;

    /// HDF object iteration function
    static herr_t iterate_func(hid_t loc, const char *name, 
			       const H5L_info_t *inf, void *op_data);
    
    /// HDF object iteration function
    static herr_t filelist_func(hid_t loc, const char *name, 
				const H5L_info_t *inf, void *op_data);
    
    /// Read a file
    virtual int comm_read(std::vector<std::string> &sv, bool itive_com);

    /// Read a file and list the O2scl objects
    virtual int comm_filelist(std::vector<std::string> &sv, bool itive_com);

    /// Find a row from a function
    virtual int comm_find_row(std::vector<std::string> &sv, bool itive_com);
    
    /// Create a column from a function
    virtual int comm_function(std::vector<std::string> &sv, bool itive_com);

    /// Read a generic data file
    virtual int comm_generic(std::vector<std::string> &sv, bool itive_com);

    /// Print out an entire row
    virtual int comm_get_row(std::vector<std::string> &sv, bool itive_com);

    /// Fit two columns to a function
    virtual int comm_fit(std::vector<std::string> &sv, bool itive_com);
    
    /// Create an html file
    virtual int comm_html(std::vector<std::string> &sv, bool itive_com);

    /// Insert a column from an external table using interpolation
    virtual int comm_insert(std::vector<std::string> &sv, bool itive_com);

    /// Insert an external table using interpolation
    virtual int comm_insert_full(std::vector<std::string> &sv, bool itive_com);

    /// Create a column which is the integral of another
    virtual int comm_integ(std::vector<std::string> &sv, bool itive_com);

    /// Toggle interactive mode
    virtual int comm_interactive(std::vector<std::string> &sv, bool itive_com);

    /// Output to a file in internal format
    virtual int comm_internal(std::vector<std::string> &sv, bool itive_com);

    /// Create an html file
    virtual int comm_interp(std::vector<std::string> &sv, bool itive_com);

    /// List columns in table 'tp' named 'tname' assuming screen size 'ncol'
    virtual int comm_list(std::vector<std::string> &sv, bool itive_com);

    /// Compute the maximum value of a colum
    virtual int comm_max(std::vector<std::string> &sv, bool itive_com);
    
    /// Compute the minimum value of a colum
    virtual int comm_min(std::vector<std::string> &sv, bool itive_com);
    
    /// Add a column for line numbers
    virtual int comm_index(std::vector<std::string> &sv, bool itive_com);

    /// Output to screen or file
    virtual int comm_output(std::vector<std::string> &sv, bool itive_com);

    /// Get or set the current interpolation type
    virtual int comm_interp_type(std::vector<std::string> &sv, bool itive_com);

    /// Preview the table
    virtual int comm_preview(std::vector<std::string> &sv, bool itive_com);

    /// Add two table3d objects
    virtual int comm_add(std::vector<std::string> &sv, bool itive_com);

    /// Rename a column
    virtual int comm_rename(std::vector<std::string> &sv, bool itive_com);

    /// Select several columns for a new table
    virtual int comm_select(std::vector<std::string> &sv, bool itive_com);

    /// Select several rows for a new table
    virtual int comm_select_rows(std::vector<std::string> &sv, bool itive_com);

    /// Post-processing for setting a value
    virtual int comm_set(std::vector<std::string> &sv, bool itive_com);

    /// Set an individual data point at a specified row and column
    virtual int comm_set_data(std::vector<std::string> &sv, bool itive_com);
    
    /// Set units of a column
    virtual int comm_set_unit(std::vector<std::string> &sv, bool itive_com);
    
    /// Set units of a column
    virtual int comm_show_units(std::vector<std::string> &sv, bool itive_com);
    
    /// Get units of a column
    virtual int comm_get_unit(std::vector<std::string> &sv, bool itive_com);
    
    /// Convert units of a column
    virtual int comm_convert_unit(std::vector<std::string> &sv, 
				  bool itive_com);
    
    /// Sort the table by a column
    virtual int comm_sort(std::vector<std::string> &sv, bool itive_com);

    /// Get column stats
    virtual int comm_stats(std::vector<std::string> &sv, bool itive_com);

    /// Print version
    virtual int comm_version(std::vector<std::string> &sv, bool itive_com);

    /// Get a conversion factor
    virtual int comm_get_conv(std::vector<std::string> &sv, bool itive_com);

    /// Set screen witdth
    int set_swidth(int ncol) {
      ncols=ncol;
      return 0;
    }

  protected:
    
    /** \brief Separate string into words delimited by whitespace 
	(for comm_fit())
    */
    int separate(std::string str, std::vector<std::string> &sv);

    /// An internal command for prompting the user for command arguments
    int get_input(std::vector<std::string> &sv, 
		  std::vector<std::string> &directions,
		  std::vector<std::string> &in, std::string comm_name,
		  bool itive_com);

    /// An internal command for prompting the user for one command argument
    int get_input_one(std::vector<std::string> &sv, std::string directions,
		   std::string &in, std::string comm_name,
		   bool itive_com);
  };

}