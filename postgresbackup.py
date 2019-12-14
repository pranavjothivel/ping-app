#!/usr/bin/env python
import os
import subprocess
import sys
import shutil
import datetime

path = 'TEMP'
time = datetime.datetime.now()
file = str(time)
backup_command = str('pg_dumpall > %s ' % file)
delete_temp_command = str('shutil.rmtree(%s)' % path)
backup = None
arg = sys.argv[1]

print('Starting Postgres Backup job at %s' % time)

if arg == 'auto':
    backup == 'automatic'
elif arg == 'manual':
    backup == 'manual'
else:
    raise Exception('Argument needed for script execution type')

print('Starting %s database backup at %s' % backup, time)

try:
    os.mkdir(path)
except OSError as e:
    print('Creating directory %s failed' % path)
    print('Error: %s' % e)
    print('Exiting...')
    sys.exit()
else:
    print('Successfully created directory %s' % path)

try:
    subprocess.call(backup_command) 
except OSError as e:
    print('Error processing command')
    print('OSError: %s' % e)
    print('Exiting...')
    exit
else:
    print('Successfully backed up database')

try:
    subprocess.call(delete_temp_command)
except OSError as e:
    print('Error deleting temp directory')
    print('OSError: %s' % e)
    print('Exiting...')
else:
    print('Successfully deleted temp directory')

print('Ending database backup at %s' % time)


# lookup how to use python classes

# lookup python raise
# lookup use if statement and allow to run if matches
# lookup python exceptions
# lookup