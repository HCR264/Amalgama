(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)
(*                                                                             *)
(*         This file has been automatically generated by FeynRules.            *)
(*                                                                             *)
(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)


FR$ModelInformation={
  ModelName->"SM_Plus_Scalars",
  Authors -> "C. Duhr",
  Institutions -> "Universite catholique de Louvain (CP3).",
  Emails -> "claude.duhr@uclouvain.be",
  Date -> "14. 06. 2009",
  Version -> "1.0",
  URLs -> "http://feynrules.phys.ucl.ac.be/view/Main/StandardModelScalars",
  References -> "\"The minimal non-minimal Standard Model\", J.J. van der Bij, Phys.Lett.B636:56-59,2006, hep-ph/0603082"};

FR$ClassesTranslation={};

FR$InteractionOrderPerturbativeExpansion={{QCD, 0}, {QED, 0}};

FR$GoldstoneList={S[2], S[3]};

(*     Declared indices    *)

IndexRange[ Index[Generation] ] = Range[ 3 ]

IndexRange[ Index[Colour] ] = NoUnfold[ Range[ 3 ] ]

IndexRange[ Index[Gluon] ] = NoUnfold[ Range[ 8 ] ]

IndexRange[ Index[SU2W] ] = Range[ 3 ]

IndexRange[ Index[SGen] ] = Range[ 4 ]

(*     Declared particles    *)

M$ClassesDescription = {
F[1] == {
    SelfConjugate -> False,
    Indices -> {Index[Generation]},
    QuantumNumbers -> {LeptonNumber},
    PropagatorLabel -> "v",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0 },

F[2] == {
    SelfConjugate -> False,
    Indices -> {Index[Generation]},
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorLabel -> "l",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Ml },

F[3] == {
    SelfConjugate -> False,
    Indices -> {Index[Generation], Index[Colour]},
    QuantumNumbers -> {(2*Q)/3},
    PropagatorLabel -> "uq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Mu },

F[4] == {
    SelfConjugate -> False,
    Indices -> {Index[Generation], Index[Colour]},
    QuantumNumbers -> {-Q/3},
    PropagatorLabel -> "dq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Md },

U[1] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> uA,
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0 },

U[2] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> uZ,
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MZ },

U[31] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {Q, GhostNumber},
    PropagatorLabel -> uWp,
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW },

U[32] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {-Q, GhostNumber},
    PropagatorLabel -> uWm,
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW },

U[4] == {
    SelfConjugate -> False,
    Indices -> {Index[Gluon]},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> uG,
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0 },

V[1] == {
    SelfConjugate -> True,
    Indices -> {},
    PropagatorLabel -> "a",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> 0 },

V[2] == {
    SelfConjugate -> True,
    Indices -> {},
    PropagatorLabel -> "Z",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZ },

V[3] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {Q},
    PropagatorLabel -> "W",
    PropagatorType -> Sine,
    PropagatorArrow -> Forward,
    Mass -> MW },

V[4] == {
    SelfConjugate -> True,
    Indices -> {Index[Gluon]},
    PropagatorLabel -> G,
    PropagatorType -> Cycles,
    PropagatorArrow -> None,
    Mass -> 0 },

S[1] == {
    SelfConjugate -> True,
    PropagatorLabel -> "H",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MH,
    Indices -> {} },

S[2] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Phi",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {} },

S[3] == {
    SelfConjugate -> False,
    PropagatorLabel -> "Phi2",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    QuantumNumbers -> {Q},
    Mass -> MW,
    Indices -> {} },

S[4] == {
    ClassMembers :> Table[Symbol[StringJoin["S", ToString[k]]], {k, Nf}],
    SelfConjugate -> True,
    Indices -> {Index[SGen]},
    PropagatorLabel -> Sk,
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MSk }
}


(*        Definitions       *)

GaugeXi[ U[1] ] = GaugeXi[A];
GaugeXi[ U[2] ] = GaugeXi[Z];
GaugeXi[ U[31] ] = GaugeXi[W];
GaugeXi[ U[32] ] = GaugeXi[W];
GaugeXi[ U[4] ] = GaugeXi[G];
GaugeXi[ V[1] ] = GaugeXi[A];
GaugeXi[ V[2] ] = GaugeXi[Z];
GaugeXi[ V[3] ] = GaugeXi[W];
GaugeXi[ V[4] ] = GaugeXi[G];
GaugeXi[ S[1] ] = 1;
GaugeXi[ S[2] ] = GaugeXi[Z];
GaugeXi[ S[3] ] = GaugeXi[W];

Ml[ 1 ] := Me;
Ml[ 2 ] := MM;
Ml[ 3 ] := MTA;
Mu[ 1, _ ] := MU;
Mu[ 1 ] := MU;
Mu[ 2, _ ] := MC;
Mu[ 2 ] := MC;
Mu[ 3, _ ] := MT;
Mu[ 3 ] := MT;
Md[ 1, _ ] := MD;
Md[ 1 ] := MD;
Md[ 2, _ ] := MS;
Md[ 2 ] := MS;
Md[ 3, _ ] := MB;
Md[ 3 ] := MB;
MZ[ ___ ] := MZ;
MW[ ___ ] := MW;
MH[ ___ ] := MH;
MSk[ ___ ] := MSk;


TheLabel[ F[1, {1}] ] := "ve";
TheLabel[ F[1, {2}] ] := "vm";
TheLabel[ F[1, {3}] ] := "vt";
TheLabel[ F[2, {1}] ] := "e";
TheLabel[ F[2, {2}] ] := "m";
TheLabel[ F[2, {3}] ] := "tt";
TheLabel[ F[3, {1, _}] ] := "u";
TheLabel[ F[3, {1}] ] := "u";
TheLabel[ F[3, {2, _}] ] := "c";
TheLabel[ F[3, {2}] ] := "c";
TheLabel[ F[3, {3, _}] ] := "t";
TheLabel[ F[3, {3}] ] := "t";
TheLabel[ F[4, {1, _}] ] := "d";
TheLabel[ F[4, {1}] ] := "d";
TheLabel[ F[4, {2, _}] ] := "s";
TheLabel[ F[4, {2}] ] := "s";
TheLabel[ F[4, {3, _}] ] := "b";
TheLabel[ F[4, {3}] ] := "b";
TheLabel[ U[4, {__}] ] := TheLabel[U[4]];
TheLabel[ V[4, {__}] ] := TheLabel[V[4]];
TheLabel[ S[4, {1}] ] := "S1"
TheLabel[ S[4, {2}] ] := "S2"
TheLabel[ S[4, {3}] ] := "S3"
TheLabel[ S[4, {4}] ] := "S4"


(*      Couplings (calculated by FeynRules)      *)

M$CouplingMatrices = {

C[ S[1] , S[1] , S[1] , S[1] ] == {{(-6*I)*lam, 0}},

C[ S[1] , S[1] , S[2] , S[2] ] == {{(-2*I)*lam, 0}},

C[ S[2] , S[2] , S[2] , S[2] ] == {{(-6*I)*lam, 0}},

C[ S[1] , S[1] , S[3] , -S[3] ] == {{(-2*I)*lam, 0}},

C[ S[2] , S[2] , S[3] , -S[3] ] == {{(-2*I)*lam, 0}},

C[ S[3] , S[3] , -S[3] , -S[3] ] == {{(-4*I)*lam, 0}},

C[ S[1] , S[1] , S[1] ] == {{(-6*I)*lam*v, 0}},

C[ S[1] , S[2] , S[2] ] == {{(-2*I)*lam*v, 0}},

C[ S[1] , S[3] , -S[3] ] == {{(-2*I)*lam*v, 0}},

C[ S[3] , -S[3] , V[1] , V[1] ] == {{(2*I)*EL^2, 0}},

C[ S[3] , -S[3] , V[1] ] == {{(-I)*gc11, 0}, {I*gc11, 0}},

C[ -U[1] , U[32] , V[3] ] == {{I*gc12, 0}, {I*gc12, 0}, {0, 0}},

C[ -U[1] , U[31] , -V[3] ] == {{I*gc13, 0}, {I*gc13, 0}, {0, 0}},

C[ -S[3] , -U[32] , U[1] ] == {{EL*MW, 0}},

C[ -U[32] , U[1] , -V[3] ] == {{I*gc15, 0}, {I*gc15, 0}, {0, 0}},

C[ S[1] , -U[32] , U[32] ] == {{((-I/2)*EL*MW)/sw, 0}},

C[ S[2] , -U[32] , U[32] ] == {{-(EL*MW)/(2*sw), 0}},

C[ -U[32] , U[32] , V[1] ] == {{I*gc18, 0}, {I*gc18, 0}, {0, 0}},

C[ -U[32] , U[32] , V[2] ] == {{I*gc19, 0}, {I*gc19, 0}, {0, 0}},

C[ -S[3] , -U[32] , U[2] ] == {{(EL*MW*(cw - sw)*(cw + sw))/(2*cw*sw), 0}},

C[ -U[32] , U[2] , -V[3] ] == {{I*gc21, 0}, {I*gc21, 0}, {0, 0}},

C[ S[3] , -U[31] , U[1] ] == {{-(EL*MW), 0}},

C[ -U[31] , U[1] , V[3] ] == {{I*gc23, 0}, {I*gc23, 0}, {0, 0}},

C[ S[1] , -U[31] , U[31] ] == {{((-I/2)*EL*MW)/sw, 0}},

C[ S[2] , -U[31] , U[31] ] == {{(EL*MW)/(2*sw), 0}},

C[ -U[31] , U[31] , V[1] ] == {{I*gc26, 0}, {I*gc26, 0}, {0, 0}},

C[ -U[31] , U[31] , V[2] ] == {{I*gc27, 0}, {I*gc27, 0}, {0, 0}},

C[ S[3] , -U[31] , U[2] ] == {{-(EL*MW*(cw - sw)*(cw + sw))/(2*cw*sw), 0}},

C[ -U[31] , U[2] , V[3] ] == {{I*gc29, 0}, {I*gc29, 0}, {0, 0}},

C[ S[3] , -U[2] , U[32] ] == {{(EL*MZ)/(2*sw), 0}},

C[ -U[2] , U[32] , V[3] ] == {{I*gc31, 0}, {I*gc31, 0}, {0, 0}},

C[ -S[3] , -U[2] , U[31] ] == {{-(EL*MZ)/(2*sw), 0}},

C[ -U[2] , U[31] , -V[3] ] == {{I*gc33, 0}, {I*gc33, 0}, {0, 0}},

C[ S[1] , -U[2] , U[2] ] == {{((-I/2)*EL*MZ)/(cw*sw), 0}},

C[ -U[4, {e1x1}] , U[4, {e2x1}] , V[4, {e3x2}] ] == {{gc35*SUNF[e3x2, e1x1, e2x1], 0}, {gc35*SUNF[e3x2, e1x1, e2x1], 0}, {0, 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] ] == {{-(gc36*SUNF[e1x2, e2x2, e3x2]), 0}, {gc36*SUNF[e1x2, e2x2, e3x2], 0}, {gc36*SUNF[e1x2, e2x2, e3x2], 0}, {-(gc36*SUNF[e1x2, e2x2, e3x2]), 0}, {-(gc36*SUNF[e1x2, e2x2, e3x2]), 0}, {gc36*SUNF[e1x2, e2x2, e3x2], 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] ] == {{(-I)*gc37*(SUNF[e1x2, e2x2, e3x2, e4x2] + SUNF[e1x2, e3x2, e2x2, e4x2]), 0}, {I*gc37*(SUNF[e1x2, e2x2, e3x2, e4x2] - SUNF[e1x2, e4x2, e2x2, e3x2]), 0}, {I*gc37*(SUNF[e1x2, e3x2, e2x2, e4x2] + SUNF[e1x2, e4x2, e2x2, e3x2]), 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc38*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc38*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc39*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc39*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ S[1] , -S[3] , V[1] , V[3] ] == {{-EL^2/(2*sw), 0}},

C[ S[2] , -S[3] , V[1] , V[3] ] == {{((-I/2)*EL^2)/sw, 0}},

C[ -S[3] , V[1] , V[3] ] == {{-(EL^2*v)/(2*sw), 0}},

C[ S[1] , -S[3] , V[3] ] == {{-gc43, 0}, {gc43, 0}},

C[ S[2] , -S[3] , V[3] ] == {{(-I)*gc44, 0}, {I*gc44, 0}},

C[ V[1] , V[3] , -V[3] ] == {{(-I)*gc45, 0}, {I*gc45, 0}, {I*gc45, 0}, {(-I)*gc45, 0}, {(-I)*gc45, 0}, {I*gc45, 0}},

C[ S[1] , S[3] , V[1] , -V[3] ] == {{EL^2/(2*sw), 0}},

C[ S[2] , S[3] , V[1] , -V[3] ] == {{((-I/2)*EL^2)/sw, 0}},

C[ S[3] , V[1] , -V[3] ] == {{(EL^2*v)/(2*sw), 0}},

C[ S[1] , S[3] , -V[3] ] == {{-gc49, 0}, {gc49, 0}},

C[ S[2] , S[3] , -V[3] ] == {{(-I)*gc50, 0}, {I*gc50, 0}},

C[ S[1] , S[1] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[2] , S[2] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[3] , -S[3] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[1] , V[3] , -V[3] ] == {{((I/2)*EL^2*v)/sw^2, 0}},

C[ V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc55, 0}, {(-I)*gc55, 0}, {(2*I)*gc55, 0}},

C[ V[3] , -V[3] , V[2] ] == {{(-I)*gc56, 0}, {I*gc56, 0}, {I*gc56, 0}, {(-I)*gc56, 0}, {(-I)*gc56, 0}, {I*gc56, 0}},

C[ V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc57, 0}, {(-I)*gc57, 0}, {(2*I)*gc57, 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[3] ] == {{gc58L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc58R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , -S[3] ] == {{gc59L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc59R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] ] == {{I*gc60[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc60[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[2] ] == {{gc61L[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc61R[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[1] ] == {{I*gc62[e1x2]*IndexDelta[e1x2, e2x2], 0}, {I*gc62[e1x2]*IndexDelta[e1x2, e2x2], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[2] ] == {{gc63L[e1x2]*IndexDelta[e1x2, e2x2], 0}, {gc63R[e1x2]*IndexDelta[e1x2, e2x2], 0}},

C[ -F[1, {e1x2}] , F[2, {e2x2}] , S[3] ] == {{0, 0}, {gc64R[e1x2]*IndexDelta[e1x2, e2x2], 0}},

C[ -F[2, {e1x2}] , F[1, {e2x2}] , -S[3] ] == {{gc65[e1x2]*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] ] == {{I*gc66[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc66[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[2] ] == {{gc67L[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc67R[e1x2]*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ S[3] , -S[3] , V[1] , V[2] ] == {{(I*EL^2*(cw - sw)*(cw + sw))/(cw*sw), 0}},

C[ S[1] , S[2] , V[2] ] == {{-gc69, 0}, {gc69, 0}},

C[ S[3] , -S[3] , V[2] ] == {{(-I)*gc70, 0}, {I*gc70, 0}},

C[ S[1] , -S[3] , V[3] , V[2] ] == {{EL^2/(2*cw), 0}},

C[ S[2] , -S[3] , V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ -S[3] , V[3] , V[2] ] == {{(EL^2*v)/(2*cw), 0}},

C[ S[1] , S[3] , -V[3] , V[2] ] == {{-EL^2/(2*cw), 0}},

C[ S[2] , S[3] , -V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ S[3] , -V[3] , V[2] ] == {{-(EL^2*v)/(2*cw), 0}},

C[ V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc77, 0}, {I*gc77, 0}, {I*gc77, 0}},

C[ S[1] , S[1] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[2] , S[2] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[3] , -S[3] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw - sw)^2*(cw + sw)^2)/(cw^2*sw^2), 0}},

C[ S[1] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2*v)/(cw^2*sw^2), 0}},

C[ V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc82, 0}, {(-I)*gc82, 0}, {(2*I)*gc82, 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[1] ] == {{I*gc83*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc83*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[2] ] == {{I*gc84L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc84R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[1] ] == {{I*gc85*IndexDelta[e1x2, e2x2], 0}, {I*gc85*IndexDelta[e1x2, e2x2], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[2] ] == {{I*gc86L*IndexDelta[e1x2, e2x2], 0}, {I*gc86R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[1] ] == {{I*gc87*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc87*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[2] ] == {{I*gc88L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc88R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[1, {e1x2}] , F[1, {e2x2}] , V[2] ] == {{I*gc89*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[3] ] == {{I*gc90[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[1, {e1x2}] , F[2, {e2x2}] , V[3] ] == {{I*gc91*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[2, {e1x2}] , F[1, {e2x2}] , -V[3] ] == {{I*gc92*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , -V[3] ] == {{I*gc93[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ S[1] , S[1] , S[4, {e3x1}] , S[4, {e4x1}] ] == {{(-I/4)*om*IndexDelta[e3x1, e4x1], 0}},

C[ S[2] , S[2] , S[4, {e3x1}] , S[4, {e4x1}] ] == {{(-I/4)*om*IndexDelta[e3x1, e4x1], 0}},

C[ S[3] , -S[3] , S[4, {e3x1}] , S[4, {e4x1}] ] == {{(-I/4)*om*IndexDelta[e3x1, e4x1], 0}},

C[ S[1] , S[4, {e2x1}] , S[4, {e3x1}] ] == {{(-I/4)*om*v*IndexDelta[e2x1, e3x1], 0}},

C[ S[4, {e1x1}] , S[4, {e2x1}] , S[4, {e3x1}] , S[4, {e4x1}] ] == {{(-I/4)*lS*(IndexDelta[e1x1, e4x1]*IndexDelta[e2x1, e3x1] + IndexDelta[e1x1, e3x1]*IndexDelta[e2x1, e4x1] + IndexDelta[e1x1, e2x1]*IndexDelta[e3x1, e4x1]), 0}}

}

(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)

(* Parameter replacement lists (These lists were created by FeynRules) *)

(* FA Couplings *)

M$FACouplings = {
     gc11 -> -EL,
     gc12 -> EL,
     gc13 -> -EL,
     gc15 -> EL,
     gc18 -> -EL,
     gc19 -> -((cw*EL)/sw),
     gc21 -> (cw*EL)/sw,
     gc23 -> -EL,
     gc26 -> EL,
     gc27 -> (cw*EL)/sw,
     gc29 -> -((cw*EL)/sw),
     gc31 -> (cw*EL)/sw,
     gc33 -> -((cw*EL)/sw),
     gc35 -> GS,
     gc36 -> -GS,
     gc37 -> -GS^2,
     gc38 -> GS,
     gc39 -> GS,
     gc43 -> EL/(2*sw),
     gc44 -> EL/(2*sw),
     gc45 -> gw*sw,
     gc49 -> EL/(2*sw),
     gc50 -> -EL/(2*sw),
     gc55 -> -(gw^2*sw^2),
     gc56 -> cw*gw,
     gc57 -> gw^2,
     gc58L[e1x2_, e2x2_] -> CKM[e1x2, e2x2]*yu[e1x2],
     gc58R[e1x2_, e2x2_] -> -(CKM[e1x2, e2x2]*yd[e2x2]),
     gc59L[e1x2_, e2x2_] -> Conjugate[CKM[e2x2, e1x2]]*yd[e1x2],
     gc59R[e1x2_, e2x2_] -> -(Conjugate[CKM[e2x2, e1x2]]*yu[e2x2]),
     gc60[e1x2_] -> -(yd[e1x2]/Sqrt[2]),
     gc61L[e1x2_] -> -(yd[e1x2]/Sqrt[2]),
     gc61R[e1x2_] -> yd[e1x2]/Sqrt[2],
     gc62[e1x2_] -> -(yl[e1x2]/Sqrt[2]),
     gc63L[e1x2_] -> -(yl[e1x2]/Sqrt[2]),
     gc63R[e1x2_] -> yl[e1x2]/Sqrt[2],
     gc64R[e1x2_] -> -yl[e1x2],
     gc65[e1x2_] -> yl[e1x2],
     gc66[e1x2_] -> -(yu[e1x2]/Sqrt[2]),
     gc67L[e1x2_] -> yu[e1x2]/Sqrt[2],
     gc67R[e1x2_] -> -(yu[e1x2]/Sqrt[2]),
     gc69 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc70 -> -(cw*EL)/(2*sw) + (EL*sw)/(2*cw),
     gc77 -> cw*gw^2*sw,
     gc82 -> -(cw^2*gw^2),
     gc83 -> -EL/3,
     gc84L -> -(EL*(3*cw^2 + sw^2))/(6*cw*sw),
     gc84R -> (EL*sw)/(3*cw),
     gc85 -> -EL,
     gc86L -> -(EL*(cw^2 - sw^2))/(2*cw*sw),
     gc86R -> (EL*sw)/cw,
     gc87 -> (2*EL)/3,
     gc88L -> (cw*EL)/(2*sw) - (EL*sw)/(6*cw),
     gc88R -> (-2*EL*sw)/(3*cw),
     gc89 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc90[e1x2_, e2x2_] -> (EL*CKM[e1x2, e2x2])/(Sqrt[2]*sw),
     gc91 -> EL/(Sqrt[2]*sw),
     gc92 -> EL/(Sqrt[2]*sw),
     gc93[e1x2_, e2x2_] -> (EL*Conjugate[CKM[e2x2, e1x2]])/(Sqrt[2]*sw)};

