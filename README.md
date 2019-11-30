# odoo11
Pruebas con Odoo 11

30/11/19 -  sudo chown -R ubuntu odoo11     (permisos carpeta Git)
Pruebas con GIT:

            git add Readme.md / git add .
            git commit -m "Update readme file"
            git push origin master (japarici , pass: 05)
        Crear rama:
            git pull origin master (traemos cambios)
            git checkout -b v2  (creamos)
            git branch          (revisamos; con -a vemos lo oculto)
            git push origin v2
        Para juntarlas:
            git checkout master (nos posicionamos)
            git merge v2
            git push origin v2
