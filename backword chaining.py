% Define facts and rules
bird(tweety).
bird(penguin).
flies(X) :- bird(X), not(penguin(X)).

% Query predicate for backward chaining
can_fly(X) :- flies(X), write(X), write(' can fly.').

% Backward chaining algorithm
backward_chain(Goal) :- Goal, !.
backward_chain(Goal) :- rule(Goal, Premise), backward_chain(Premise).

% Rules to support backward chaining
rule(flies(X), bird(X)).

% Query the goal
:- backward_chain(can_fly(tweety)).
