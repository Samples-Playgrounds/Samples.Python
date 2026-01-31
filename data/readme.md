
Check data folders:

```shell
find . -type d -iname "*.hwaifs"
```

Nuke data folders:

```shell
find . -type d -iname "*.hwaifs" -exec rm -rfv "{}" \;
```