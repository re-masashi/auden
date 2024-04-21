import click
import uvicorn

import subprocess
import os

@click.group()
@click.option('--debug', default=True, help='Debug mode. True/False')
@click.pass_context
def main(ctx, debug):

    processes = set()

    if debug:
        processes.add(subprocess.Popen("cd assets; pnpm run dev", shell=True))
    else:
        processes.add(subprocess.Popen("cd assets; pnpm run build", shell=True))
    processes.add(subprocess.Popen("cd assets; pnpm run esbuild", shell=True))
    processes.add(subprocess.Popen("cp -r assets/images .dist/", shell=True))
    processes.add(subprocess.Popen("cp -r assets/html .dist/", shell=True))
    processes.difference_update([
        p for p in processes if p.poll() is not None])

    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug

@main.command()
def build_assets():
    print("Building assets...")

@main.command("start")
@click.option('--port', default=8080, help='Port')
@click.option('--host', default="0.0.0.0", help='Host')
@click.pass_context
def start_server(ctx, port, host):
    print(f"Starting server on {host}:{port}... with `debug={ctx.obj['DEBUG']}`")
    config = uvicorn.Config(
        "auden:app", 
        port=port, 
        reload=True,
        reload_includes=['templates', '.dist/*', 'auden']
    )
    server = uvicorn.Server(config)
    server.run()

if __name__ == '__main__':
    main()