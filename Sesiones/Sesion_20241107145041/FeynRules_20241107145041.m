$FeynRulesPath = SetDirectory["/home/harold/Documentos/GitHub/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/GitHub/Amalgama/Modelos"]
LoadModel["SM.fr", "Scalar_Alba.fr"]
FeynmanRules[Lax]
WriteCHOutput[Lax]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
