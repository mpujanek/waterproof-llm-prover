coq_with_imports() {
    cat imports.v "$1" > /tmp/tmp_coq.v && coqc -w -all /tmp/tmp_coq.v && rm /tmp/tmp_coq.v
}

for f in *.v; do
    if [[ "$f" != "imports.v" ]]; then
        coq_with_imports "$f"
    fi
done