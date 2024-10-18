# duckdb-sql-syntax-highlighting-in-python README


## Development

https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#injection-grammars

https://github.com/ptweir/python-string-sql/tree/master (MIT License)

## Rebuilding
If you want to experiment with another regex match in in [syntaxes/injection.json](./syntaxes/injection.json?plain=1#L4), you need to ensure the extension is refreshed.

```sh
vsce package && code --uninstall-extension duckdb-sql* && code --install-extension duckdb-sql*`
```
Not sure if you you also need to reload:
`CTRL+SHIFT+P -> Developer: Reload Window`

## Multi-line match support
This is quite tricky. See this issue: https://github.com/microsoft/vscode-textmate/issues/41