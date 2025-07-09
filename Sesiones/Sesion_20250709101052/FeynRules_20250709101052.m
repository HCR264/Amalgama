$FeynRulesPath = SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/feynrules-current"]
<<FeynRules`
SetDirectory["/home/harold/Documentos/Repositorios/Proyectos/Amalgama/Modelos"]
LoadModel["InertDoublet.fr"]
FeynmanRules[LIDM]
WriteCHOutput[LIDM]
(*WriteFeynArtsOutput[]*)
(*WriteSHOutput[]*)
(*WriteLaTeXOutput[]*)
(*WriteUFO[]*)
(*WriteWOOutput[]*)
