from google.cloud import bigquery
from google.cloud.bigquery import job
from datetime import datetime

LOCATION = "asia-northeast1"

def _print(msg: str) -> None:
    print(f"{datetime.now()} {msg}")

client = bigquery.Client()

query = """
    select
        first_name
        , last_name
    from
        dataset.sample
    ;
"""

job_config = bigquery.QueryJobConfig()
query_job = client.query(query, job_config=job_config)
job_id = query_job.job_id
_print(f"Job created. job_id: {job_id}")

while True:
    _job = client.get_job(job_id, location=LOCATION)
    print(_job.error_result)
    if _job.state == job._DONE_STATE and _job.error_result is None:
        _print("The query finished.")
        break
    _print(f"The query job {job_id} is currently in state {_job.state}")
    time.sleep(1)

_print("The query data:")
for row in query_job.result():
    _print(row)


