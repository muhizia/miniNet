#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, RemoteController, Node
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo(Topo):
    "Linear topology of k switches, with one host per switch."
    def __init__(self, k=2, **opts):
        """Init.
        k: number of switches (and hosts)
        hconf: host configuration options
        lconf: link configuration options"""
        super(LinearTopo, self).__init__(**opts)
        # self.k = k
        # lastSwitch = None
        h1 = self.addHost( 'h1', ip='0.0.0.0' )
        h2 = self.addHost( 'h2', ip='0.0.0.0' )
        h3 = self.addHost( 'h3', ip='0.0.0.0' )
        h4 = self.addHost( 'h4', ip='0.0.0.0' )
        h5 = self.addHost( 'h5', ip='0.0.0.0' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s2, bw=10, delay='5ms', loss=0, max_queue_size=1000, use_htb=True)
        self.addLink( h4, s3 )
        self.addLink( h5, s3 )
        
        # for i in irange(1, k):
        #     host =self.addHost('h%s' %i, cpu=.5/k)
        #     switch =self.addSwitch('s%s' %i)
        #     # 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
        #     self.addLink( host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
        #     if lastSwitch:
        #         self.addLink(switch, lastSwitch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
        #     lastSwitch = switch
def perfTest():
    "Create network and run simple performance test"
    CONTROLLER_IP='10.0.0.1'
    topo = LinearTopo(k=4)
    net =Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.addController( 'c0', controller=RemoteController, ip=CONTROLLER_IP, port=6633)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    perfTest()