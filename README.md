<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/launchd-exec.svg?maxAge=3600)](https://pypi.org/project/launchd-exec/)
[![](https://img.shields.io/npm/v/launchd-exec.svg?maxAge=3600)](https://www.npmjs.com/package/launchd-exec)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-exec.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-exec/)

#### Installation
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
~/Library/Logs/launchd-exec/bash/<datetime>.<pid>/launchd.plist
~/Library/Logs/launchd-exec/bash/<datetime>.<pid>/out.log
~/Library/Logs/launchd-exec/bash/<datetime>.<pid>/err.log
```

#### Related projects
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>