#!/usr/bin/env python

import subprocess
import paramiko
cmd = "vagrant ssh-config vagrant2"
p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
config = paramiko.SSHConfig()
config.parse(p.stdout)
print config.lookup("vagrant2")

