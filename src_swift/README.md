# NLP 100 Drill Exercises 2015 ver. using Swift

## How to run

### find swift executing file

1. install Xcode6
2. run `$ find /Applications/Xcode.app -name swift | grep /bin/swift`
  - in my env, it returns `/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift`

### set swift executing file to PATH

3. `$ export PATH=(/Applications/Xcode.app/.../bin/):$PATH` or write the path to `.zshrc`

### run it

4. `$ swift hello.swift`

## Tips

it would be easily running by `./hello.swift` with setting suffix alias to `.zshrc`

## Reference

- Swiftをコマンドラインから実行 - Qiita - [http://goo.gl/9xe1pv]
