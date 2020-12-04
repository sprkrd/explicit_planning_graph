(define (problem p0)
  (:domain IMAGINE)
  (:objects
    pcb lid actuator screw0 screw1 screw2 - struct
    top bottom - side
    screwdriver-flat screwdriver-torx8 suction-pad none - tool
  )
  (:init
   (removable pcb)
   (removable lid)
   (removable actuator)
   (removable screw0)
   (removable screw1)
   (removable screw2)
   
   (precedes pcb screw2)
   (precedes lid actuator)
   (precedes screw0 pcb)
   (precedes screw1 lid)
   (precedes screw2 actuator)

   (reachable pcb bottom)
   (reachable lid top)
   (reachable actuator top)
   (reachable screw0 bottom)
   (reachable screw1 top)
   (reachable screw2 bottom)

   (current-side top)
   (current-tool none)

   (usable-tool screwdriver-flat pcb)
   (usable-tool suction-pad pcb)
   (usable-tool screwdriver-flat lid)
   (usable-tool suction-pad lid)
   (usable-tool screwdriver-flat actuator)
   (usable-tool screwdriver-torx8 screw0)
   (usable-tool screwdriver-torx8 screw1)
   (usable-tool screwdriver-torx8 screw2)

   (= (total-cost) 0)

   (= (remove-cost screwdriver-flat pcb) 1)
   (= (remove-cost suction-pad pcb) 4)
   (= (remove-cost screwdriver-flat lid) 4)
   (= (remove-cost suction-pad lid) 1)
   (= (remove-cost screwdriver-flat actuator) 2)
   (= (remove-cost screwdriver-torx8 screw0) 1)
   (= (remove-cost screwdriver-torx8 screw1) 1)
   (= (remove-cost screwdriver-torx8 screw2) 1)

   (= (flip-cost) 1)
   (= (switch-tool-cost) 1)
  )
  (:goal (and (removed pcb) (removed lid) (removed actuator)))
  ;(:goal (and (removed screw0)))
  ;(:goal (and (current-tool screwdriver-flat)))
  (:metric minimize (total-cost))
)
