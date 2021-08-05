# fog_edge

# Running without OAI
Run code of master branch
1) Clone the repository in a folder
2) Open the folder in PyCharm
3) Run Fog/fog_server.py
4) Run Proxy/vUser.py
5) Run Edge/visited_mme.py
6) Finally, run UE/ue.py and UE gets authenticated.

# Running with OAI
Run code of oai_phase

 OAI Core network can be found here : https://github.com/OPENAIRINTERFACE/openair-epc-fed/tree/2021.w06 
 I have used the 2021.w06 tag of master branch. To install, follow instructions from this page :
 https://github.com/OPENAIRINTERFACE/openair-epc-fed/blob/2021.w06/docs/DEPLOY_HOME.md
    
 OAI RAN (for eNB and UE ) can be found here: https://gitlab.eurecom.fr/oai/openairinterface5g
 To install and run, see "Where to start" Section of this link. 
 
1) Clone this repository from oai_phase branch.
2) Open the cloned folder in PyCharm
3) Run Fog/fog_server.py
4) Run Proxy/vUser.py
5) Start OAI and connect a OAI UE. Then, Fog generates auth vector 
    
