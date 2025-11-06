# Despliegue en Vercel (Python serverless)

Este repositorio contiene una función serverless mínima para desplegar en Vercel.

Archivos creados:
- `api/index.py` — función serverless mínima.
- `requirements.txt` — dependencias.
- `vercel.json` — configuración para Vercel.

Pasos para subir a GitHub (PowerShell):

```powershell
cd C:\Users\USERCAD\Documents\dw_evaluacion\mycrudproject
# Inicializar git (si aún no está inicializado)
git init
git add .
git commit -m "Primer commit para Vercel"
# Cambia 'tu-usuario' y 'mi-proyecto-vercel' por tu usuario y nombre de repo
git branch -M main
git remote add origin https://github.com/tu-usuario/mi-proyecto-vercel.git
git push -u origin main
```

Pasos para desplegar en Vercel:
1. Ve a https://vercel.com e inicia sesión.
2. Haz clic en "Add New Project" y selecciona tu repositorio de GitHub.
3. En la configuración del proyecto en Vercel:
   - Framework Preset: Other
   - Build Command: (vacío)
   - Output Directory: (vacío)
4. Despliega. Vercel usará `vercel.json` para enrutar todas las peticiones a `api/index.py`.

Notas y alternativas:
- Si quieres desplegar tu aplicación Django completa en Vercel, la integración es más compleja (ASGI/WSGI adaptadores, dependencias, manejo de archivos estáticos y base de datos). Prefiero ayudarte a preparar eso si quieres; dime si quieres intentar desplegar el Django entero o solo una función mínima.
- Puedes cambiar el runtime en `vercel.json` a `python3.10` o `python3.11` si lo prefieres.
