Como manejarse con Git:
    -En rama development se manejan los cambios, cada dev tendrá una rama de la cual trabajar, al iniciar
       la mergea con development, trabaja, una vez termina su trabajo pushea su rama, y cuando confirme que es código funcional se mergea a development
       Ej: git checkout mi_rama , git merge development (work) git add, git commit, git push mi_rama, git checkout development, git push development.

    -La rama main se va a actualizar mediante push request desde la rama development, ninguna otra rama se conecta con main.

Como manejarse con el front y el back:
    -En el .gitignore estan los ignore para react y django
    -En la carpeta back generar un virtualenv con el nombre 'venv' con python3 (para que lo tome el .gitignore), una ves abierto el venv,
    instalar las dependencias desde requirements.txt.
    -En la carpeta front crear un proyecto en react y despues cargar pullear los datos de la app, o llevar los módulos.
    
