$FeynRulesPath = SetDirectory["/home/harold/Documentos/GitHub/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/GitHub/Amalgama/Modelos"]
LoadModel["InertDoublet.fr", "SM_old.fr"]
FeynmanRules[LIDM]
WriteCHOutput[LIDM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
