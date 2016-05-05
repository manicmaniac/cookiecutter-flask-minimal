from fabric.api import cd, local, put, run, task


@task
def pack():
    local('python setup.py sdist --formats=gztar', capture=False)


@task
def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/{{cookiecutter.package}}.tar.gz')
    run('mkdir /tmp/{{cookiecutter.package}}')
    with cd('/tmp/{{cookiecutter.package}}'):
        run('tar xzf /tmp/{{cookiecutter.package}}.tar.gz')
        run('/var/www/{{cookiecutter.package}}/env/bin/python setup.py install')
    run('rm -rf /tmp/{{cookiecutter.package}} /tmp/{{cookiecutter.package}}.tar.gz')
    run('touch /var/www/{{cookiecutter.package}}.wsgi')
