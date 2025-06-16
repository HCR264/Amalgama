data = Import["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/micromegas_6.1.15/MO_Sesion_20250610133046/Results/results_Prueba_1.txt", "Table"][[All,{3,1,2}]];
data = Rest[data];
interpolData = Interpolation[data, InterpolationOrder -> 1];
plot = ContourPlot[interpolData[x,y], {x,,}, {y,,}, Contours -> {}, ContourShading -> True, ColorFunction -> (Blend[{Blue, Green, Red}, #] &), ScalingFunctions -> {"Linear", "Log"}, PlotRange -> All, PlotLegends -> Automatic]; 
Export["Plot.pdf",plot];
