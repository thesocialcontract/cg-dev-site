# CG-DEV-SITE
Source for my dev site.  Intended to be a gallery and playground.

## Setup
You'll need:
- Python 3.8 or greater.
- Google Cloud SDK
- Google Cloud SQL Proxy
- Pipenv

Step into the directory in your terminal and run `pipenv shell`

To access the cloud DB proxy on Linux:
- Run `wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy`
- Then `chmod+x cloud_sql_proxy`
- Then `./cloud_sql_proxy -instances={db-connection-name}=tcp:3306`

There are secrets that need passed to Django.  In order to keep them out of source, we'll place those secrets in local files not included in source control.  Make sure you add the **.env** file and the **env_variables.yaml** file.  Add these env variables:
- CG_SITE_DB_HOST
- CG_SITE_DB_USER
- CG_SITE_DB_PASS
- CG_SITE_DB_NAME

## To Deploy
- Validate server runs locally (see Django Docs).
- Change ALLOWED_HOSTS in settings.py from dev to prod line.
- Generate dependencies with `pipenv lock -r > requirements.txt`
- Run `gcloud app deploy app.yaml`

## Wishlist
- React or Angular frontend.
- Simplify deploy to a command.
- Simplify setup to a command.
- Switch to ASGI to enable websockets applications.
- Plug in Aji.
- Enable Development Blog.
- Enable Cloud Storage integration for file sharing:
    - Public Sharing.
    - Private Sharing.
- Glitchart Gallery.
- Resume Page.
- Github/Code walkthrough.
- Store static files on GStorage
- Light/Dark Mode
    - Glitch Stylesheets
    - Material Stylesheets
    - Gradient Stylesheets
    - WYLTPA Stylesheets
- If we use a CMS, use [wagtail](https://docs.wagtail.io/)

## Tech to Explore
- Testing in Django
- Realtime Glitchart, like Processing

## Apps
- blog
- portfolio
- 