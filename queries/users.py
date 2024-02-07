def list(client, job_config=None):
    query = """
        select
            id
            , name
            , age
            , address
        from
            dataset.users
    """
    return client.query(query, job_config=job_config)
