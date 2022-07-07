from .code_utils import (
    DOCS_DIR,
)

class AirflowDocsBuilder:
    """Documentation builder for Airflow."""

    def __init__(self, package_name: str, for_production: bool):
        self.package_name = package_name
        self.for_production = for_production

    @property
    def _doctree_dir(self) -> str:
        return f"{DOCS_DIR}/_doctrees/docs/{self.package_name}"

def get_available_providers_packages():
    """Get list of all available provider packages to build."""
    return [provider['package-name'] for provider in ]