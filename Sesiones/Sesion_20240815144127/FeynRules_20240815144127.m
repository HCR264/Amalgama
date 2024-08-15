$FeynRulesPath = SetDirectory["/home/harold/Documents/Tesis/Programa/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documents/Tesis/Programa/Modelos"]
LoadModel["SMScalars.fr"]
FeynmanRules[LScalar]
WriteCHOutput[LScalar]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
