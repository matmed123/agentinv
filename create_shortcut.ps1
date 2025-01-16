$ShortcutPath = "$env:USERPROFILE\Desktop\AgenteInv.lnk"
$TargetPath = "C:\Program Files\Python311\python.exe"
$Arguments = "c:\Users\matia\Desktop\test2\main.py"
$IconPath = "c:\Users\matia\Desktop\test2\main.py"

$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.Arguments = $Arguments
$Shortcut.IconLocation = $IconPath
$Shortcut.Save()