$FeynRulesPath = SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/Modelos"]
LoadModel["Scalar_Alba.fr", "SM_old.fr"]
FeynmanRules[Lax, LSM]
WriteCHOutput[Lax, LSM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
