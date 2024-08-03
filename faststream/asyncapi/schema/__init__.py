"""AsyncAPI schema related functions."""

from faststream.asyncapi.schema.bindings import (
    ChannelBinding,
    OperationBinding,
    ServerBinding,
)
from faststream.asyncapi.schema.channels import Channel
from faststream.asyncapi.schema.info import (
    BaseInfo,
    Contact,
    ContactDict,
    InfoV2_6,
    License,
    LicenseDict,
)
from faststream.asyncapi.schema.main import (
    BaseSchema,
    Components,
    SchemaV2_6,
)
from faststream.asyncapi.schema.message import CorrelationId, Message
from faststream.asyncapi.schema.operations import Operation
from faststream.asyncapi.schema.security import SecuritySchemaComponent
from faststream.asyncapi.schema.servers import Server
from faststream.asyncapi.schema.utils import (
    ExternalDocs,
    ExternalDocsDict,
    Reference,
    Tag,
    TagDict,
)
from faststream.asyncapi.version import AsyncAPIVersion
from . import v3_0_0

__all__ = (
    # main
    "AsyncAPIVersion",
    "BaseSchema",
    "SchemaV2_6",
    "Components",
    # info
    "BaseInfo",
    "InfoV2_6",
    "Contact",
    "ContactDict",
    "License",
    "LicenseDict",
    # servers
    "Server",
    # channels
    "Channel",
    # utils
    "Tag",
    "TagDict",
    "ExternalDocs",
    "ExternalDocsDict",
    "Reference",
    # bindings
    "ServerBinding",
    "ChannelBinding",
    "OperationBinding",
    # messages
    "Message",
    "CorrelationId",
    # security
    "SecuritySchemaComponent",
    # subscription
    "Operation",
    "v3_0_0",
)
