$FeynRulesPath = SetDirectory["/home/harold/Documents/Tesis/Programa/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documents/Tesis/Programa/Modelos"]
LoadModel["SM_old.fr"]
FeynmanRules[LSM]
WriteCHOutput[LSM]
WriteFeynArtsOutput[LSM]
WriteSHOutput[LSM]
WriteLaTeXOutput[LSM]
WriteUFO[LSM]
(*WriteWOOutput[]*)
