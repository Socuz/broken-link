# Template S2I

Simply process the file `template-s2i.yaml` to create:
- Build Config
- Image Stream
- Cronjob

You will need four parameters:
- NAMESPACE: Name of your Rahti project/namespace
- GITHUB_URL: URL of the GitHub repo where to source for building the image
- GITHUB_BRANCH: Name of the GitHub branch. By default "main"
- EMAIL_RECIPIENT: Email address of the recipient(s)

Example:
```shell
oc process -f template-s2i.yaml -p NAMESPACE="my-project-test" -p GITHUB_URL="https://github.com/Socuz/broken-link.git" -p GITHUB_BRANCH="otherbranch" -p EMAIL_RECIPIENT="some.address@world.com" | oc apply -f - 
```
You can modify the schedule of the cronjob by modifying the line `schedule`:
```yaml
...
spec:
    schedule: '0 3 2 * *'
    jobTemplate:
...
```

More information about cron:  
https://en.wikipedia.org/wiki/Cron

Cronjob scheduler:  
https://crontab.guru/