# django-learning

## Tooling

### djlint (Django template formatter)

Install djlint as a global uv tool:

```
uv tool install djlint
```

Install the VS Code extension: `monosans.djlint`

Add to `.code-workspace` settings (not `.vscode/settings.json` — doesn't apply in multi-root workspaces):

```json
"djlint.useVenv": false,
"djlint.executablePath": "C:\\Users\\<username>\\AppData\\Roaming\\uv\\tools\\djlint\\Scripts\\djlint.exe"
```

Format on save is configured in `.vscode/settings.json`:

```json
"[html]": {
    "editor.defaultFormatter": "monosans.djlint",
    "editor.formatOnSave": true
},
"[django-html]": {
    "editor.defaultFormatter": "monosans.djlint",
    "editor.formatOnSave": true
}
```
