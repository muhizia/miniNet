#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf
def aggNet():
    CONTROLLER_IP='10.0.0.1'
    net = Mininet( topo=None, build=False)
    net.addController( 'c0', controller=RemoteController, ip=CONTROLLER_IP, port=6633)
    h1 = net.addHost( 'h1', ip='0.0.0.0' )
    h2 = net.addHost( 'h2', ip='0.0.0.0' )
    h3 = net.addHost( 'h3', ip='0.0.0.0' )
    h4 = net.addHost( 'h4', ip='0.0.0.0' )
    h5 = net.addHost( 'h5', ip='0.0.0.0' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    net.addLink( s1, s2 )
    net.addLink( s2, s3 )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )
    net.addLink( h3, s2 )
    net.addLink( h4, s3 )
    net.addLink( h5, s3 )
    net.start()
    CLI( net )
    net.stop()
if __name__ == '__main__':
    setLogLevel( 'info' )
    aggNet()