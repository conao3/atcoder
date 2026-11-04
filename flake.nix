{
  description = "atcoder";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-darwin"
      ];

      imports = [
        inputs.treefmt-nix.flakeModule
      ];

      perSystem =
        {
          pkgs,
          ...
        }:
        let
          python = pkgs.python315;
        in
        {
          devShells.default = pkgs.mkShell {
            packages = [
              python
              pkgs.uv
            ];
          };

          treefmt = {
            projectRootFile = "flake.nix";
            programs.nixfmt.enable = true;
            programs.ruff-check.enable = true;
            programs.ruff-format.enable = true;
            settings.excludes = [ "scripts/template/main.py" ];
          };
        };
    };
}
