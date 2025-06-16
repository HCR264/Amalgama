data = Import["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/micromegas_6.1.15/MO_Sesion_20250610141123/Results/results_Prueba_2.txt", "Table"][[All,{2,1,3}]];
data = Rest[data];
interpolData = Interpolation[data, InterpolationOrder -> 1];
plot = ContourPlot[interpolData[x,y], {x,30,80}, {y,10^-4,10}, Contours -> {0.12}, ContourShading -> True, ColorFunction -> (Blend[{Blue, Green, Red}, #] &), ScalingFunctions -> {"Linear", "Log"}, PlotRange -> All, PlotLegends -> Automatic]; 
Export["Plot.pdf",plot];
