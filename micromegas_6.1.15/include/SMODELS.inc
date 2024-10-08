{
   char *VERSION="3.0.0";
   char smodels_database[100];
   char smodels_version[100];
   system("rm -f smodels.*");

   strcpy(smodelsInfo,VERSION);
   topology[0]=0;
   analysis[0]=0;
   status=0;
   Rvalue=0;
   Rexpected=0.;
   SmoLsig=INFINITY;
   SmoLmax=INFINITY;
   SmoLSM=INFINITY;

   CombRvalue=0;
   CombRexpected=0.;
   CombSmoLsig=INFINITY;
   CombSmoLmax=INFINITY;
   CombSmoLSM=INFINITY;
   CombAnalyses[0]=0;

   if(VERSION[0]<'2' || VERSION[0]>'9')
   {
      char command[100];
      sprintf(command, "echo  \" SModelS '%s' is not supported\n\" > smodels.err",VERSION);
      system(command);
      status=-5;
   }else
   {        
      char*command=(char*)malloc(strlen(micrO)+300 );
      sprintf(command,"%s/Packages/smodels-%s/runSModelS.py",micrO,VERSION);
      if(access(command,X_OK ))
      {  printf("Downloading SModelS v%s\n",VERSION);
         sprintf(command,"pwd=$PWD; cd  %s/Packages;  make -f SMODELS.makef VERSION=%s 1>$pwd/smodels.err 2>$pwd/smodels.err", micrO,VERSION); 
         system(command);
         sprintf(command,"%s/Packages/smodels-%s/runSModelS.py",micrO,VERSION);
         if(access(command,X_OK )) status=-4; else system("rm -f smodels.err");
      } 

      if(status==0) if(smodels(LHCrun,5/*nf*/, 0.005/*fb*/, "smodels.slha",VERSION, 0)) status=-2;
      if(status==0)
      {        
         sprintf(command,"%s/include/smodels_parameters.ini",micrO);
         FILE*ip=fopen(command,"r");
         FILE*pi=fopen("smodels_parameters.ini","w");
         char buff[200];
         for(;;)
         {  if(EOF==fscanf(ip,"%[^\n]\n",buff)) break;
            if(strstr(buff,"[parameters]"))
            {   
              fprintf(pi,"combineSRs = "); if(combineSRs)  fprintf(pi,"True\n"); else fprintf(pi,"False\n");
              if(combineAnas) fprintf(pi,"combineAnas = %s\n",combineAnas );
            }   
            fprintf(pi,"%s\n",buff);
         }  
         fclose(ip); 
         fclose(pi);   
         sprintf(command,"micrO=%s; python3  $micrO/Packages/smodels-%s/runSModelS.py -f smodels.slha -p smodels_parameters.ini -o ./ -v info 2>smodels.err\n"
                       "if(test $? -eq 0) then rm -f smodels.err; fi \n",micrO,VERSION);

         system(command);
         if(!access("smodels.err",R_OK )) status=-3;
         else 
         {        
            err=slhaRead("smodels.slha.smodelsslha", 1);
            slhaSTRFormat("SModelS_Settings"," 0 %s",smodels_version);
            slhaSTRFormat("SModelS_Settings"," 1 %s",smodels_database);
            sprintf(smodelsInfo,"%s with database %s",smodels_version, smodels_database);
            status=slhaVal("SModelS_Exclusion",0.,2,0,0); 
            if(status>=0)
            { 
               slhaSTRFormat("SModelS_Exclusion"," 1 0  %[^#]",topology);
               Rvalue=slhaVal("SModelS_Exclusion",0.,2,1,1);
               if (slhaValExists("SModelS_Exclusion",2,1,2)==1) Rexpected=slhaVal("SModelS_Exclusion",0.,2,1,2);
               if (slhaValExists("SModelS_Exclusion",2,1,6)==1) 
               {
                 SmoLsig=slhaVal("SModelS_Exclusion",0.,2,1,6);
                 SmoLmax=slhaVal("SModelS_Exclusion",0.,2,1,7);
                 SmoLSM=slhaVal("SModelS_Exclusion",0.,2,1,8);
               }  
               slhaSTRFormat("SModelS_Exclusion"," 1 4 %s",analysis);

               if (slhaValExists("SModelS_CombinedAnas",2,1,1)==1) 
               {
                 CombRvalue=slhaVal("SModelS_CombinedAnas",0.,2,1,1);
                 CombRexpected=slhaVal("SModelS_CombinedAnas",0.,2,1,2);
                 CombSmoLsig=slhaVal("SModelS_CombinedAnas",0.,2,1,3);
                 CombSmoLmax=slhaVal("SModelS_CombinedAnas",0.,2,1,4);
                 CombSmoLSM=slhaVal("SModelS_CombinedAnas",0.,2,1,5);
                 slhaSTRFormat("SModelS_CombinedAnas"," 1 6  %[^#]",CombAnalyses);
               }  

            }
         }
      }
      free(command);
   }
   if(status>=-2) smodelsOK=1; else smodelsOK=0; 
}
