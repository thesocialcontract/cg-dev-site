# CG-DEV-SITE
Source for my dev site.  Intended to be a gallery and playground.

## Setup
You'll need:
- Python 3.8 or greater.
- Google Cloud SDK
- Pipenv

There are secrets that need passed to Django.  In order to keep them out of source, we'll place those secrets in local files not included in source control.  Make sure you add the **.env** file and the **env_variables.yaml** file.  See cgsite/env_var_service.py for list of required env variables.

Set environment variables in `.env` to your local postgresql instance.  Step into the directory in your terminal and run `pipenv install` then run `pipenv shell`

## Local Development
1. Validate environment variables in `.env` to your local postgresql instance.  Set `CG_SITE_DEPLOY_ENV=local`
2. Activate pipenv by running `pipenv shell`
3. Run `python manage.py runserver`

## To Deploy
- Create env_variables_prod.yaml if necessary
- run deploy.sh

## Wishlist
- React or Angular frontend.
- ~~Simplify deploy to a command.~~
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
- gallery