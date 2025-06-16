data = Import["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/micromegas_6.1.15/MO_Sesion_20250516140556/Results/results_Prueba1.txt", "Table"][[All,{1,1,1}]];
data = Rest[data];
interpolData = Interpolation[data, InterpolationOrder -> 1];
plot = ContourPlot[interpolData[x,y], {x,,}, {y,,}, Contours -> {}, ContourShading -> True, ColorFunction -> (Blend[{Blue, Green, Red}, #] &), ScalingFunctions -> {"Linear", "Log"}, PlotRange -> All, PlotLegends -> Automatic]; 
Export["Plot.pdf",plot];
