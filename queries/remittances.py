def list(client, job_config=None):
    query = """
        select
            id
            , user_id
            , amount
            , currency
        from
            dataset.remittances
    """
    return client.query(query, job_config=job_config)
