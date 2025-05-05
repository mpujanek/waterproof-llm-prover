coq_with_imports() {
    tmpfile="/tmp/$(basename "$1")"
    imports="imports/$(basename "$1")"
    cat "$imports" "$1" > "$tmpfile" && coqc -w -all "$tmpfile" && rm "$tmpfile"
}

if [[ -z "$1" ]]; then
    echo "Usage: $0 file.v"
    exit 1
fi

coq_with_imports "$1"