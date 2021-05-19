import os

# Database
DB_ENGINE       = os.getenv( 'CG_SITE_DB_ENGINE' )
DB_HOST         = os.getenv( 'CG_SITE_DB_HOST' )   # Endpoint
DB_PORT         = os.getenv( 'CG_SITE_DB_PORT' )
DB_USER         = os.getenv( 'CG_SITE_DB_USER' )
DB_PASS         = os.getenv( 'CG_SITE_DB_PASS' )
DB_NAME         = os.getenv( 'CG_SITE_DB_NAME' )

DJANGO_SECRET   = os.getenv( 'CG_SITE_DJANGO_SECRET' )
DEPLOY_ENV      = os.getenv( 'CG_SITE_DEPLOY_ENV' )
ALLOWED_HOSTS   = [ os.getenv( 'CG_SITE_ALLOWED_HOSTS_0' ), os.getenv( 'CG_SITE_ALLOWED_HOSTS_1' ) ]