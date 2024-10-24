#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../CalcHEP_src/include/extern.h"
#include "../../CalcHEP_src/include/VandP.h"
#include "autoprot.h"
extern int  FError;
/*  Special model functions  */
extern int access(const char *pathname, int mode);

int nModelParticles=21;
static ModelPrtclsStr ModelPrtcls_[21]=
{
  {"~S1","~S1",1, 9000001, "MSk","0",0,1,1,0}
, {"~S2","~S2",1, 9000002, "MSk","0",0,1,1,0}
, {"~S3","~S3",1, 9000003, "MSk","0",0,1,1,0}
, {"~S4","~S4",1, 9000004, "MSk","0",0,1,1,0}
, {"ve","ve~",0, 12, "0","0",1,1,2,0}
, {"vm","vm~",0, 14, "0","0",1,1,2,0}
, {"vt","vt~",0, 16, "0","0",1,1,2,0}
, {"e-","e+",0, 11, "Me","0",1,1,2,-3}
, {"m-","m+",0, 13, "MM","0",1,1,2,-3}
, {"tt-","tt+",0, 15, "MTA","0",1,1,2,-3}
, {"u","u~",0, 2, "MU","0",1,3,6,2}
, {"c","c~",0, 4, "MC","0",1,3,6,2}
, {"t","t~",0, 6, "MT","WT",1,3,6,2}
, {"d","d~",0, 1, "MD","0",1,3,6,-1}
, {"s","s~",0, 3, "MS","0",1,3,6,-1}
, {"b","b~",0, 5, "MB","0",1,3,6,-1}
, {"A","A",1, 22, "0","0",2,1,2,0}
, {"Z","Z",1, 23, "MZ","WZ",2,1,3,0}
, {"W+","W-",0, 24, "MW","WW",2,1,3,3}
, {"G","G",1, 21, "0","0",2,8,16,0}
, {"H","H",1, 25, "MH","WH",0,1,1,0}
};
ModelPrtclsStr *ModelPrtcls=ModelPrtcls_; 
int nModelVars=29;
int nModelFunc=2;
static int nCurrentVars=28;
int*currentVarPtr=&nCurrentVars;
static char*varNames_[31]={
 "lS","om","aEWM1","Gf","aS","ymdo","ymup","yms","ymc","ymb"
,"ymt","yme","ymm","ymtau","cabi","MSk","Me","MM","MTA","MU"
,"MC","MT","MD","MS","MB","MZ","MH","E","Pi","aEW"
,"MW"};
char**varNames=varNames_;
static REAL varValues_[31]={
   5.000000E-01,  5.000000E-01,  1.279000E+02,  1.166370E-05,  1.184000E-01,  5.040000E-03,  2.550000E-03,  1.010000E-01,  1.270000E+00,  4.700000E+00
,  1.720000E+02,  5.110000E-04,  1.056600E-01,  1.777000E+00,  2.277360E-01,  4.000000E+01,  5.110000E-04,  1.056600E-01,  1.777000E+00,  2.550000E-03
,  1.420000E+00,  1.720000E+02,  5.040000E-03,  1.010000E-01,  4.700000E+00,  9.118760E+01,  1.200000E+02,  2.718282E+00,  3.141593E+00};
REAL*varValues=varValues_;
int calcMainFunc(void)
{
   int i;
   static REAL * VV=NULL;
   static int iQ=-1;
   static int cErr=1;
   REAL *V=varValues;
   FError=0;
   if(VV && cErr==0)
   { for(i=0;i<nModelVars;i++) if(i!=iQ && VV[i]!=V[i]) break;
     if(i==nModelVars)     return 0;
   }
  cErr=1;
   nCurrentVars=29;
   V[29]=Pow(V[2],-1);
   if(!isfinite(V[29]) || FError) return 29;
   nCurrentVars=30;
   V[30]=Pow(Pow(V[25],2)/(2.)+Pow(Pow(V[25],4)/(4.)-V[29]*V[28]*Pow(2,-0.5)*Pow(V[3],-1)*Pow(V[25],2),0.5),0.5);
   if(!isfinite(V[30]) || FError) return 30;
   if(VV==NULL) 
   {  VV=malloc(sizeof(REAL)*nModelVars);
      for(i=0;i<nModelVars;i++) if(strcmp(varNames[i],"Q")==0) iQ=i;
   }
   for(i=0;i<nModelVars;i++) VV[i]=V[i];
   cErr=0;
   nCurrentVars++;
   return 0;
}
