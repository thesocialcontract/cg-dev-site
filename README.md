# CG-DEV-SITE
Source for my dev site.  Intended to be a gallery and playground.

GCP Needs requirements.txt and NO pipfile!  Generate with `pipenv lock -r > requirements.txt`


gcloud app deploy app.yaml

To access the cloud DB, run `wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy`
Then `chmod+x cloud_sql_proxy`
Then `./cloud_sql_proxy -instances={db-connection-name}=tcp:3306`


SET THESE ENVS BEFORE DEPLOY:
CG_SITE_DB_HOST
CG_SITE_DB_USER
CG_SITE_DB_PASS
CG_SITE_DB_NAME