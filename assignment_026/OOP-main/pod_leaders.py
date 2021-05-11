'''
################################################
#  Program: Pod_leaders.py                     #
#  Author: Jacore Baptiste                               #
#  Date: 2/17/2021                             #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

class Pod_leaders:
  
    # Class Constructor method is called when an Object is instantiated
    def __init__(self):
       self.pod_leader = {}

    # Class method to add a leader to the pod_leader dictionary       
    def add_leader(self, leader_to_add,cell_number):
        self.pod_leader[leader_to_add] = cell_number
        
    # Class method to print the pod_leader and cell numbers   
    def display_leaders(self):
      print('POD Leaders')      
      for leader, number in self.pod_leader.items():
        print(leader, number)
            
pod = Pod_leaders()
pod.add_leader("Richard","(510) 228-5623")
pod.add_leader("Jacore","(845) 200-6250")
pod.add_leader("Gabriel","(510) 326-5834")
pod.add_leader("Aris","(510) 229-6359 ")
pod.add_leader("Andrew","(925) 727-4611")
pod.display_leaders()


