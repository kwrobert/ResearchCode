@echo off
if "%1"=="" goto 1
if not exist examples\vb%1.c goto 3
copy examples\vb%1.c code\main.c
chdir code
del main.obj
del tst.*
make tst.out
rename tst.out vb%1.out
chdir ..
goto 2
:3 
echo    You have entered an invalid option.
pause
:1
type examples\examples³
echo   Type 'testcase 1'   etc. at the DOS            
echo   prompt to activate one of these options.       
:2

