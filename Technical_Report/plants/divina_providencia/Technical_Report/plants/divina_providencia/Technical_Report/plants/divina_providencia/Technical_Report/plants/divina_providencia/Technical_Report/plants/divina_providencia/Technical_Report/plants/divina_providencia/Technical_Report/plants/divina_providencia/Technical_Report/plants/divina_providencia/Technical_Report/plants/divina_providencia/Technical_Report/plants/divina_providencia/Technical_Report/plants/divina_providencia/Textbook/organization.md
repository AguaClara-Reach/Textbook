## "Constants"
- 6 filter layers
- 75 cm of head max + signal for backwash (diff for plantita/ostars)
- sand layers are 20 cm (except for estars for plantita, then 15cm)
- branch spacing is 1/2 sand layer height
- max orifice size is 1/4"
- possible orifice sizes are 1/16, 1/8, 3/16, 1/4 inch
- drains must be large enough so they flow can exit with 10cm head
- head loss in orifices <5 cm (from dec-18 comments)
- head loss in sand is 1.2 m (because of the depth of the sand)

## Inputs
- plant flow

## Outputs
- number of filters --> amt of materials
- sizes of filters (this is a complex output) (most generally, an output could look like: 3 2ft estars)

## Conditions that must be met + things that are true
- inlet/outlet pipes must touch the floor
- for now the exits are slotted pipes
- inlets have wings
- branches go through trunks (thus trunk area matters so the branches don't act like valves)
- entrance tank contains: settled water inlet, four filter inlet pipes, overflow pipe, drain pipe (can overflow go back to clarifier?)
- exit tank contains: plant exits, three filter outlets, drain
- even flow across all branches
- even flow in all trunks
- even flow between filters
- air vent on filter body
- sand drain on filter body (only open if you want a big mess!)
- max flow is the backwash flow is the design flow is the flow a size if set for! 

## Need algorithms that:
- take in flow and return number/size (the big one)
    - plant flow --> \[array of pipe diameters] --> \[Q_filter for one filter of each diameter] --> \[Qplant/QFi (N_filt)]
    - then select the lowest number greater than 2 to the the number of filters chosen of a diameter 
    - this is the same algorithm that the tubes in the chemical dosing system use
    - diameters: (1, 1.5, 2, 3); flows: (.764, 1.608, 3.07, 7.024)
    - determine if we use 1.5 ft!
- take in size of filter and output dimensions for all components
  - diameters for all pipes
  - spacing of components
  - entrance and exit tank sizes
  - orifice conditions (number, diameter, spacing)
    - N_orifice*A_orifice = A_orificetotal
    - Q_filter/A_orificetotal = V_orifice **this is what needs to be limited to keep orifice headloss small!**
    - maximum orifice size is 1/4" 
    - should spacing be half the distance of the branch spacing to keep the relative spacing even between "level"; 5cm?
    - number of orifices depends on length of branches which is totally from geometry --> (slightly fewer orifices on BW level)
    - maximum orifice velocity comes from the ratio of the PR to the HL_sand
  - lengths for pipes (trunks, branches, heights of tanks, inlet + outlet piping)
  - amt of pipe for inlet wings
  - number of branches f(velocity) 


# Variables

*Requires a "decision" that is external to physical parameters to resolve*

**is not based on other variables/constants that are based on "true", fabrication variables**

\[Is an array of values]
 
|Names| Depends on/ constant value of|
|-----|-----------|
|Q_{Plant}| - |
|N_{SandLayeres}|6|
|H_{SandLayers}| 20cm|
| V_{BW}| 9.8mm/s|
|H_{SafetyEntranceTank}| **5cm**|
|HL_{WeirEntrance}| **3cm**|
|H_{overflowWater}| **10cm**|
|ND_{BallValve}	 |	3 in	| 
|ND_{BedTester}	| 	0.5in	 |
|ND_{BedTesterOuter}|	 	1in	 |
|ND_{FiAirRelValve}	 |	0.5in	 |
|ND_{FiBwTrunkMin}	 |	3in	 |
|ND_{FiBwBranchkMin}|	 	1in	 |
|ND_{FiTrunkMin}	 |	2in	 |
|ND_{FiDrainExit}	 |	3in	 |
|ND_{FiOverflowEnt}	 |	3in	 |
|ND_{FiBranchMin}	 |	1in |
|HL_{Sand}|120cm (HL_{SandLayer}|
|D_{filter}| *Q_{Plant}, N_{Filter}*|
|N_Filter| *Q_{plant}, D_{filter}*|
|S_{Branch}|H_{SandLayer}|
|S_{Orifice}|S_{Branch}?|
|Pi_{expansion}|1.3 (V_{BW})|
|H_{SafetyFilterBody}| 20cm |
|H_{FilterBody}|H_{SafetyFilterBody}, H{SandLayer}, N_{SandLayer}, Pi_{Expansion}|
|N_{Branches| S_{Branch}, D_{Filter}|
|V_{orificeMax}|   Pi_{man}, HL_{SandLayer}   |
| V_{orificeBW} | Q_{Filter}, HL_{AllowableBWOrifice}|
| \[L_{Branches}] |   D_{filter} , D_{Trunk}   |
| \[L_{BranchesBW}] |   D_{Filter}, D_{BWTrunk}   |
|A_{orifice}  | D_{orifice}     |
|N_{Branches}  |  D_{filter}, S_{branches}, (D_{Trunk}/D_{BWtrunk)?    |
|L_Trunk  |  D_{Filter}    |
|L_{BWTrunk)   |  D_{Filter}    |
|N_{orifices}  | S_{orifices}, L_{branchtotal}     |
|  D_{overflow}   |   H_{OverflowWater}, Q_{filt} |
|  D_{drain}   |   H_{OverflowWater}, Q_{filt} |
|   D_{settledWater}  | Q_{filter}?     |
|  D_{filterexit}   |  Q_{filter}?    |
|  \[L_{inlets}] |    H_{sandLayers}, H_{entranceTank}, D_{entranceTank}  |
|  \[L_{outlets}] |     H_{sandLayers}, H_{exitTank}, D_{exitTank}   |
|   D_{trunk} |      |
|   D_{BWTrunk}  |      |
|    D_{Branch} |      |
|   D_{InletBox}  |      |
|   D_{ExitBox}  |      |
|   A_{orificeTotal}  |      |
| D_{orifice}| |
| H_{ExitTank} | |
| H_{entranceTank} | |

