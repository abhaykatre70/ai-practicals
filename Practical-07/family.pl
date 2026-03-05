% --- FACTS ---
% parent(Parent, Child)
parent(rajesh, priya).
parent(rajesh, arjun).
parent(priya, ananya).
parent(arjun, vivaan).

% Gender facts
male(rajesh).
male(arjun).
male(vivaan).

female(priya).
female(ananya).

% --- RULES ---

% father(X, Y) :- X is the father of Y
father(X, Y) :-
    parent(X, Y),
    male(X).

% mother(X, Y) :- X is the mother of Y
mother(X, Y) :-
    parent(X, Y),
    female(X).

% sibling(X, Y) :- X and Y share the same parent (and are different persons)
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% grandparent(X, Y) :- X is the grandparent of Y
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% grandfather(X, Y) :- X is the grandfather of Y
grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

% grandmother(X, Y) :- X is the grandmother of Y
grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

% ancestor(X, Y) :- X is an ancestor of Y  (recursive)
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% ============================================================
% SAMPLE QUERIES TO TRY IN SWI-PROLOG:
%
%  ?- father(rajesh, arjun).          % Is rajesh the father of arjun?
%  ?- mother(X, ananya).              % Who is ananya's mother?
%  ?- sibling(priya, arjun).          % Are priya and arjun siblings?
%  ?- grandparent(rajesh, vivaan).    % Is rajesh a grandparent of vivaan?
%  ?- ancestor(rajesh, ananya).       % Is rajesh an ancestor of ananya?
%  ?- ancestor(rajesh, X).            % List all descendants of rajesh.
% ============================================================
