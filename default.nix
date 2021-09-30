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
     pre-commit install
      '';
  }
