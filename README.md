# dalias

Tool used for generating bash functions that act as docker aliases. These functions allow for the reference of relatively complex docker run commands using simple syntax.

Add the following to your shell init script in order to start updating functions on shell start.
```bash
dalias > ~/.dalias/aliases.sh
source ~/.dalias/aliases.sh
```

Take a look in the `configs` directory for an example of a config file for generating bash functions
