$FeynRulesPath = SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/Modelos"]
LoadModel["SM_old.fr", "DM_Scalars.fr"]
FeynmanRules[LSM, LDM]
WriteCHOutput[LSM, LDM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
