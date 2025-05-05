coq_with_imports() {
    tmpfile="/tmp/$(basename "$1")"
    imports="imports/$(basename "$1")"
    cat "$imports" "$1" > "$tmpfile" && coqc -w -all "$tmpfile" && rm "$tmpfile"
}

for f in *.v; do
    if [[ "$f" != "imports.v" ]]; then
        coq_with_imports "$f"
    fi
done