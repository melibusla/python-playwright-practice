# Python + Playwright Practice

Ejercicios de automatización de tests con **Python**, **Playwright** y **pytest**, hechos mientras sigo un curso de Udemy.

## Estructura

```
PythonBasics/        Ejercicios de Python (manejo de archivos, clases, etc.)
Playwright/          Tests de Playwright
  test_playwright.py        URL y título de la página (sync)
  test_playwright_async.py  Lo mismo con la API async
  test_pwlocators.py        Locators contra nopCommerce local
docker-compose.yml   Entorno local de nopCommerce
```

## Requisitos

- Python 3 y las dependencias de los tests:
  ```bash
  pip install pytest pytest-playwright pytest-asyncio
  playwright install chromium
  ```
- [Docker Desktop](https://www.docker.com/products/docker-desktop/), para el entorno de nopCommerce

## Por qué hay un nopCommerce local

El curso usa `https://demo.nopcommerce.com`, pero ese sitio está detrás de una verificación anti-bot de Cloudflare que bloquea los navegadores automatizados y rompe los tests.

En lugar de intentar evadir esa protección, levanto **mi propia instancia de nopCommerce con Docker**. Así los tests:

- no dependen de un sitio de terceros que puede cambiar o caerse,
- son estables y más rápidos,
- corren contra un entorno controlado, como se hace en un equipo de QA real.

## Levantar el entorno

Con Docker Desktop abierto, desde la raíz del proyecto:

```bash
docker compose up -d
```

La tienda queda en **http://localhost:8080**. La primera carga tarda unos segundos.

| Comando | Qué hace |
|---|---|
| `docker compose up -d` | Levanta nopCommerce y la base MySQL |
| `docker compose down` | Los apaga. Los datos quedan guardados |
| `docker compose down -v` | Los apaga **y borra la base**. Al volver a levantar aparece el instalador |

**Panel de administración:** http://localhost:8080/admin (usuario `admin@yourstore.com`, contraseña `admin123`).

> Son credenciales de un entorno local de práctica, no de algo real.

### Instalación desde cero

Solo hace falta si la base está vacía, por ejemplo después de `docker compose down -v`. Al entrar a http://localhost:8080 aparece el instalador:

1. Admin email `admin@yourstore.com` y password `admin123`
2. Tildar **Create sample data**
3. Database: **MySQL**, server `db`, database `nopcommerce`, usuario `root`, password `nopCommerce_db_password`
4. **Install**. Tarda unos minutos y al final la app se reinicia sola.

Para que el logo coincida con el del curso (`alt="nopCommerce demo store"`), renombrar la tienda:

```bash
docker compose exec db mysql -uroot -pnopCommerce_db_password nopcommerce -e "UPDATE Store SET Name='nopCommerce demo store';"
docker compose restart nopcommerce
```

## Correr los tests

```bash
pytest Playwright -v              # todos
pytest Playwright/test_pwlocators.py -v
pytest Playwright --headed        # viendo el navegador
```

`test_pwlocators.py` necesita el entorno de nopCommerce levantado. Los otros tests usan `demowebshop.tricentis.com`, que no tiene verificación anti-bot.

## Notas

- Cuando el curso usa `https://demo.nopcommerce.com`, acá se reemplaza por `http://localhost:8080`.
- La versión local puede ser más nueva que la del curso, así que algún texto o producto puede ser distinto. Si un locator falla, conviene revisar la página primero con `page.pause()` o `playwright codegen http://localhost:8080`.
