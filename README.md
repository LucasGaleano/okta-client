# okta-client

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
/path/to/file {
    rotate 5
    weekly
    size 1G
    copytruncate
}
```

