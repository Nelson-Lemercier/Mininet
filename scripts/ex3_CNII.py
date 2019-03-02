#!/usr/bin/python

"""
This example creates a multi-controller network from semi-scratch by
using the net.add*() API and manually starting the switches and controllers.

This is the "mid-level" API, which is an alternative to the "high-level"
Topo() API which supports parametrized topology classes.

Note that one could also create a custom switch class and pass it into
the Mininet() constructor.
"""


from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def multiControllerNet():
    "Create a network from semi-scratch with multiple controllers."

    net = Mininet( controller=Controller, switch=OVSSwitch )

    info( "*** Creating (reference) controllers\n" )
    c1 = net.addController( 'c1', port=6633 )

    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )

    info( "*** Creating hosts\n" )
    
    Host1 = net.addHost( 'Host1' )
    Host2 = net.addHost( 'Host2' )
    Host3 = net.addHost( 'Host3' )
    Host4 = net.addHost( 'Host4' )

    info( "*** Creating links\n" )
    
    net.addLink( Host1, s1 )
    net.addLink( s1, s2 )
    net.addLink( s2, s3 )
    net.addLink( s3, Host3 )
    net.addLink( Host2, s2 )
    net.addLink( Host4, s3 )
    net.addLink( s1, s4 )
    net.addLink( s4, s2 )

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    s2.start( [ c1 ] )
    s3.start( [ c1 ] )
    s4.start( [ c1 ] )

    #info( "*** Testing network\n" )
    #net.pingAll()

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
