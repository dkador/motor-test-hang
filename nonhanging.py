import motor

__author__ = 'dkador'

mongo_connection_sync = motor.MotorReplicaSetConnection(
    "localhost",
    replicaSet="keen_service"
)

if __name__ == "__main__":
    print "This doesn't hang."