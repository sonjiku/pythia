{
    description = "Python development environment template";
    inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    inputs.systems.url = "github:nix-systems/default";
    inputs.flake-utils = {
        url = "github:numtide/flake-utils";
        inputs.systems.follows = "systems";
    };

    outputs = { nixpkgs, flake-utils, ... }:
        flake-utils.lib.eachDefaultSystem (
            system:
            let
                pkgs = nixpkgs.legacyPackages.${system};
            in
            {
                devShells.default = pkgs.mkShell {
                    packages = [
                        pkgs.uv
                        pkgs.bashInteractive
                    ];
                    shellHook = ''
                        if [ ! -f .python-version ]; then
                            echo "Initializing dir with uv"
                            uv init
                        fi
                        if [ -f .venv ]; then
                            echo "Found .venv."
                        else
                            uv sync --frozen
                        fi
                    '';

                };
                # source .venv/bin/activate
            }
        );
}
