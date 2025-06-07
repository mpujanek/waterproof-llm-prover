coq_with_imports() {
    tmpfile="/tmp/$(basename "$1")"
    imports="imports/$(basename "$1")"
    cat libimports.v "$imports" "$1" > "$tmpfile" && coqc -w -all "$tmpfile" && rm "$tmpfile"
}

for f in *.v; do
    if [[ "$f" != "libimports.v" && "$f" != "importsall.v" ]]; then
        coq_with_imports "$f"
    fi
done