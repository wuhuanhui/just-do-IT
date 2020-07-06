#### gprof
"gprof" produces an execution  profile of C, Pascal, or Fortran77 programs.  The effect of called routines is incorporated in the profile of each caller.  
- 使用gprof命令来分析记录程序运行信息的gmon.out文件，如：gprof test.exe gmon.out则可以在显示器上看到函数调用相关的统计、分析信息
- gprof test.exe gmon.out> gprofresult.txt重定向到文本文件以便于后续分析