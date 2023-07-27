# Template S2I

Simply process the file `template-s2i.yaml` to create:
- Build Config
- Image Stream
- Cronjob

You can modify the schedule of the cronjob by modifying the line `schedule`:
```yaml
...
spec:
    schedule: '*/10 * * * *'
    jobTemplate:
...
```

More information about cron:  
https://en.wikipedia.org/wiki/Cron

Cronjob scheduler:  
https://crontab.guru/