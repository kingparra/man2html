#!/usr/bin/env bash
enum_manpages() (
	man -K ''
)


generate_html() (
	while read -r line; do
		zcat "$line" | groff -mandoc -Thtml > "$(basename "$line")".html
	done
)


inject_css() (
	for file in "$@"; do
		patch "$file" ./style.diff
	done
)

main() (
	enum_manpages > list_of_manpages.txt
	generate_html < list_of_manpages.txt
	inject_css ./*.html
)


if [[ "${BASH_SOURCE[0]}" = "$0" ]]; then
	main
fi
