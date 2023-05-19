#!/usr/bin/env python3
# from fabric.api import env, run  
from fabric import Connection
from fabric.api import env

# Hosts
web_01 = '54.160.79.52'
web_02 = '54.160.79.52'
env.user = 'ubuntu'
env.hosts = [web_01, web_02]
env.key_filename = '~/.ssh/id_rsa'

result = Connection('52.87.215.121').run('uname -s', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))