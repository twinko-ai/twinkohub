import os
import shlex
import shutil
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

# --- Get the project root directory (assuming tasks.py is in the root) ---
# PROJECT_ROOT = Path(__file__).parent
# DOTENV_PATH = PROJECT_ROOT / ".env"
# -------------------------------------------------------------------------

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS_FILE_BASE_ZH = "pelicanconf_zh.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_base_zh": SETTINGS_FILE_BASE_ZH,
    "settings_publish": "publishconf.py",
    "settings_publish_zh": "publishconf_zh.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Host and port for `serve`
    "host": "localhost",
    "port": 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of English site"""
    pelican_run("-s {settings_base}".format(**CONFIG))


@task
def build_zh(c):
    """Build local version of Chinese site"""
    pelican_run("-s {settings_base_zh}".format(**CONFIG))


@task
def build_all(c):
    """Build both English and Chinese sites"""
    build(c)
    build_zh(c)


@task
def rebuild(c):
    """Clean and rebuild English site"""
    clean(c)
    build(c)


@task
def rebuild_zh(c):
    """Clean and rebuild Chinese site"""
    clean(c)
    build_zh(c)


@task
def rebuild_all(c):
    """Clean and rebuild both English and Chinese sites"""
    clean(c)
    build_all(c)


@task
def regenerate(c):
    """Automatically regenerate English site upon file modification"""
    pelican_run("-r -s {settings_base}".format(**CONFIG))


@task
def regenerate_zh(c):
    """Automatically regenerate Chinese site upon file modification"""
    pelican_run("-r -s {settings_base_zh}".format(**CONFIG))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], CONFIG["port"]),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write("Serving at {host}:{port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """Build English site, then serve"""
    build(c)
    serve(c)


@task
def reserve_zh(c):
    """Build Chinese site, then serve"""
    build_zh(c)
    serve(c)


@task
def reserve_all(c):
    """Build both sites, then serve"""
    build_all(c)
    serve(c)


@task
def preview(c):
    """Build production version of English site"""
    pelican_run("-s {settings_publish}".format(**CONFIG))


@task
def preview_zh(c):
    """Build production version of Chinese site"""
    pelican_run("-s {settings_publish_zh}".format(**CONFIG))


@task
def preview_all(c):
    """Build production version of both sites"""
    preview(c)
    preview_zh(c)


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true"
        pelican_run(cmd.format(**CONFIG))

    cached_build()
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        f"{theme_path}/templates/**/*.html",
    ]

    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{}/**/*{}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = f"{theme_path}/static/**/*{extension}"
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def publish(c):
    """Publish English site to production"""
    pelican_run("-s {settings_publish}".format(**CONFIG))


@task
def publish_zh(c):
    """Publish Chinese site to production"""
    pelican_run("-s {settings_publish_zh}".format(**CONFIG))


@task
def publish_all(c):
    """Publish both sites to production"""
    publish(c)
    publish_zh(c)


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))
