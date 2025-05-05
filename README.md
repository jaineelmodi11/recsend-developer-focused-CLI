██████╗ ███████╗███████╗███████╗██████╗ ███████╗███╗   ██╗███████╗  
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝████╗  ██║██╔════╝  
██████╔╝█████╗  ███████╗█████╗  ██████╔╝█████╗  ██╔██╗ ██║█████╗    
██╔═══╝ ██╔══╝  ╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║██╔══╝    
██║     ███████╗███████║███████╗██║  ██║███████╗██║ ╚████║███████╗  
╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝╚══════╝  
------------------------------------------------------------------  
A developer-focused CLI for testing your movie-recommendation backend via JSON/YAML files

## Features

- **JSON/YAML request files** to define any HTTP call (method, URL, headers, body, etc.)  
- **Convenience subcommands** for your core flows:
  - `swipe`      — simulate Tinder-style like/dislike  
  - `recommend`  — fetch model recommendations  
  - `push-user`  — create or update test users in Firebase  
  - `log`        — inspect a user’s interaction history  
- **Colorized output** for easy reading  
- **I/O redirection**: body → stdout, headers/status → stderr  
- **Installable** via `pip`, cross-platform (macOS, Linux, Windows)  
- **Fully tested** with `pytest` and HTTP mocks  

## Installation

> **Requires** Python 3.8+

```bash
pip install recsend
