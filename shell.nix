with import <nixpkgs> {};

stdenv.mkDerivation rec {
	name = "flask-firehose";
	env = buildEnv {
		name = name;
		paths = buildInputs;
	};
	buildInputs = [
		fish
		nghttp2
		(python3.withPackages(ps: with ps; [
			flask
			pytest
			wheel
			twine
		]))
	];
	shellHook = "export SOURCE_DATE_EPOCH=$(date +%s); exec fish";
}
