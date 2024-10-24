$FeynRulesPath = SetDirectory["/home/harold/Documentos/GitHub/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/GitHub/Amalgama/Modelos"]
LoadModel["SMScalars.fr", "SM_old.fr"]
FeynmanRules[LScalar]
WriteCHOutput[LScalar]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
