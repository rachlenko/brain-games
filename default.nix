let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    name = "simpleEnv";
    buildInputs = with pkgs; [
    # basic python dependencies
      python39
      direnv

    # dirty virtualenv dependencies
      python39Packages.pip
      python39Packages.virtualenv
    ];
   shellHook = ''
     echo "running python here "
     python -m virtualenv venv
     source venv/bin/activate
     pip install -r requirements.txt
     curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
     source $HOME/.poetry/env
     pre-commit install
      '';
  }
