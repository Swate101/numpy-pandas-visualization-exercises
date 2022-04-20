# READ ONLY credentials
host = "157.230.209.171"
username = "jemison_1761"
user = username
password = "mUwSQRpZLSsgrnewaSSQw5dW3ynD7cWw"


def get_db_url(db_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url