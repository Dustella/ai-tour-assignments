$files = Get-ChildItem -Path "./Python ������ϰ" -Filter "*.py"

foreach ($file in $files) {
    $newName = $file.Name -replace '\.py$', '_work.py'
    
    Rename-Item -Path $file.FullName -NewName $newName
}
