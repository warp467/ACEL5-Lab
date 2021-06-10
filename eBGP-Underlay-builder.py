#from cvplibrary import CVPGlobalVariables, GlobalVariableNames 
import yaml
#hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)

config = """
leaf1-DC1:
  interfaces:
    loopback0:
      ipv4: 192.168.101.11
      mask: 32
    loopback1:
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.0
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.2
      mask: 31
    Ethernet5:
      ipv4: 192.168.103.4
      mask: 31
  spine-peers:
    - 192.168.203.25
    - 192.168.203.27
    - 192.168.203.29
leaf2-DC1:
  interfaces:
    loopback0:
      ipv4: 192.168.101.12
      mask: 32
    loopback1:
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.6
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.8
      mask: 31
    Ethernet5:
      ipv4: 192.168.103.10
      mask: 31
  spine-peers:
    - 192.168.203.25
    - 192.168.203.27
    - 192.168.203.29
"""
switches = yaml.load(config)
hostname = "leaf1-DC1"
switch = "leaf1-DC1"

print (switches[switch]['spine-peers'])

for x in switches[switch]['spine-peers']:
  print (x)

for iface in switches[hostname]['interfaces']:
  #print("interface %s") %iface
  ip = switches[hostname]['interfaces'][iface]['ipv4']
  mask = switches[hostname]['interfaces'][iface]['mask']
  #print ("  ip address %s/%s") %(ip,mask)
  if "thernet" in iface:
    print ("  no switchport")
    
#print(switches['leaf1-DC1']['interfaces']['loopback0']['ipv4'])