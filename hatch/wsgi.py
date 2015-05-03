import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hatch.settings")

# In production, fill in the actual values of these environ vars. 
# In development, export these environ vars in ~/.bashrc
os.environ["HATCH_SECRET_KEY"] = ""
os.environ["HATCH_DB_PW"] = ""
os.environ["HATCH_ACCOUNT_REDIRECT_URL"] = "" 
os.environ["HATCH_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY="] = "" 
os.environ["HATCH_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"] = "" 

application = get_wsgi_application()
