$FeynRulesPath = SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/Modelos"]
LoadModel["DM_Scalars.fr", "SM.fr"]
FeynmanRules[LDM, LSM]
WriteCHOutput[LDM, LSM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
