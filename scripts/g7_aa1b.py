# -*- coding: utf-8 -*-
"""Documentos GA7-220501096-AA1-EV04 y EV05 (instalación y ejercicio de Git)."""
import sys

from sena_doc import SenaDoc

FECHA = "Noviembre 2026"
REPO = "https://github.com/DylanA-dev/Proyecto-Adso-Lavadero"
CAPTURAS = r"C:\Users\dylan\Documents\OpenCode\ADSO\proyectos\lavadero\interfaz\capturas"


def ev04():
    d = SenaDoc(
        "GA7-220501096-AA1-EV04",
        "Instalación y configuración de herramienta de versionamiento (local/web)",
        FECHA,
    )
    d.intro([
        "El control de versiones requiere la instalación de una herramienta local y la "
        "configuración de un repositorio remoto que respalde el código y permita el trabajo "
        "colaborativo. En esta evidencia se documenta el proceso de instalación y "
        "configuración de Git en un equipo con Windows y su integración con GitHub como "
        "repositorio remoto del proyecto AquaLavado.",
        "El documento presenta los requisitos previos, los pasos de instalación, la "
        "configuración del usuario, la creación del repositorio local, la vinculación con "
        "el repositorio remoto y las verificaciones realizadas. Cada paso se acompaña de la "
        "evidencia obtenida en el equipo.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Instalar y configurar Git como herramienta de versionamiento local y GitHub como "
        "repositorio remoto, verificando su funcionamiento con el repositorio del proyecto "
        "AquaLavado.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Instalar Git en el equipo de trabajo y verificar la versión.",
        "Configurar el nombre, el correo y las preferencias globales del usuario.",
        "Crear y configurar el repositorio local del proyecto.",
        "Crear el repositorio remoto y enlazarlo con el repositorio local.",
        "Publicar los cambios y verificar la sincronización entre ambos entornos.",
    ])

    d.h2("2. Requisitos previos")
    d.tabla(
        ["Requisito", "Descripción"],
        [
            ["Sistema operativo", "Windows 10 u 11 de 64 bits."],
            ["Conexión a Internet", "Necesaria para descargar Git y sincronizar con GitHub."],
            ["Cuenta de GitHub", "Cuenta activa para crear el repositorio remoto."],
            ["Editor de código", "Visual Studio Code, configurado como editor de Git."],
            ["Espacio en disco", "Suficiente para el repositorio y el historial del proyecto."],
        ],
        anchos=[4.0, 11.6],
        caption="Requisitos previos para la instalación.",
    )

    d.h2("3. Instalación de Git")
    d.p("La instalación se realizó desde el sitio oficial de Git para Windows. El "
        "instalador incluye Git Bash, el administrador de credenciales y la integración con "
        "el explorador de archivos. Durante el proceso se conservaron las opciones "
        "recomendadas por el instalador, entre ellas el uso de Git desde la línea de "
        "comandos y la integración con el almacén de credenciales de Windows.")
    d.numeros([
        "Descargar el instalador de 64 bits desde https://git-scm.com/download/win.",
        "Ejecutar el instalador y aceptar la licencia de uso.",
        "Seleccionar la carpeta de instalación y los componentes predeterminados.",
        "Elegir el editor predeterminado para Git (Visual Studio Code).",
        "Mantener la opción de usar Git desde la línea de comandos y la consola de Windows.",
        "Seleccionar el administrador de credenciales de Windows para la autenticación.",
        "Finalizar la instalación y abrir una terminal nueva.",
    ])
    d.p("La verificación de la instalación se realizó con los comandos git --version, where "
        "git y git --exec-path. La siguiente captura muestra la versión instalada y la "
        "ubicación del ejecutable.")
    d.imagen(f"{CAPTURAS}\\git_version.png",
             "Verificación de la instalación de Git.", 14.5)

    d.h2("4. Configuración local")
    d.p("La configuración global define la identidad del usuario y las preferencias que se "
        "aplican a todos los repositorios del equipo. El nombre y el correo se registran en "
        "cada confirmación, por lo que deben coincidir con la cuenta utilizada en GitHub.")
    d.codigo(
        "git config --global user.name \"DylanA-dev\"\n"
        "git config --global user.email \"dylandavidariasrojas@gmail.com\"\n"
        "git config --global init.defaultBranch main\n"
        "git config --global core.autocrlf true\n"
        "git config --global core.editor \"code --wait\"")
    d.p("La opción init.defaultBranch establece main como rama inicial, coherente con el "
        "repositorio del proyecto. La opción core.autocrlf adapta los finales de línea al "
        "trabajar entre Windows y otros sistemas, y core.editor permite editar los mensajes "
        "de confirmación en Visual Studio Code.")
    d.imagen(f"{CAPTURAS}\\git_config.png",
             "Configuración global de Git y archivo de configuración.", 14.5)

    d.h2("5. Configuración del repositorio local")
    d.p("El repositorio local se creó en la carpeta del proyecto. Antes de la primera "
        "confirmación se definió el archivo .gitignore para excluir dependencias, "
        "compilados y archivos temporales, y se agregaron los archivos del proyecto al "
        "área de preparación.")
    d.codigo(
        "cd C:\\Users\\dylan\\Documents\\OpenCode\\ADSO\\proyectos\\lavadero\n"
        "git init\n"
        "git add .\n"
        "git commit -m \"feat: proyecto lavadero ADSO\"")
    d.p("El repositorio conserva las ramas main y remotes/origin/main, y el historial de "
        "confirmaciones con los cambios del proyecto. La siguiente captura muestra el "
        "repositorio remoto configurado, las ramas y el historial.")
    d.imagen(f"{CAPTURAS}\\git_repositorio.png",
             "Repositorio local, ramas e historial de confirmaciones.", 14.5)

    d.h2("6. Configuración del repositorio remoto")
    d.p("El repositorio remoto se creó en GitHub con el nombre Proyecto-Adso-Lavadero y "
        "visibilidad pública. Luego se enlazó con el repositorio local mediante el comando "
        "git remote add y se publicó la rama principal con git push.")
    d.codigo(
        "git remote add origin https://github.com/DylanA-dev/Proyecto-Adso-Lavadero.git\n"
        "git remote -v\n"
        "git push -u origin main")
    d.p("El repositorio remoto se encuentra disponible en " + REPO + ". La cuenta utiliza "
        "la autenticación de GitHub a través del administrador de credenciales de Windows, "
        "por lo que no es necesario escribir la contraseña en cada operación. La captura "
        "anterior muestra la confirmación publicada en origin/main, lo que evidencia la "
        "sincronización entre el repositorio local y el remoto.")

    d.h2("7. Verificación de la configuración")
    d.tabla(
        ["Verificación", "Comando", "Resultado"],
        [
            ["Versión instalada", "git --version", "git version 2.55.0.windows.3"],
            ["Ubicación del ejecutable", "where git", "C:\\Program Files\\Git\\cmd\\git.exe"],
            ["Nombre configurado", "git config --global user.name", "DylanA-dev"],
            ["Correo configurado", "git config --global user.email", "dylandavidariasrojas@gmail.com"],
            ["Rama inicial", "git config --global init.defaultBranch", "main"],
            ["Remoto configurado", "git remote -v", "origin con las URL de lectura y escritura"],
            ["Estado del repositorio", "git status", "Árbol de trabajo limpio"],
        ],
        anchos=[4.2, 6.4, 5.0],
        caption="Verificaciones de la instalación y la configuración.",
        size=7.5,
    )

    d.h2("8. Buenas prácticas de configuración")
    d.bullets([
        "Usar el mismo correo en Git y en GitHub para asociar correctamente las contribuciones.",
        "Mantener un archivo .gitignore desde el inicio del proyecto.",
        "Definir main como rama principal y protegerla en el repositorio remoto.",
        "No almacenar contraseñas ni tokens en archivos del repositorio.",
        "Verificar la configuración con git config --list antes de comenzar a trabajar.",
        "Publicar los cambios con frecuencia para conservar el respaldo remoto.",
    ])

    d.conclusion([
        "La instalación y configuración de Git permitió habilitar el control de versiones "
        "del proyecto AquaLavado y su respaldo en GitHub. La identidad del usuario, la rama "
        "principal y el manejo de los finales de línea quedaron definidos para todo el "
        "equipo.",
        "La verificación de la versión, la configuración y el repositorio remoto confirma "
        "que el entorno está listo para registrar los cambios del proyecto y sincronizarlos "
        "con la nube, cumpliendo con los lineamientos de la evidencia.",
    ])

    d.bibliografia([
        "Git. (2025). Git documentation. https://git-scm.com/doc",
        "Git for Windows. (2025). Git for Windows. https://git-scm.com/download/win",
        "GitHub. (2026). GitHub Docs: Set up Git. https://docs.github.com/es/get-started/getting-started-with-git/set-up-git",
        "GitHub. (2026). GitHub Docs: Managing remote repositories. https://docs.github.com/es/get-started/getting-started-with-git/managing-remote-repositories",
    ])
    return d.guardar()


def ev05():
    d = SenaDoc(
        "GA7-220501096-AA1-EV05",
        "Herramientas de versionamiento (GIT) instalada y configurada",
        FECHA,
    )
    d.intro([
        "La evidencia de desempeño de esta actividad consiste en ejecutar los comandos "
        "básicos de Git local y remoto sobre un repositorio de práctica llamado "
        "Programa-Git, y presentar el ejercicio en un video. Este documento reúne el paso a "
        "paso ejecutado, los comandos utilizados, los resultados obtenidos y el guion del "
        "video que se entrega en formato MP4.",
        "El ejercicio permite comprobar la creación de un repositorio, la preparación y "
        "confirmación de cambios, la creación de un archivo, el enlace con un repositorio "
        "remoto y la publicación del historial en GitHub.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Ejecutar los comandos básicos de Git local y remoto sobre el repositorio de "
        "práctica Programa-Git, verificando la creación del repositorio, el registro de "
        "cambios y la conexión con un repositorio remoto.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Crear un repositorio local y un repositorio público en GitHub.",
        "Preparar y confirmar los cambios del proyecto.",
        "Crear el archivo kotlin.txt con los datos del aprendiz.",
        "Enlazar el repositorio local con el remoto y publicar los cambios.",
        "Verificar el historial y el estado del repositorio.",
        "Documentar el guion del video de sustentación.",
    ])

    d.h2("2. Preparación del ejercicio")
    d.p("Antes de ejecutar los comandos se creó un repositorio público en GitHub con el "
        "nombre Programa-Git. El repositorio se creó sin archivos iniciales para evitar "
        "conflictos con el primer envío desde el equipo local.")
    d.tabla(
        ["Elemento", "Valor utilizado"],
        [
            ["Nombre del repositorio", "Programa-Git"],
            ["Visibilidad", "Pública"],
            ["Protocolo", "HTTPS"],
            ["Rama de trabajo", "master"],
            ["Archivo de práctica", "kotlin.txt"],
            ["Mensaje de confirmación", "Añadido datos."],
        ],
        anchos=[5.0, 10.6],
        caption="Datos del ejercicio Programa-Git.",
    )

    d.h2("3. Paso 1: crear el repositorio y enlazarlo")
    d.p("Se creó la carpeta de trabajo, se inicializó el repositorio local y se enlazó con "
        "el repositorio remoto. El comando git remote -v permite comprobar las direcciones "
        "de lectura y escritura configuradas.")
    d.codigo(
        "mkdir Programa-Git\n"
        "cd Programa-Git\n"
        "git init -b master\n"
        "git remote add github https://github.com/DylanA-dev/Programa-Git.git\n"
        "git remote -v")
    d.p("Resultado esperado: dos líneas con el nombre github, una para fetch y otra para "
        "push, con la URL del repositorio remoto.")

    d.h2("4. Paso 2: crear el archivo y confirmar los cambios")
    d.p("Se creó el archivo kotlin.txt con el nombre y el correo del aprendiz, se agregó al "
        "área de preparación y se confirmó con el mensaje solicitado por la guía.")
    d.codigo(
        "echo Dylan David Arias Rojas > kotlin.txt\n"
        "echo Correo: dylandavidariasrojas@gmail.com >> kotlin.txt\n"
        "git add .\n"
        "git status --short\n"
        "git commit -m \"Añadido datos.\"\n"
        "git log --oneline")
    d.p("La confirmación crea un registro en el historial con el identificador del commit, "
        "el autor, la fecha y el mensaje. La siguiente captura muestra la ejecución real de "
        "los pasos anteriores en el equipo.")
    d.imagen(f"{CAPTURAS}\\git_ejercicio.png",
             "Ejecución del ejercicio Programa-Git.", 15.0)

    d.h2("5. Paso 3: publicar en el repositorio remoto")
    d.p("Con el repositorio remoto enlazado y la confirmación creada, se publica la rama "
        "master. En GitHub se verifica que el archivo kotlin.txt y el historial estén "
        "disponibles en el repositorio público.")
    d.codigo(
        "git push github master")
    d.p("Después del envío, la página del repositorio en GitHub debe mostrar el archivo "
        "kotlin.txt, el mensaje Añadido datos. y la fecha de la confirmación. El historial "
        "local y el remoto deben coincidir.")

    d.h2("6. Comandos utilizados")
    d.tabla(
        ["Comando", "Tipo", "Función"],
        [
            ["git init -b master", "Local", "Crear el repositorio local en la rama master."],
            ["git status", "Local", "Consultar el estado de los archivos."],
            ["git add .", "Local", "Agregar los cambios al área de preparación."],
            ["git commit -m", "Local", "Registrar los cambios con un mensaje."],
            ["git log --oneline", "Local", "Consultar el historial resumido."],
            ["git remote add", "Remoto", "Enlazar el repositorio local con el remoto."],
            ["git remote -v", "Remoto", "Listar los repositorios remotos configurados."],
            ["git push", "Remoto", "Publicar los commits en el repositorio remoto."],
            ["git fetch", "Remoto", "Descargar los cambios sin fusionarlos."],
            ["git pull", "Remoto", "Descargar y fusionar los cambios del remoto."],
        ],
        anchos=[3.8, 2.2, 9.6],
        caption="Comandos ejecutados en el ejercicio.",
        size=7.5,
    )

    d.h2("7. Verificación de resultados")
    d.tabla(
        ["Verificación", "Resultado obtenido"],
        [
            ["Repositorio local creado", "Carpeta .git con la rama master."],
            ["Archivo de práctica", "kotlin.txt con el nombre y el correo."],
            ["Cambios preparados", "Archivo listado en el área de preparación."],
            ["Confirmación", "Commit con el mensaje Añadido datos."],
            ["Repositorio remoto", "github enlazado con la URL de GitHub."],
            ["Publicación", "Rama master enviada al repositorio remoto."],
        ],
        anchos=[5.0, 10.6],
        caption="Resultados del ejercicio.",
    )

    d.h2("8. Guion del video")
    d.p("El video se entrega en formato MP4, con una presentación inicial en la que se "
        "indica el nombre del aprendiz y los ejercicios que se van a realizar. La grabación "
        "muestra la terminal y la página de GitHub, y explica cada comando antes de "
        "ejecutarlo.")
    d.tabla(
        ["Momento", "Acción en pantalla", "Explicación"],
        [
            ["1. Presentación", "Diapositiva con el nombre y el objetivo del ejercicio.", "Saludo, nombre, programa y relación del ejercicio con el versionamiento."],
            ["2. Repositorio local", "Crear la carpeta y ejecutar git init.", "Explicar qué es un repositorio local y para qué sirve la rama master."],
            ["3. Archivo", "Crear kotlin.txt con el nombre y el correo.", "Mostrar el contenido del archivo antes de agregarlo."],
            ["4. Preparación y commit", "Ejecutar git add, git status y git commit.", "Explicar el área de preparación y el mensaje de confirmación."],
            ["5. Historial", "Ejecutar git log --oneline.", "Identificar el commit, el autor y el mensaje."],
            ["6. Repositorio remoto", "Crear el repositorio público Programa-Git en GitHub.", "Explicar la diferencia entre repositorio local y remoto."],
            ["7. Enlace", "Ejecutar git remote add y git remote -v.", "Mostrar las URL de lectura y escritura."],
            ["8. Publicación", "Ejecutar git push github master.", "Explicar el envío de los commits al repositorio remoto."],
            ["9. Verificación", "Abrir GitHub y mostrar el archivo y el historial.", "Confirmar que el archivo y el commit están publicados."],
            ["10. Cierre", "Volver a la terminal y despedirse.", "Resumir lo aprendido y agradecer."],
        ],
        anchos=[3.4, 6.8, 5.4],
        caption="Guion del video del ejercicio de Git.",
        size=7,
    )

    d.h2("9. Recomendaciones para la grabación")
    d.bullets([
        "Grabar en una sola toma y con una resolución mínima de 1280 x 720.",
        "Aumentar el tamaño de la letra de la terminal para facilitar la lectura.",
        "Explicar cada comando antes de ejecutarlo y leer el resultado en voz alta.",
        "Mantener el repositorio de GitHub abierto en otra pestaña para mostrar la verificación.",
        "No mostrar contraseñas, tokens ni datos personales diferentes a los solicitados.",
        "Nombrar el archivo del video con el código de la evidencia y el nombre del aprendiz.",
    ])

    d.conclusion([
        "El ejercicio permitió ejecutar el ciclo completo de Git: crear el repositorio "
        "local, preparar y confirmar los cambios, enlazar el repositorio remoto y publicar "
        "el historial en GitHub. La captura de la ejecución evidencia el funcionamiento de "
        "los comandos y la creación del archivo solicitado.",
        "El guion del video organiza la sustentación y asegura que se expliquen tanto los "
        "comandos locales como los remotos. Con esta evidencia queda demostrada la "
        "instalación, la configuración y el uso de Git en el proyecto.",
    ])

    d.bibliografia([
        "Chacon, S. y Straub, B. (2014). Pro Git (2.ª ed.). Apress. https://git-scm.com/book/es/v2",
        "Git. (2025). Git reference. https://git-scm.com/docs",
        "GitHub. (2026). GitHub Docs: About remote repositories. https://docs.github.com/es/get-started/getting-started-with-git/about-remote-repositories",
        "GitHub. (2026). GitHub Docs: Pushing commits to a remote repository. https://docs.github.com/es/get-started/using-git/pushing-commits-to-a-remote-repository",
    ])
    return d.guardar()


if __name__ == "__main__":
    cual = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cual in ("all", "ev04"):
        print(ev04())
    if cual in ("all", "ev05"):
        print(ev05())
