# Quick-Copy
![kuikku](https://user-images.githubusercontent.com/79365546/202890626-bc91a04f-3c09-498c-934b-9be699e76287.png)

# What is QuickCopy?
QuickCopyはコピー作業効率化を目指しているGUIツールです。
コピーリストでコピーしたいものを管理し、
ワンクリックでクリップボードに収納します。
PySide6 GUIフレームワークを使用し作成されました。
そのためOSに依存することなく、Windows,macとLinuxと複数のOSで実行が可能です。

# 操作手順
操作手順はリリース版に公開してある操作方法のzipファイルの動画を参照してください

# 注意事項
このツールはWindowsとmacで操作確認をしましたが、PyinstallerでうまくコンパイルできたのはWinodwsだけでしたので、
macで実行する際はPythonで実行して試してください




# PyInstaller
PyInstallerとは、さまざまなOSでスタンドアロンとして実行可能ファイルにパッケージ化します。
URL -> https://pypi.org/project/pyinstaller/

以下のコマンドでコンパイルします

```shell
pyinstaller --name="QuickCopy" --windowed --icon=icon/QuickCopy.ico .\QuickCopy_PyInstaller\__main__.py
```
distフォルダが生成されQuickCopyフォルダの中にexeファイルが存在します。
