#!/usr/bin/env python3

import subprocess
import sys
import os
from pathlib import Path

BANNER = r"""
 ______   ______     ______     ______   __  __     ______     ______    
/\  == \ /\  == \   /\  __ \   /\__  _\ /\ \/\ \   /\  == \   /\  ___\   
\ \  _-/ \ \  __<   \ \ \/\ \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \  __\   
 \ \_\    \ \_\ \_\  \ \_____\    \ \_\  \ \_____\  \ \_____\  \ \_____\ 
  \/_/     \/_/ /_/   \/_____/     \/_/   \/_____/   \/_____/   \/_____/
"""

HELP_TEXT = """
PROTUBE - Baixador do YouTube
==============================
Uso:
  run.py [OPCOES] <URL>

Opcoes:
  -h, --help            Exibe esta mensagem
  -o, --output DIR      Pasta de saida (padrao: musicas / videos)
  -q, --quality VALOR   Qualidade: 320, 192, 128 para audio | 1080, 720, 480 para video
  -v, --video           Baixa video ao inves de audio
  -p, --playlist        Baixa a playlist inteira

Exemplos:
  run.py https://youtube.com/watch?v=xxx
  run.py -q 192 https://youtube.com/watch?v=xxx
  run.py -v https://youtube.com/watch?v=xxx
  run.py -v -q 720 -o downloads https://youtube.com/watch?v=xxx
  run.py -p "https://youtube.com/playlist?list=xxx"
  run.py -p -v -q 720 "https://youtube.com/playlist?list=xxx"
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def parse_args(argv):
    args = {
        "url": None,
        "output": None,
        "quality": None,
        "video": False,
        "playlist": False,
        "help": False,
    }

    i = 0
    url_parts = []

    while i < len(argv):
        t = argv[i]

        if t in ("-h", "--help"):
            args["help"] = True
        elif t in ("-v", "--video"):
            args["video"] = True
        elif t in ("-p", "--playlist"):
            args["playlist"] = True
        elif t in ("-o", "--output"):
            i += 1
            if i < len(argv):
                args["output"] = argv[i]
        elif t in ("-q", "--quality"):
            i += 1
            if i < len(argv):
                args["quality"] = argv[i]
        elif t.startswith("http"):
            url_parts.append(t)
        elif url_parts:
            url_parts.append(t)

        i += 1

    if url_parts:
        args["url"] = "".join(url_parts)

    return args

def download(url, output, quality, video, playlist):
    playlist_flag = "--yes-playlist" if playlist else "--no-playlist"

    if video:
        pasta = Path(output or "videos")
        q = quality or "1080"
        fmt = f"bestvideo[height<={q}]+bestaudio/best[height<={q}]"
        if playlist:
            out_tpl = str(pasta / "%(playlist_index)s - %(uploader)s - %(title)s.%(ext)s")
        else:
            out_tpl = str(pasta / "%(uploader)s - %(title)s.%(ext)s")
        cmd = [
            "yt-dlp",
            "--format", fmt,
            "--merge-output-format", "mp4",
            "--output", out_tpl,
            "--embed-thumbnail",
            "--embed-metadata",
            playlist_flag,
            "--no-warnings",
            "--sleep-requests", "2",
            "--sleep-interval", "3",
            "--extractor-args", "youtube:player_client=ios,android,web",
            url,
        ]
        mode = "video"
        detail = f"mp4 {q}p"
    else:
        pasta = Path(output or "musicas")
        q = quality or "320"
        if playlist:
            out_tpl = str(pasta / "%(playlist_index)s - %(uploader)s - %(title)s.%(ext)s")
        else:
            out_tpl = str(pasta / "%(uploader)s - %(title)s.%(ext)s")
        cmd = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", f"{q}k",
            "--format", "bestaudio/best",
            "--output", out_tpl,
            "--embed-thumbnail",
            "--embed-metadata",
            playlist_flag,
            "--no-warnings",
            "--sleep-requests", "2",
            "--sleep-interval", "3",
            "--extractor-args", "youtube:player_client=ios,android,web",
            url,
        ]
        mode = "audio"
        detail = f"mp3 {q}kbps"

    pasta.mkdir(exist_ok=True)

    print(f"[*] Target   : {url}")
    print(f"[*] Output   : {pasta.resolve()}")
    print(f"[*] Mode     : {mode} ({detail})")
    print(f"[*] Playlist : {'yes' if playlist else 'no'}")
    print()

    try:
        result = subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted.")
        while True:
            try:
                resp = input("[?] Do you want to close the program? (S/N): ").strip().lower()
            except KeyboardInterrupt:
                resp = "s"
            if resp in ("s", "sim", "y", "yes"):
                print("[-] Closed by the user.")
                sys.exit(0)
            elif resp in ("n", "nao", "no"):
                print("[*] Retomando...")
                download(url, output, quality, video, playlist)
                return
            else:
                print("[!] Digite S para sair ou N para continuar.")
        return

    if result.returncode == 0:
        print("\n[+] Download complete.")
    else:
        print("\n[-] Download failed.")

def main():
    clear()
    print(BANNER)

    args = parse_args(sys.argv[1:])

    if args["help"] or not args["url"]:
        print(HELP_TEXT)
        sys.exit(0)

    download(args["url"], args["output"], args["quality"], args["video"], args["playlist"])

if __name__ == "__main__":
    main()