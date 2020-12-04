(define (domain IMAGINE)
(:requirements :adl :equality :action-costs)
(:types struct side tool - object)
(:predicates (precedes ?x ?y - struct)
             (reachable ?x - struct ?y - side)
             (removable ?x - struct)
             (removed ?x - struct)
             (current-side ?x - side)
             (current-tool ?x - tool)
             (usable-tool ?x - tool ?y - struct)
)
(:functions
  (total-cost)
  (remove-cost ?tool - tool ?x - struct)
  (flip-cost)
  (switch-tool-cost)
)

(:action remove
 :parameters (?what - struct ?where - side ?tool - tool)
 :precondition (and
  (removable ?what)
  (not (removed ?what))
  (forall (?other - struct) (not (precedes ?other ?what)))
  (reachable ?what ?where)
  (current-side ?where)
  (current-tool ?tool)
  (usable-tool ?tool ?what)
 )
 :effect (and
  (removed ?what)
  (forall (?other - struct) (not (precedes ?what ?other)))
  (increase (total-cost) (remove-cost ?tool ?what)))
)

(:action flip
 :parameters (?current-side ?desired-side - side)
 :precondition (and
  (not (= ?current-side ?desired-side))
  (current-side ?current-side)
 )
 :effect (and
  (not (current-side ?current-side))
  (current-side ?desired-side)
  (increase (total-cost) (flip-cost)))
)

(:action switch-tool
 :parameters (?current-tool ?desired-tool - tool)
 :precondition (and
  (not (= ?current-tool ?desired-tool))
  (current-tool ?current-tool)
 )
 :effect (and
  (not (current-tool ?current-tool))
  (current-tool ?desired-tool)
  (increase (total-cost) (switch-tool-cost)))
)

)


