from mininet.topo import Topo

class TopoQ3( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        SwitchA = self.addSwitch( 's1' )
        SwitchB = self.addSwitch( 's2' )
        SwitchC = self.addSwitch( 's3' )
        SwitchD = self.addSwitch( 's4' )
        Host1 = self.addHost( 'Host1' )
        Host2 = self.addHost( 'Host2' )
        Host3 = self.addHost( 'Host3' )
        Host4 = self.addHost( 'Host4' )

        # Add links

        self.addLink( Host1, SwitchA )
        self.addLink( SwitchA, SwitchB )
        self.addLink( SwitchB, SwitchC )
        self.addLink( SwitchC, Host3 )
        self.addLink( Host2, SwitchB )
        self.addLink( Host4, SwitchC )
        self.addLink( SwitchA, SwitchD )
        self.addLink( SwitchD, SwitchB )


topos = { 'topoq3': ( lambda: TopoQ3() ) }