# python_scripts
Script `sets_hosts`.

Script sets host record in /etc/hosts To add new records add new line to hosts list.
You can do it in two ways:
  - read from the file
```
./sets_hosts fileToRead
```
  - add record to hosts lists
```
hosts = [['192.168.56.101', 'host1', 'host1.dev.internal'],
         ['192.168.56.102', 'host2', 'host2.dev.internal'],
         ['ipaddress', 'hostname', 'fqdn'],
]
```
