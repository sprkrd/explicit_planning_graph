(define (domain hanoi)
  (:requirements :strips :action-costs :equality)
  (:types disc peg - object)
  (:predicates
    (clear ?x - object)
    (on ?x - disc ?y - object)
    (smaller ?x - object ?y - disc)
    (base-peg ?x - object ?y - peg)
  )
  (:functions
    (total-cost)
    (move-cost ?peg-src ?peg-dst - peg)
  )

  (:action move
    :parameters (?disc - disc ?from - object ?base-from - peg ?to - object ?base-to - peg)
    :precondition (and (not (= ?base-from ?base-to)) (smaller ?to ?disc) (on ?disc ?from)
               (clear ?disc) (clear ?to) (base-peg ?disc ?base-from) (base-peg ?to ?base-to))
    :effect  (and
      (clear ?from)
      (on ?disc ?to)
      (base-peg ?disc ?base-to)
      (not (on ?disc ?from))
      (not (clear ?to))
      (not (base-peg ?disc ?base-from))
      (increase (total-cost) (move-cost ?base-from ?base-to))
  ))

)

