$FeynRulesPath = SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/Modelos"]
LoadModel["Scalar_Alba.fr"]
FeynmanRules[Lax]
WriteCHOutput[Lax]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
