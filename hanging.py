import pymongo

__author__ = 'dkador'

mongo_connection_sync = pymongo.ReplicaSetConnection(
    "localhost",
    replicaSet="keen_service"
)

if __name__ == "__main__":
    print "This hangs on my machine. ctrl+c doesn't work."