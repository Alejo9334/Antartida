# ❄ ANTÁRTIDA — Realidad Aumentada

Aplicación independiente de **ANTÁRTIDA Heladería y Café** (Colombia), basada en el motor de realidad aumentada desarrollado en `Code-fuente`.

## Accesos (después del primer despliegue)

- **Visor del cliente:** https://alejo9334.github.io/Antartida/
- **Editor ANTÁRTIDA Studio:** https://alejo9334.github.io/Antartida/editor.html
- **Optimizador:** https://alejo9334.github.io/Antartida/optimizar.html

## Identidad visual

Azul profundo / hielo / blanco, acentos turquesa. El panel administrativo rediseñado presenta una experiencia polar con paneles de vidrio oscuro, botones de hielo y espacios de trabajo diferenciados.

## Primera instalación

1. En **Settings → Pages**, elegir **Source: GitHub Actions**.
2. En **Actions → Instalar ANTÁRTIDA AR y publicar**, pulsar **Run workflow → Run workflow** en la rama `main`.
3. La acción copiará todos los archivos del visor, editor, catálogo, imágenes PNG/WebP, referencias y `targets.mind` desde `Code-fuente/desarrollo/multicuadros-ar-v2`.
4. Aplicará el diseño propio mediante `scripts/personalizar_antartida.py` y guardará **una copia completa dentro de este repositorio**. La publicación usa los archivos de esta copia y deja de depender del proyecto original.
5. Verificar la página publicada, la cámara y el reconocimiento de las imágenes en un celular.

La acción no sobrescribe una copia ya instalada. Puedes editar los archivos aquí sin modificar `Code-fuente` ni `Visor-AR`.

## Importante

La primera copia conserva los cuadros de demostración (Minecraft y Carnet). Sustitúyelos por referencias y capas propias de ANTÁRTIDA antes de compartir el visor con clientes.

El editor mantiene guardado local en el navegador, exportación JSON, anclaje por PNG, giros XYZ, sombras, trayectorias, parallax, historial y presets. **La URL del editor no tiene autenticación propia**: para uso estrictamente interno, habrá que implementar acceso autenticado antes de distribuirla. Publicar diseños en el catálogo requiere el flujo de GitHub autorizado.

No incluir contraseñas, tokens privados ni datos de clientes en el repositorio.
