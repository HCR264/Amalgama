#include<string.h>
#include <pthread.h>
#include"VandP.h"


double usrFF_(int n_in, int n_out,double * pvect,char**pnames,int*pdg)
{ return  usrFF(n_in,n_out,pvect,pnames,pdg);}
double usrfun_(char * name,int n_in, int n_out,double * pvect,char**pnames,int*pdg) 
{ return  usrfun(name,n_in,n_out,pvect,pnames,pdg);}


extern int findval(char *name,double *val);
extern int qnumbers(char*pname, int *spin2, int * charge3, int * cdim);

int findval(char *name,double *val)
{ int i;
  for(i=0;i<nModelVars+nModelFunc;i++) 
  if(!strcmp(name,varNames[i])){ *val= varValues[i]; return 0;}  
  return 1;
}


int qnumbers(char*pname, int *spin2, int * charge3, int * cdim)
{
   int n,sign;
   for(n=0;n<nModelParticles;n++)
   { 
     if(!strcmp(pname,ModelPrtcls[n].name )) {sign=1; break;} 
     if(!strcmp(pname,ModelPrtcls[n].aname)) {sign=-1;break;}
   }
   if(n==nModelParticles) return 0;

   if(spin2)   *spin2  =ModelPrtcls[n].spin2;
   if(charge3) *charge3=sign*ModelPrtcls[n].q3;
   if(cdim)    
   {  *cdim   =ModelPrtcls[n].cdim; 
      if(sign==-1 &&(*cdim==3 || *cdim==-3)) (*cdim)*=-1;
   }
   return sign*ModelPrtcls[n-1].NPDG;
}
