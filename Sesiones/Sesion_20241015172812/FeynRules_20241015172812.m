$FeynRulesPath = SetDirectory["/home/harold/Documents/GitHub/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documents/GitHub/Amalgama/Modelos"]
LoadModel["InertDoublet.fr"]
FeynmanRules[LIDM]
WriteCHOutput[LIDM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
