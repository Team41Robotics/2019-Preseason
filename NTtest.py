from networktables import NetworkTables

NetworkTables.initialize(server='10.0.41.62')

smartdashboard = NetworkTables.getTable("SmartDashboard")
for i in range(0,10000000000000000):
	smartdashboard.putNumber('testnum',i)

