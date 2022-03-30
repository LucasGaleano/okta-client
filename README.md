# okta-client

The script will fetch and log to a file the okta events every 60 sec.

## How it works

Create a config file name okta.conf with this information in the root directory. (there is a example file in the repository)

```
[okta]
host = https://example.com
token = tokenKey
```

## Logging
The script will log all the events to log.json as a json format and to stdout as a syslog format.

you should use this config for the logrotate inside /etc/logrotate.d/okta

```
/path/to/file/log.json {
    rotate 5
    size 1G
    copytruncate
}
```

