# CIFRADOS 2025

## 📜 Descripción
CIFRADOS 2025 es un repositorio diseñado para la gestión de material del curso Cifrados del año 2025. En este repositorio se encontraran los ejercicios y ejemplos de la clase, asi como la documentacion del contenido de la clase.
 * https://locano-uvg.github.io/cifrados-25/

## ✨ Características
- Documentacion del contenido de la clase
- Ejercicios
- Ejemplos
- Proyectos

## 🚀 Uso de Scripts (Ejercicios)

Este repositorio contiene scripts para la generación de llaves y cifrado ASCII.

### 1. Generador de Llaves (`key_generator.py`)
Genera una llave aleatoria de caracteres ASCII imprimibles.
```bash
python3 key_generator.py <length> [--output <file>]
# Ejemplo:
python3 key_generator.py 16
```

### 2. Cifrado con Llave Fija (`cipher_fixed_key.py`)
Cifra o descifra un mensaje usando una llave de tamaño fijo (tipo Vigenère/Modular).
```bash
# Cifrar
python3 cipher_fixed_key.py encrypt --message "Hola Mundo" --key "clave"

# Descifrar
python3 cipher_fixed_key.py decrypt --message "MensajeCifrado" --key "clave"
```

### 3. Cifrado con Llave Dinámica (`cipher_dynamic_key.py`)
Cifra usando una llave del mismo tamaño que el mensaje (Generated on-the-fly, One-Time Pad style).
```bash
# Cifrar (Genera llave automáticamente)
python3 cipher_dynamic_key.py encrypt --message "Mensaje Secreto" --key-out llave.txt

# Descifrar (Requiere la llave generada)
python3 cipher_dynamic_key.py decrypt --message "Ciphertext" --key "LlaveUsada..."
```

## 📜 Dependencias Principales
Las principales dependencias del proyecto incluyen:
* [![Node][Node.js]][Node-url]
* [![Reveal][Reveal-js]][Reveal-url]
* [![Python][Python]][Python-url]

Para más detalles, puedes consultar el archivo `package.json`.
(Ir al inicio)

## 📜 Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:
1. Realiza un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

### Developer's
* [![Linkedin][Linkedin]][Linkedin-lud]
* [![GitHub][GitHub]][GitHub-lud]
(Ir al inicio)

## 📜 Contacto
Si tienes preguntas o comentarios, puedes contactarnos a traves de nuestras redes sociales:
* [![Instagram][Instagram]][Instagram-url]
* [![Website][Website]][Website-url]
(Ir al inicio)

<!-- MARKDOWN LINKS & IMAGES -->
[Redux]: https://img.shields.io/badge/Redux-764ABC?style=flat&logo=redux&logoColor=white
[Redux-url]: https://redux.js.org/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[MongoDB]: https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.npmjs.com/package/mongodb
[Node.js]: https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org/en/
[Reveal-js]: https://img.shields.io/badge/Reveal.js-339933?style=flat&logo=reveal.js&logoColor=white
[Reveal-url]: https://revealjs.com/
[Python]: https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Instagram]: https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white
[Instagram-url]: https://www.instagram.com/ludwing238/
[Website]: https://img.shields.io/website?url=https://lc2tech.com/
[Website-url]: https://lc2tech.com/
[AntDesign]: https://img.shields.io/badge/-Ant%20Design-333333?style=flat&logo=ant-design&logoColor=0170FE
[AntDesign-url]: https://ant.design/
[Chartjs]: https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white
[Chartjs-url]: https://github.com/reactchartjs/react-chartjs-2
[Linkedin-lud]: https://www.linkedin.com/in/ludwing-cano238
[Linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Github-lud]: https://github.com/locano
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
