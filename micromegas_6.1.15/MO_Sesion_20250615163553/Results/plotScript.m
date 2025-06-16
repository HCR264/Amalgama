data = Import["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/micromegas_6.1.15/MO_Sesion_20250615163553/Results/results_.txt", "Table"][[All,{2,1,3}]];
data = Rest[data];
interpolData = Interpolation[data, InterpolationOrder -> 1];
plot = ContourPlot[interpolData[x,y], {x,10,90}, {y,10^-3,10^1}, Contours -> {0.112}, ContourShading -> True, ColorFunction -> (Blend[{White, Green, Gray}, #] &), ScalingFunctions -> {"Linear", "Log"}, PlotRange -> All, PlotLegends -> Automatic] 
Export["Plot.pdf",plot]
