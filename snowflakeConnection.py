from snowflake import connector


def sfconnect():
    cnx = connector.connect(
        account='ft45898.us-central1.gcp',
        user='YUPEICHEN',
        password='Cent##0499',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC')
    return cnx
