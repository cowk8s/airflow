DOCS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly DOCS_DIR

(cd "${DOCS_DIR}"/_build || exit;
        python3 -m http.server 8000
)