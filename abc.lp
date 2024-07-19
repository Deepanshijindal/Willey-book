\ Model Office Relocation
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.5 factory_depot_quantities[Liverpool,Newcastle]
   + 0.5 factory_depot_quantities[Liverpool,Birmingham]
   + factory_depot_quantities[Liverpool,London]
   + 0.2 factory_depot_quantities[Liverpool,Exeter]
   + 0.3 factory_depot_quantities[Brighton,Birmingham]
   + 0.5 factory_depot_quantities[Brighton,London]
   + 0.2 factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Liverpool,C1]
   + 1.5 factory_customer_quantities[Liverpool,C3]
   + 2 factory_customer_quantities[Liverpool,C4]
   + factory_customer_quantities[Liverpool,C6]
   + 2 factory_customer_quantities[Brighton,C1]
   + 1.5 depot_customer_quantities[Newcastle,C2]
   + 0.5 depot_customer_quantities[Newcastle,C3]
   + 1.5 depot_customer_quantities[Newcastle,C4]
   + depot_customer_quantities[Newcastle,C6]
   + depot_customer_quantities[Birmingham,C1]
   + 0.5 depot_customer_quantities[Birmingham,C2]
   + 0.5 depot_customer_quantities[Birmingham,C3]
   + depot_customer_quantities[Birmingham,C4]
   + 0.5 depot_customer_quantities[Birmingham,C5]
   + 1.5 depot_customer_quantities[London,C2]
   + 2 depot_customer_quantities[London,C3]
   + 0.5 depot_customer_quantities[London,C5]
   + 1.5 depot_customer_quantities[London,C6]
   + 0.2 depot_customer_quantities[Exeter,C3]
   + 1.5 depot_customer_quantities[Exeter,C4]
   + 0.5 depot_customer_quantities[Exeter,C5]
   + 1.5 depot_customer_quantities[Exeter,C6]
Subject To
 R0: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C1] <= 150000
 R1: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C2] <= 150000
 R2: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C3] <= 150000
 R3: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C4] <= 150000
 R4: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C5] <= 150000
 R5: factory_depot_quantities[Liverpool,Newcastle]
   + factory_customer_quantities[Liverpool,C6] <= 150000
 R6: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C1] <= 200000
 R7: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C2] <= 200000
 R8: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C3] <= 200000
 R9: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C4] <= 200000
 R10: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C5] <= 200000
 R11: factory_depot_quantities[Brighton,Newcastle]
   + factory_customer_quantities[Brighton,C6] <= 200000
 R12: factory_depot_quantities[Liverpool,Newcastle]
   + factory_depot_quantities[Brighton,Newcastle] <= 70000
 R13: - factory_depot_quantities[Liverpool,Newcastle]
   - factory_depot_quantities[Brighton,Newcastle]
   + depot_customer_quantities[Newcastle,C1]
   + depot_customer_quantities[Newcastle,C2]
   + depot_customer_quantities[Newcastle,C3]
   + depot_customer_quantities[Newcastle,C4]
   + depot_customer_quantities[Newcastle,C5]
   + depot_customer_quantities[Newcastle,C6] <= 0
 R14: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C1] <= 150000
 R15: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C2] <= 150000
 R16: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C3] <= 150000
 R17: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C4] <= 150000
 R18: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C5] <= 150000
 R19: factory_depot_quantities[Liverpool,Birmingham]
   + factory_customer_quantities[Liverpool,C6] <= 150000
 R20: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C1] <= 200000
 R21: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C2] <= 200000
 R22: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C3] <= 200000
 R23: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C4] <= 200000
 R24: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C5] <= 200000
 R25: factory_depot_quantities[Brighton,Birmingham]
   + factory_customer_quantities[Brighton,C6] <= 200000
 R26: factory_depot_quantities[Liverpool,Birmingham]
   + factory_depot_quantities[Brighton,Birmingham] <= 50000
 R27: - factory_depot_quantities[Liverpool,Birmingham]
   - factory_depot_quantities[Brighton,Birmingham]
   + depot_customer_quantities[Birmingham,C1]
   + depot_customer_quantities[Birmingham,C2]
   + depot_customer_quantities[Birmingham,C3]
   + depot_customer_quantities[Birmingham,C4]
   + depot_customer_quantities[Birmingham,C5]
   + depot_customer_quantities[Birmingham,C6] <= 0
 R28: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C1] <= 150000
 R29: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C2] <= 150000
 R30: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C3] <= 150000
 R31: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C4] <= 150000
 R32: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C5] <= 150000
 R33: factory_depot_quantities[Liverpool,London]
   + factory_customer_quantities[Liverpool,C6] <= 150000
 R34: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C1] <= 200000
 R35: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C2] <= 200000
 R36: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C3] <= 200000
 R37: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C4] <= 200000
 R38: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C5] <= 200000
 R39: factory_depot_quantities[Brighton,London]
   + factory_customer_quantities[Brighton,C6] <= 200000
 R40: factory_depot_quantities[Liverpool,London]
   + factory_depot_quantities[Brighton,London] <= 100000
 R41: - factory_depot_quantities[Liverpool,London]
   - factory_depot_quantities[Brighton,London]
   + depot_customer_quantities[London,C1]
   + depot_customer_quantities[London,C2]
   + depot_customer_quantities[London,C3]
   + depot_customer_quantities[London,C4]
   + depot_customer_quantities[London,C5]
   + depot_customer_quantities[London,C6] <= 0
 R42: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C1] <= 150000
 R43: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C2] <= 150000
 R44: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C3] <= 150000
 R45: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C4] <= 150000
 R46: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C5] <= 150000
 R47: factory_depot_quantities[Liverpool,Exeter]
   + factory_customer_quantities[Liverpool,C6] <= 150000
 R48: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C1] <= 200000
 R49: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C2] <= 200000
 R50: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C3] <= 200000
 R51: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C4] <= 200000
 R52: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C5] <= 200000
 R53: factory_depot_quantities[Brighton,Exeter]
   + factory_customer_quantities[Brighton,C6] <= 200000
 R54: factory_depot_quantities[Liverpool,Exeter]
   + factory_depot_quantities[Brighton,Exeter] <= 40000
 R55: - factory_depot_quantities[Liverpool,Exeter]
   - factory_depot_quantities[Brighton,Exeter]
   + depot_customer_quantities[Exeter,C1]
   + depot_customer_quantities[Exeter,C2]
   + depot_customer_quantities[Exeter,C3]
   + depot_customer_quantities[Exeter,C4]
   + depot_customer_quantities[Exeter,C5]
   + depot_customer_quantities[Exeter,C6] <= 0
 R56: factory_customer_quantities[Liverpool,C1]
   + factory_customer_quantities[Brighton,C1]
   + depot_customer_quantities[Newcastle,C1]
   + depot_customer_quantities[Birmingham,C1]
   + depot_customer_quantities[London,C1]
   + depot_customer_quantities[Exeter,C1] >= 50000
 R57: 0.5 factory_customer_quantities[Liverpool,C1]
   - 0.5 factory_customer_quantities[Brighton,C1]
   - 0.5 depot_customer_quantities[Newcastle,C1]
   - 0.5 depot_customer_quantities[Birmingham,C1]
   - 0.5 depot_customer_quantities[London,C1]
   - 0.5 depot_customer_quantities[Exeter,C1] >= 0
 R58: factory_customer_quantities[Liverpool,C2]
   + factory_customer_quantities[Brighton,C2]
   + depot_customer_quantities[Newcastle,C2]
   + depot_customer_quantities[Birmingham,C2]
   + depot_customer_quantities[London,C2]
   + depot_customer_quantities[Exeter,C2] >= 10000
 R59: - 0.5 factory_customer_quantities[Liverpool,C2]
   - 0.5 factory_customer_quantities[Brighton,C2]
   + 0.5 depot_customer_quantities[Newcastle,C2]
   - 0.5 depot_customer_quantities[Birmingham,C2]
   - 0.5 depot_customer_quantities[London,C2]
   - 0.5 depot_customer_quantities[Exeter,C2] >= 0
 R60: factory_customer_quantities[Liverpool,C3]
   + factory_customer_quantities[Brighton,C3]
   + depot_customer_quantities[Newcastle,C3]
   + depot_customer_quantities[Birmingham,C3]
   + depot_customer_quantities[London,C3]
   + depot_customer_quantities[Exeter,C3] >= 40000
 R61: - 0.5 factory_customer_quantities[Liverpool,C2]
   - 0.5 factory_customer_quantities[Brighton,C2]
   - 0.5 depot_customer_quantities[Newcastle,C2]
   + depot_customer_quantities[Newcastle,C3]
   - 0.5 depot_customer_quantities[Birmingham,C2]
   - 0.5 depot_customer_quantities[London,C2]
   - 0.5 depot_customer_quantities[Exeter,C2] >= 0
 R62: factory_customer_quantities[Liverpool,C4]
   + factory_customer_quantities[Brighton,C4]
   + depot_customer_quantities[Newcastle,C4]
   + depot_customer_quantities[Birmingham,C4]
   + depot_customer_quantities[London,C4]
   + depot_customer_quantities[Exeter,C4] >= 35000
 R63: - 0.5 factory_customer_quantities[Liverpool,C2]
   - 0.5 factory_customer_quantities[Brighton,C2]
   - 0.5 depot_customer_quantities[Newcastle,C2]
   + depot_customer_quantities[Newcastle,C4]
   - 0.5 depot_customer_quantities[Birmingham,C2]
   - 0.5 depot_customer_quantities[London,C2]
   - 0.5 depot_customer_quantities[Exeter,C2] >= 0
 R64: factory_customer_quantities[Liverpool,C5]
   + factory_customer_quantities[Brighton,C5]
   + depot_customer_quantities[Newcastle,C5]
   + depot_customer_quantities[Birmingham,C5]
   + depot_customer_quantities[London,C5]
   + depot_customer_quantities[Exeter,C5] >= 60000
 R65: - 0.5 factory_customer_quantities[Liverpool,C5]
   - 0.5 factory_customer_quantities[Brighton,C5]
   - 0.5 depot_customer_quantities[Newcastle,C5]
   + 0.5 depot_customer_quantities[Birmingham,C5]
   - 0.5 depot_customer_quantities[London,C5]
   - 0.5 depot_customer_quantities[Exeter,C5] >= 0
 R66: factory_customer_quantities[Liverpool,C6]
   + factory_customer_quantities[Brighton,C6]
   + depot_customer_quantities[Newcastle,C6]
   + depot_customer_quantities[Birmingham,C6]
   + depot_customer_quantities[London,C6]
   + depot_customer_quantities[Exeter,C6] >= 20000
 R67: - 0.5 factory_customer_quantities[Liverpool,C6]
   - 0.5 factory_customer_quantities[Brighton,C6]
   - 0.5 depot_customer_quantities[Newcastle,C6]
   - 0.5 depot_customer_quantities[Birmingham,C6]
   + 0.5 depot_customer_quantities[London,C6]
   + 0.5 depot_customer_quantities[Exeter,C6] >= 0
Bounds
 factory_depot_quantities[Brighton,Newcastle] = 0
 factory_customer_quantities[Liverpool,C2] = 0
 factory_customer_quantities[Liverpool,C5] = 0
 factory_customer_quantities[Brighton,C2] = 0
 factory_customer_quantities[Brighton,C3] = 0
 factory_customer_quantities[Brighton,C4] = 0
 factory_customer_quantities[Brighton,C5] = 0
 factory_customer_quantities[Brighton,C6] = 0
 depot_customer_quantities[Newcastle,C1] = 0
 depot_customer_quantities[Newcastle,C5] = 0
 depot_customer_quantities[Birmingham,C6] = 0
 depot_customer_quantities[London,C1] = 0
 depot_customer_quantities[London,C4] = 0
 depot_customer_quantities[Exeter,C1] = 0
 depot_customer_quantities[Exeter,C2] = 0
End
