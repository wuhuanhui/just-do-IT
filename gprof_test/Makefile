# Makefile

.PHONY : all debug release clean


define MAKE_OBJ
@mkdir objs -p
#$(foreach OBJ, $(CPPOBJS), $(CXX) -o objs/$(OBJ).o -c $(SRCPATH)/$(OBJ).cpp $(CFLAG) $(INCFLAG) $(ENDLINE))
$(foreach OBJ, $(COBJS), $(CC) -o objs/$(OBJ).o -c $(SRCPATH)/$(OBJ).c $(CFLAG) $(INCFLAG) $(ENDLINE))
endef

define LINK_OBJ
$(CC) -o $(TARGET) objs/*.o $(DEPOBJS) $(LFLAG) $(LIBFLAB) $(LIBS)
endef


CC := gcc
CXX := g++
LFLAG := -pg
INCFLAG := 
LIBFLAB := 
LIBS := 
DIRS := 
SRCPATH := .
CPPOBJS := 
COBJS := test func
DEPOBJS := 

TARGET := test_gprof.out

all : debug

debug : CFLAG = -pg  -pipe -Wall -W
debug :
	@set -e; for d in $(DIRS); do $(MAKE) -C $$d debug; done
	$(MAKE_OBJ)
	$(LINK_OBJ)
#	@echo "111111"
release : CFLAG = -g -O2 -pipe -Wall -W -DEH_NDEBUG
release :
	@set -e; for d in $(DIRS); do $(MAKE) -C $$d release; done
	$(MAKE_OBJ)
	$(LINK_OBJ)

clean:
	@for d in $(DIRS); do $(MAKE) -C $$d clean; done
	@rm objs $(TARGET) -rf
