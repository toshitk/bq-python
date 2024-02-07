from google.cloud import bigquery
from google.cloud.bigquery import job as bq_job
from datetime import datetime

from queries import users, remittances

LOCATION = "asia-northeast1"
client = bigquery.Client()

def _print(msg: str) -> None:
    print(f"{datetime.now()} {msg}")

def get_job_result(client, job_id: str) -> dict:
    job = client.get_job(job_id, location=LOCATION)

    state = job.state
    error = job.error_result

    return {
        "job": job,
        "state": state,
        "error": error,
        "succeeded": state == bq_job._DONE_STATE and error is None
    }

def main():
    job_config = bigquery.QueryJobConfig()

    users_job = users.list(client=client, job_config=job_config)
    remittances_job = remittances.list(client=client, job_config=job_config)
    jobs = [users_job, remittances_job]

    _print(f"Job(users) created. job_id: {users_job.job_id}")
    _print(f"Job(remittances) created. job_id: {remittances_job.job_id}")

    job_ids = [job.job_id for job in jobs]

    job_state_dict = {
        job_id: get_job_result(client=client, job_id=job_id)
    for job_id in job_ids}

    for job_id, v in job_state_dict.items():
        _print(f"job_id: {job_id}")
        _print("data:")
        for data in v["job"].result():
            _print(data)

if __name__ == "__main__":
    main()
