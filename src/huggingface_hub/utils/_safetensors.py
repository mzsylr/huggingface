from dataclasses import dataclass
from typing import Dict, List, Literal, Optional, Tuple


FILENAME_T = str
TENSOR_NAME_T = str
DTYPE_T = Literal["F64", "F32", "F16", "BF16", "I64", "I32", "I16", "I8", "U8", "BOOL"]


class SafetensorsParsingError(Exception):
    """Raised when failing to parse a safetensors file metadata.

    This can be the case if the file is not a safetensors file or does not respect the specification.
    """


class NotASafetensorsRepoError(Exception):
    """Raised when a repo is not a Safetensors repo i.e. doesn't have either a `model.safetensors` or a
    `model.safetensors.index.json` file.
    """


@dataclass
class TensorInfo:
    """Information about a tensor.

    For more details regarding the safetensors format, check out https://huggingface.co/docs/safetensors/index#format.

    Attributes:
        dtype (`str`):
            The data type of the tensor ("F64", "F32", "F16", "BF16", "I64", "I32", "I16", "I8", "U8", "BOOL").
        shape (`List[int]`):
            The shape of the tensor.
        data_offsets (`Tuple[int, int]`):
            The offsets of the data in the file as a tuple `[BEGIN, END]`.
    """

    dtype: DTYPE_T
    shape: List[int]
    data_offsets: Tuple[int, int]


@dataclass
class SafetensorsFileMetadata:
    """Metadata for a Safetensors file hosted on the Hub.

    This class is returned by [`parse_safetensors_file_metadata`].

    For more details regarding the safetensors format, check out https://huggingface.co/docs/safetensors/index#format.

    Attributes:
        metadata (`Dict`):
            The metadata contained in the file.
        tensors (`Dict[str, TensorInfo]`):
            A map of all tensors. Keys are tensor names and values are information about the corresponding tensor, as a
            [`TensorInfo`] object.
    """

    metadata: Dict
    tensors: Dict[TENSOR_NAME_T, TensorInfo]


@dataclass
class SafetensorsRepoMetadata:
    """Metadata for a Safetensors repo.

    A repo is considered to be a Safetensors repo if it contains either a 'model.safetensors' weight file (non-shared
    model) or a 'model.safetensors.index.json' index file (sharded model) at its root.

    This class is returned by [`get_safetensors_metadata`].

    For more details regarding the safetensors format, check out https://huggingface.co/docs/safetensors/index#format.

    Attributes:
        metadata (`Dict`, *optional*):
            The metadata contained in the 'model.safetensors.index.json' file, if it exists. Only populated for sharded
            models.
        sharded (`bool`):
            Whether the repo contains a sharded model or not.
        weight_map (`Dict[str, str]`):
            A map of all weights. Keys are tensor names and values are filenames of the files containing the tensors.
        files_metadata (`Dict[str, SafetensorsFileMetadata]`):
            A map of all files metadata. Keys are filenames and values are the metadata of the corresponding file, as
            a [`SafetensorsFileMetadata`] object.
    """

    metadata: Optional[Dict]
    sharded: bool
    weight_map: Dict[TENSOR_NAME_T, FILENAME_T]  # tensor name -> filename
    files_metadata: Dict[FILENAME_T, SafetensorsFileMetadata]  # filename -> metadata
