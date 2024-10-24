#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../CalcHEP_src/include/extern.h"
#include "../../CalcHEP_src/include/VandP.h"
#include "autoprot.h"
extern int  FError;
/*  Special model functions  */
extern int access(const char *pathname, int mode);

int nModelParticles=20;
static ModelPrtclsStr ModelPrtcls_[20]=
{
  {"ne","Ne",0, 12, "Mnue","0",1,1,2,0}
, {"nm","Nm",0, 14, "Mnum","0",1,1,2,0}
, {"nl","Nl",0, 16, "Mnut","0",1,1,2,0}
, {"e","E",0, 11, "Me","0",1,1,2,-3}
, {"m","M",0, 13, "MM","0",1,1,2,-3}
, {"l","L",0, 15, "MTA","0",1,1,2,-3}
, {"u","U",0, 2, "MU","0",1,3,6,2}
, {"c","C",0, 4, "MC","0",1,3,6,2}
, {"t","T",0, 6, "MT","WT",1,3,6,2}
, {"d","D",0, 1, "MD","0",1,3,6,-1}
, {"s","S",0, 3, "MS","0",1,3,6,-1}
, {"b","B",0, 5, "MB","0",1,3,6,-1}
, {"a","a",1, 22, "0","0",2,1,2,0}
, {"Z","Z",1, 23, "MZ","WZ",2,1,3,0}
, {"W+","W-",0, 24, "MW","WW",2,1,3,3}
, {"g","g",1, 21, "0","0",2,8,16,0}
, {"h","h",1, 25, "mh","Wh",0,1,1,0}
, {"~H0","~H0",1, 35, "MH0","WH0",0,1,1,0}
, {"~A0","~A0",1, 36, "MA0","WA0",0,1,1,0}
, {"~H+","~H-",0, 37, "MHch","WHch",0,1,1,3}
};
ModelPrtclsStr *ModelPrtcls=ModelPrtcls_; 
int nModelVars=26;
int nModelFunc=26;
static int nCurrentVars=25;
int*currentVarPtr=&nCurrentVars;
static char*varNames_[52]={
 "aEWM1","Gf","MMZ","MMW","MMC","MMB","MMT","aS","QS","lamL"
,"lam2","mmh","mmH0","mmA0","mmHch","Mnue","Mnum","Mnut","Me","MM"
,"MTA","MU","MD","MS","E","Pi","MZ","MW","MC","MB"
,"MT","EE","CW2","SW2","CW","SW","g1","g2","v","CKM1x1"
,"CKM1x2","CKM1x3","CKM2x1","CKM2x2","CKM2x3","CKM3x1","CKM3x2","CKM3x3","mh","MH0"
,"MA0","MHch"};
char**varNames=varNames_;
static REAL varValues_[52]={
   7.757952E-03,  1.166370E-05,  9.118760E+01,  7.994700E+01,  1.200000E+00,  4.230000E+00,  1.750000E+02,  1.172000E-01,  1.000000E+02,  1.000000E-04
,  5.000000E-04,  1.000000E+02,  7.000000E+04,  1.200000E+05,  2.000000E+05,  0.000000E+00,  0.000000E+00,  0.000000E+00,  0.000000E+00,  1.057000E-01
,  1.777000E+00,  0.000000E+00,  0.000000E+00,  1.000000E-01,  2.718282E+00,  3.141593E+00};
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
   nCurrentVars=26;
   V[26]=V[2];

   nCurrentVars=27;
   V[27]=V[3];

   nCurrentVars=28;
   V[28]=V[4];

   nCurrentVars=29;
   V[29]=V[5];

   nCurrentVars=30;
   V[30]=V[6];

   nCurrentVars=31;
   V[31]=2*Pow(V[0],0.5)*Pow(V[25],0.5);
   if(!isfinite(V[31]) || FError) return 31;
   nCurrentVars=32;
   V[32]=Pow(V[27],2)*Pow(V[26],-2);
   if(!isfinite(V[32]) || FError) return 32;
   nCurrentVars=33;
   V[33]=1-V[32];
   if(!isfinite(V[33]) || FError) return 33;
   nCurrentVars=34;
   V[34]=Pow(V[32],0.5);
   if(!isfinite(V[34]) || FError) return 34;
   nCurrentVars=35;
   V[35]=Pow(V[33],0.5);
   if(!isfinite(V[35]) || FError) return 35;
   nCurrentVars=36;
   V[36]=V[31]*Pow(V[34],-1);
   if(!isfinite(V[36]) || FError) return 36;
   nCurrentVars=37;
   V[37]=V[31]*Pow(V[35],-1);
   if(!isfinite(V[37]) || FError) return 37;
   nCurrentVars=38;
   V[38]=0.8408964152537146*Pow(V[1],-0.5);
   if(!isfinite(V[38]) || FError) return 38;
   nCurrentVars=39;
   V[39]=0.97428;

   nCurrentVars=40;
   V[40]=0.2253;

   nCurrentVars=41;
   V[41]=0.00347;

   nCurrentVars=42;
   V[42]=0.2252;

   nCurrentVars=43;
   V[43]=0.97345;

   nCurrentVars=44;
   V[44]=0.041;

   nCurrentVars=45;
   V[45]=0.00862;

   nCurrentVars=46;
   V[46]=0.0403;

   nCurrentVars=47;
   V[47]=0.999152;

   nCurrentVars=48;
   V[48]=V[11];

   nCurrentVars=49;
   V[49]=V[12];

   nCurrentVars=50;
   V[50]=V[13];

   nCurrentVars=51;
   V[51]=V[14];

   if(VV==NULL) 
   {  VV=malloc(sizeof(REAL)*nModelVars);
      for(i=0;i<nModelVars;i++) if(strcmp(varNames[i],"Q")==0) iQ=i;
   }
   for(i=0;i<nModelVars;i++) VV[i]=V[i];
   cErr=0;
   nCurrentVars++;
   return 0;
}
