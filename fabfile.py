from fabric.api import *
import fabric.contrib.project as project
import os, datetime

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def debug():
    local('pelican -s pelicanconf.py -D')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

def lpublish():
    with lcd('~/Coding/jdotjdot.github.io'):
      local('git pull origin master')
    local('pelican -s publishconf.py -o /Users/JJ/Coding/jdotjdot.github.io')
    # have to do some of this b/c pelican -o kills the .git directory
    # local('cd ~/Coding/jdotjdot.github.io && '
    #        # 'git init && git remote add origin https://github.com/jdotjdot/jdotjdot.github.io.git '
    #        'git clean -f && '
    #        'git add . && '
    #        'git commit -m "Published on {} by Fabric" && '
    #        'git pull origin master && '
    #        'git push origin master'.format(datetime.datetime.now().isoformat())
    # )

    with lcd('~/Coding/jdotjdot.github.io'):
      local('git clean -f')
      local('git add .')
      local('git commit -m "Published on {} by Fabric"'.format(datetime.datetime.now().isoformat()))
      local('git push origin master')

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
