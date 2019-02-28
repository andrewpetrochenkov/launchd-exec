[![](https://img.shields.io/pypi/v/launchd-exec.svg?maxAge=3600)](https://pypi.org/project/launchd-exec/)
[![](https://img.shields.io/npm/v/launchd-exec.svg?maxAge=3600)](https://www.npmjs.com/package/launchd-exec)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-exec.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-exec/)

#### Install
```bash
$ [sudo] npm i -g launchd-exec
```
```bash
$ [sudo] pip install launchd-exec
```

#### CLI
```bash
usage: launchd-exec command [args ...]
```

#### Examples
```bash
$ launchd-exec bash -l path/to/script.sh
```

logs:
```
~/Library/Logs/launchd-exec/bash/<datetime>/launchd.plist
~/Library/Logs/launchd-exec/bash/<datetime>/out.log
~/Library/Logs/launchd-exec/bash/<datetime>/err.log
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>