"""FastAPI configuration settings model."""

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field


class Cors(BaseModel):
    """Cors model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    allow_origins: List[str] = Field(default_factory=lambda: ["*"])
    allow_methods: List[str] = Field(default_factory=lambda: ["*"])
    allow_headers: List[str] = Field(default_factory=lambda: ["*"])


class Servers(BaseModel):
    """Servers model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    url: str = "http://localhost:8000"
    description: str = "Local DataMart development server"


class FastAPISettings(BaseModel):
    """Settings model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    version: str = "1"
    title: str = "DataMart Market API"
    description: str = "This is the DataMart Market API."
    terms_of_service: str = "http://example.com/terms/"
    contact_name: str = "DataMart Team"
    contact_url: str = ""
    contact_email: str = ""
    license_name: str = "MIT"
    license_url: str = (
        ""
    )
    servers: List[Servers] = Field(default_factory=lambda: [Servers()])
    cors: Cors = Field(default_factory=Cors)
    custom_headers: Optional[Dict[str, str]] = Field(
        default=None, description="Custom headers and respective default value."
    )

    @computed_field  # type: ignore[misc]
    @property
    def prefix(self) -> str:
        """Return the API prefix."""
        return f"/api/v{self.version}"

    def __repr__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
