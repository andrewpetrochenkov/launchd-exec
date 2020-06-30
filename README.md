<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/launchd-exec.svg?maxAge=3600)](https://pypi.org/project/launchd-exec/)
[![](https://img.shields.io/npm/v/launchd-exec.svg?maxAge=3600)](https://www.npmjs.com/package/launchd-exec)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/launchd-exec/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/launchd-exec/actions)

### Installation
```bash
$ [sudo] pip install launchd-exec
```

```bash
$ [sudo] npm i -g launchd-exec
```

#### Examples
```bash
$ launchd-exec bash -l path/to/script.sh
launchd-exec.<hash> # label

$ pid="$(/bin/launchctl list | grep "$label" | awk '{print $1}')"
```

logs:
```
~/Library/Logs/launchd-exec/<hash>/out.log
~/Library/Logs/launchd-exec/<hash>/err.log
~/Library/Logs/launchd-exec/<hash>/launchd.plist
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>