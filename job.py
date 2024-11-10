# Class to represent a job
class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

# Function to schedule jobs for maximum profit
def job_sequencing(jobs, n):
    # Sort all jobs according to descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # To keep track of free time slots
    result = [False] * n

    # To store the result (sequence of jobs)
    job_sequence = ['-1'] * n

    total_profit = 0  # To keep track of total profit

    # Iterate through all the jobs
    for i in range(len(jobs)):
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if result[j] is False:
                result[j] = True
                job_sequence[j] = jobs[i].job_id
                total_profit += jobs[i].profit
                break

    # Print the job sequence
    print("Job sequence for maximum profit:", job_sequence)
    print("Total Profit:", total_profit)

# Input from the user
n_jobs = int(input("Enter the number of jobs: "))

jobs = []

for i in range(n_jobs):
    job_id = input(f"Enter Job ID for Job {i+1}: ")
    profit = int(input(f"Enter Profit for Job {i+1}: "))
    deadline = int(input(f"Enter Deadline for Job {i+1}: "))
    jobs.append(Job(job_id, profit, deadline))

# Maximum number of time slots (assuming maximum deadline)
max_deadline = max(job.deadline for job in jobs)

# Call the job sequencing function
job_sequencing(jobs, max_deadline)
