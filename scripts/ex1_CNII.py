"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHostS1 = self.addHost( 'h1' )
        rightHostS1 = self.addHost( 'h2' )
        leftHostS2 = self.addHost( 'h3' )
        rightHostS2 = self.addHost( 'h4' )
        leftHostS3 = self.addHost( 'h5' )
        rightHostS3 = self.addHost( 'h6' )
        leftSwitch = self.addSwitch( 's1' )
        middleSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Options

        linkopts = dict(bw=5) # bw is expressed as a number in Mbit / Add "--link=tc" option to enable it

        # Add links

        self.addLink( leftSwitch, middleSwitch, **linkopts )
        self.addLink( middleSwitch, rightSwitch, **linkopts )
        self.addLink( leftHostS1, leftSwitch, **linkopts )
        self.addLink( rightHostS1, leftSwitch, **linkopts )
        self.addLink( leftHostS2, middleSwitch, **linkopts )
        self.addLink( rightHostS2, middleSwitch, **linkopts )
        self.addLink( leftHostS3, rightSwitch, **linkopts )
        self.addLink( rightHostS3, rightSwitch, **linkopts )


topos = { 'mytopo': ( lambda: MyTopo() ) }
