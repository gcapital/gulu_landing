# Gulu-landing fabfile

from fabric.api import *
from fabric.operations import *
from fabric.utils import *
from fabric.contrib.files import *
from fabric.colors import green, yellow, red

"""
Base configuration
"""
env.disable_known_hosts = True
env.project_name = 'gulu_landing'
env.site_media_prefix = "static"
env.path = '/home/gulu/sites/%(project_name)s' % env
env.log_path = '/home/gulu/logs/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.src_path = '%(path)s/src' % env
env.repo_path = '%(path)s/repository' % env
env.apache_config_path = '/etc/apache2/sites-enabled/gulu_landing'
env.nginx_config_path = '/etc/nginx/sites-enabled/gulu_landing'
#env.solr_config_path = '/etc/solr/conf/schema.xml'
env.python = 'python2.6'
env.repository_url = "git@github-landing:gcapital/gulu_landing.git"
env.ssh_key = "~/.ssh/id_rsa2"

"""
Environments
"""
def production():
    """
    Selects production environment.
    """
    
    ### This is currently holding the landing page
    #abort("Production deployment is currently disabled.")
    
    env.settings = 'production'
    env.hosts = ['gulu.com']
    env.user = 'gulu'
    env.generic = False

def staging():
    abort("Staging deployment is currently disabled.")
    """
    Selects staging environment.
    """
    env.settings = 'staging'
    env.hosts = ['beta.gulu.com'] 
    env.user = 'gulu'
    env.generic = False

def demo():
    abort("Demo deployment is currently disabled.")
    """
    Selects demo environment.
    """
    env.settings = 'demo'
    env.hosts = ['demo.gulu.com']
    env.user = 'gulu'
    env.generic = False

def generic(host_name):
    abort("Generic deployment is currently disabled.")
    """
    Selects generic environment (arbitrary host)
    """
    env.settings = 'generic'
    env.hosts = [host_name,]
    env.user = 'gulu'
    env.generic = True # NOT staging / production deployment
   
   
"""
Branches
"""
def stable():
    """
    Selects stable branch.
    """
    env.branch = 'stable'

def master():
    """
    Selects development branch.
    """
    env.branch = 'master'

def branch(branch_name):
    """
    Selects any an arbitrary branch.
    """
    env.branch = branch_name

 
"""
Commands - setup
"""
def setup():
    """
    Sets up a remote deployment environment.
    
    Does NOT perform the functions of deploy().
    """
    require('generic', 'settings', provided_by=[production, staging, generic])
    require('branch', provided_by=[stable, master, branch])
    
    if env.generic:
        print green("Performing a generic setup on: %s" % env.hosts[0])
    else:
        print green("Performing a staging/production setup on: %s" % env.hosts[0])
    
    setup_directories()
    setup_virtualenv()
    clone_repo()
    checkout_latest()
    fix_perms()
    install_django_nonrel()
    install_requirements()
    load_data()
    
    if env.generic:
        write_conf_generic()
    
    install_webserver_conf()
    #install_solr_conf()
    #rebuild_solr_index()
    reboot()

def setup_directories():
    """
    Creates directories necessary for deployment.
    """
    print yellow("Creating project directories...")
    
    run('mkdir -p %(path)s' % env)
    run('mkdir -p %(env_path)s' % env)
    run('mkdir -p %(src_path)s' % env)
    run ('mkdir -p %(log_path)s;' % env)
    sudo('chgrp -R www-data %(log_path)s; chmod -R g+w %(log_path)s;' % env)
    run('ln -s %(log_path)s %(path)s/logs' % env)
    
def setup_virtualenv():
    """
    Sets up a fresh virtualenv and installs pip.
    """
    print yellow("Setting up a fresh virtual environment...")
    
    run('virtualenv -p %(python)s --no-site-packages %(env_path)s;' % env)
    with prefix('source %(env_path)s/bin/activate' % env):
        run('easy_install -U setuptools; easy_install pip;' % env)

def clone_repo():
    """
    Do initial clone of the git repository.
    """
    print yellow("Cloning git repo...")
    
    run('git clone -q %(repository_url)s %(repo_path)s' % env)

def checkout_latest():
    """
    Pull the latest code on the specified branch.  Overwrites any local
    configuration changes.
    """
    print yellow("Pulling latest source...")
    
    with prefix('cd %(repo_path)s' % env):
        sudo('chown -R %(user)s %(path)s' % env)
        run('git reset --hard HEAD')
        run('git checkout %(branch)s' % env)
        run('git pull origin %(branch)s' % env)

def fix_perms():
    """
    Gives www-data user permissions to photos directory
    """
    sudo('chown -R www-data %(repo_path)s/%(project_name)s/assets' % env)

def install_requirements():
    """
    Install the required packages using pip.
    """
    print yellow("Installing pip requirements...")
    
    with prefix('source %(env_path)s/bin/activate' % env):
        run('pip install -E %(env_path)s -r %(repo_path)s/requirements.txt' % env)

def install_django_nonrel():
    """
    Installs django-nonrel
    """
    print yellow("Installing django-nonrel...")
    
    with prefix('cd %(src_path)s' % env):
        run('hg clone https://bitbucket.org/wkornewald/django-nonrel' % env)
    with prefix('source %(env_path)s/bin/activate' % env):
        run('python %(src_path)s/django-nonrel/setup.py --quiet install' % env)

def install_webserver_conf():
    """
    Install the apache and nginx site config file.
    """
    print yellow("Installing apache and nginx config...")
    
    # TODO: update images so chown isn't necessary
    sudo('chown -R www-data /var/log/apache2')
    sudo('cp %(repo_path)s/%(project_name)s/configs/%(settings)s/apache %(apache_config_path)s' % env)
    sudo('cp %(repo_path)s/%(project_name)s/configs/%(settings)s/nginx %(nginx_config_path)s' % env)

def install_solr_conf():
    """
    Install the solr conf file
    """
    with prefix('source %(env_path)s/bin/activate' % env):
        with prefix('cd %(repo_path)s/%(project_name)s/configs/%(settings)s' % env):
            sudo('python manage.py build_solr_schema > %(solr_config_path)s' % env)
    
def rebuild_solr_index():
    """
    Rebuilds the solr index
    """
    rebuild = prompt('Rebuild solr index? [Y/n]', default='Y', validate=r'y|Y|n|N')
    
    if rebuild in "yY":
        print yellow("Rebuilding solr index (this will take a while)...")
        with prefix('source %(env_path)s/bin/activate' % env):
            with prefix('cd %(repo_path)s/%(project_name)s/configs/%(settings)s' % env):
                sudo('python manage.py rebuild_index --remove --verbosity 1')

def update_solr_index():
    """
    Updates the solr index
    """
    update = prompt('Update solr index? [Y/n]', default='Y', validate=r'y|Y|n|N')
    
    if update in "yY":
        print yellow("Updating solr index (this will take a while)...")
        with prefix('source %(env_path)s/bin/activate' % env):
            with prefix('cd %(repo_path)s/%(project_name)s/configs/%(settings)s' % env):
                sudo('python manage.py update_index --remove --verbosity 1')

def write_conf_generic():
    """
    Writes the django, apache, and nginx settings files for a generic deployment.
    """
    print yellow("Writing conf files...")
    
    require('generic', provided_by=[generic])
    
    cfg_path = "%(repo_path)s/%(project_name)s/configs/generic/" % env
    sed("%ssettings.py" % cfg_path, r'^.*MEDIA_URL.*$', "MEDIA_URL = \"http://%s/assets/\"" % env.hosts[0])
    sed("%sapache" % cfg_path, r'^.*ServerName.*$', "ServerName %s" % env.hosts[0])
    sed("%snginx" % cfg_path, r'^.*server_name.*$', "server_name %s;" % env.hosts[0])

"""
Commands - deployment
"""
def deploy():
    """
    Deploy the latest version of the site to the server and restarts web servers.
    """
    require('generic', 'settings', provided_by=[production, staging, generic])
    require('branch', provided_by=[stable, master, branch])
    
    if env.generic:
        print green("Performing a generic deployment to: %s" % env.hosts[0])
    else:
        print green("Performing a staging/production deployment to: %s" % env.hosts[0])
    
    #with settings(warn_only=True):
        #maintenance_up()
        
    checkout_latest()
    fix_perms()
    
    if env.generic:
        write_conf_generic()
    
    install_webserver_conf()
    #install_solr_conf()
    #update_solr_index()
    reboot()
    
def deploy_onebox():
    """
    Deploys the latest version to a onebox
    """
    require('settings', provided_by=[onebox])
    require('branch', provided_by=[stable, master, branch])

    checkout_latest()

def maintenance_up():
    """
    Install the Apache maintenance configuration.
    """
    sudo('cp %(repo_path)s/%(project_name)s/configs/%(settings)s/apache_maintenance %(apache_config_path)s' % env)
    reboot()
       
def reboot(): 
    """
    Restarts the apache2 and nginx servers.
    """
    print yellow("Restarting web servers...")
    
    sudo('/etc/init.d/apache2 restart', pty=False)
    sudo('/etc/init.d/nginx restart')
    #sudo('/etc/init.d/tomcat6 restart')

def maintenance_down():
    """
    Reinstall the normal site configuration.
    """
    install_apache_conf()
    reboot()
    
"""
Commands - rollback
"""
def rollback(commit_id):
    """
    Rolls back to specified git commit hash or tag.
    
    There is NO guarantee we have committed a valid dataset for an arbitrary
    commit hash.
    """
    require('settings', provided_by=[production, staging])
    require('branch', provided_by=[stable, master, branch])
    
    maintenance_up()
    checkout_latest()
    git_reset(commit_id)
    gzip_assets()
    deploy_to_s3()
    maintenance_down()
    
def git_reset(commit_id):
    """
    Reset the git repository to an arbitrary commit hash or tag.
    """
    env.commit_id = commit_id
    run("cd %(repo_path)s; git reset --hard %(commit_id)s" % env)

"""
Commands - data
"""
def load_new_data():
    """
    Erase the current database and load new data from the SQL dump file.
    """
    require('settings', provided_by=[production, staging])
    
    maintenance_up()
    destroy_database()
    create_database()
    load_data()
    maintenance_down()
    
def create_database(func=run):
    """
    Creates the user and database for this project.
    """
    
def destroy_database(func=run):
    """
    Destroys the user and database for this project.
    
    Will not cause the fab to fail if they do not exist.
    """
    print yellow("Destroying database...")
    with settings(warn_only=True):
        sudo('mongo %(project_name)s  --eval "db.dropDatabase();"' % env)
        
def load_data():
    """
    Loads data from the repository into MongoDB.
    """
    with prefix('source %(env_path)s/bin/activate' % env):
        with prefix('cd %(repo_path)s/%(project_name)s/configs/%(settings)s' % env):
            run('python manage.py syncdb --noinput')
    run('mongorestore -d %(project_name)s %(repo_path)s/data/gulu' % env)

"""
Commands - miscellaneous
"""  
def clear_cache():
    """
    Restart memcache, wiping the current cache.
    """
    sudo('service memcached restart')
    
def echo_host():
    """
    Echo the current host to the command line.
    """
    run('echo %(settings)s; echo %(hosts)s' % env)

"""
Deaths, destroyers of worlds
"""
def shiva_the_destroyer():
    """
    Remove all directories, databases, etc. associated with the application.
    """
    go = prompt(red("WARNING: This command will destroy everything related to this deployment.  Type 'yes' to continue:"))
    if go not in ["yes", "Yes", "YES"]:
        print yellow("Exiting...")
        return

    print yellow("Destroying environment...")
    with settings(warn_only=True):
        sudo('rm -Rf %(path)s' % env)
        sudo('rm -Rf %(log_path)s' % env)
        sudo('rm %(apache_config_path)s' % env)
        sudo('rm %(nginx_config_path)s' % env)
        destroy_database()
        reboot()

"""
Utility functions (not to be called directly)
""" 
def bootstrap():
    """
    Local development bootstrap: you should only run this once.
    """    
    create_database(local)
    local("sh ./manage syncdb --noinput")
    #local("sh ./manage load_shapefiles")

def shiva_local():
    """
    Undo any local setup.  This will *destroy* your local database, so use with caution.
    """    
    destroy_database(local)
