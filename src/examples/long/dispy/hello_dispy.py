"""
This is an example of how to use the "dispy" distribution
cluster
"""


import time
import socket
import random
import dispy


def compute(n):
    """ "compute" is distributed to each node running "dispynode" """
    time.sleep(n)
    host = socket.gethostname()
    return host, n


def main():
    cluster = dispy.JobCluster(compute)
    jobs = []
    for i in range(10):
        # schedule execution of "compute" on a node (running "dispynode")
        # with a parameter (random number in this case)
        job = cluster.submit(random.randint(5, 20))
        job.id = i  # optionally associate an ID to job (if needed later)
        jobs.append(job)
    # cluster.wait() # waits for all scheduled jobs to finish
    for job in jobs:
        host, n = job()  # waits for job to finish and returns results
        print(f"{host} executed job {job.id} at {job.start_time} with {n}")
        # other fields of "job" that may be useful:
        # print(job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time)
    cluster.print_status()


if __name__ == "__main__":
    main()
