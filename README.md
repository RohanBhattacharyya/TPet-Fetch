# TPet Fetch

TPet Fetch is a terminal-based program inspired by Nerdfetch that displays a terminal pet alongside some basic system information. This tool is designed to add a bit of fun to your terminal while providing useful details about your system.

## Features

- Display a terminal pet.
- Show system information such as:
  - Operating System
  - CPU model (Planned)
  - Memory usage (Planned)
  - Disk usage (Planned)
  - Uptime

## Installation
- Go to the [releases page](https://github.com/RohanBhattacharyya/TPet-Fetch/releases/latest), and download tpet.zip.
- Unzip this file and cd into the directory.
- Run the commands below
```bash
mv tpet/* ~/.local/bin/
tpet -display
```
## Issues
- If you run tpet -display and it can't find it
  - Add ~/.local/bin/ to your path  
### Prerequisites

- A Unix-like operating system (Linux, macOS, etc.)
- A [Nerd Font](https://www.nerdfonts.com/) installed to your terminal
- Bash or any compatible shell
- Python 3.10+ (Recommended)
