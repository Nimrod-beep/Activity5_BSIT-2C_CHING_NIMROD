
from array_queue import ArrayQueue


def print_queue_simulation():
    jobs = ArrayQueue(5)

    print("PRINT QUEUE SIMULATION")

    jobs_to_add = [
        ("JOB101", 5),
        ("JOB102", 2),
        ("JOB103", 8)
    ]

    for job_id, pages in jobs_to_add:
        jobs.enqueue((job_id, pages))

        print("Added:", job_id)
        print("Pages:", pages)
        print("Current queue:", jobs.show())

    print("\nPrinting jobs:")

    wait_order = 1

    while not jobs.is_empty():
        job_id, pages = jobs.dequeue()

        print("Wait order:", wait_order)
        print("Printing:", job_id)
        print("Number of pages:", pages)

        wait_order = wait_order + 1

        print("Remaining queue:", jobs.show())


if __name__ == "__main__":
    print_queue_simulation()
