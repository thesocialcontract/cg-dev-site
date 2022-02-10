# CG-DEV-SITE
Source for my dev site.  Intended to be a gallery and playground.

## Setup
You'll need:
- Python 3.8 or greater.
- Google Cloud SDK
- Pipenv

In order to keep secrets out of source, we place them in local files not included in source control. Django and postgres requires secrets, and they vary based on the deploy environment. Make sure you add the **.env** file and the **env_variables.yaml** file.  See cgsite/env_var_service.py for list of required env variables.

# Local Setup
We utilize pipenv's env file to inject environment secrets to our local deployment.

# GCP Deploy
GCP Deploy will inject environment secrets via the **env_variables.yaml** file.

Set environment variables in `.env` to your local postgresql instance.  Step into the directory in your terminal and run `pipenv install` then run `pipenv shell`

## Local Development
1. Validate environment variables in `.env` to your local postgresql instance.  Set `CG_SITE_DEPLOY_ENV=local`
1. Activate pipenv by running `pipenv shell`
1. Ensure postgres is running locally (if not, run `sudo service postgresql start`)
1. Run SCSS compiler in watch mode `sass --watch styles/:cgsite/static/css/`
1. Run `python manage.py runserver`

## To Deploy
- Create env_variables_prod.yaml if necessary
- run deploy.sh

## Wishlist
- Switch to ASGI to enable websockets applications.
- Plug in Aji.
- Enable Development Blog.
- Glitchart Gallery.
- Resume Page.
- Github/Code walkthrough.
- Store static files on GStorage
- Get CMS [wagtail](https://docs.wagtail.io/)

## Tech to Explore
- Testing in Django
- Realtime Glitchart, like Processing

## App Structure
- cgsite -- The main django application folder
- top    -- Where toplevel, non-important, misc stuff go. This is where I would route to 1 page experiments
- cms    -- Anything workable in cms. e.g. Blogs, style guides, etc.