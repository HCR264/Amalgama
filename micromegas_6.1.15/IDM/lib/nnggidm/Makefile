.PHONY: clean all

LOOPTOOLS = ../../../Packages/LoopTools_2.12-v0

all: $(LOOPTOOLS)/FlagsForMake $(LOOPTOOLS)/build/libooptools.a 
	$(MAKE)  -f makeCompile
	
 $(LOOPTOOLS)/FlagsForMake:
	cd $(LOOPTOOLS); ./configure
 	
 $(LOOPTOOLS)/build/libooptools.a: $(LOOPTOOLS)/FlagsForMake
	 $(MAKE)  -C $(LOOPTOOLS)

clean:
	rm -f nngg.a util.a lGamma.exe *.o */*.o 	