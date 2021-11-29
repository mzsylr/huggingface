import glob
import os
from pathlib import Path
from typing import Dict, Optional, Union

from .constants import HUGGINGFACE_HUB_CACHE
from .file_download import cached_download, hf_hub_url
from .hf_api import HfApi, HfFolder


REPO_ID_SEPARATOR = "__"
# ^ make sure this substring is not allowed in repo_ids on hf.co


def snapshot_download(
    repo_id: str,
    revision: Optional[str] = None,
    cache_dir: Union[str, Path, None] = None,
    library_name: Optional[str] = None,
    library_version: Optional[str] = None,
    user_agent: Union[Dict, str, None] = None,
    proxies=None,
    etag_timeout=10,
    resume_download=False,
    use_auth_token: Union[bool, str, None] = None,
    local_files_only=False,
) -> str:
    """
    Downloads a whole snapshot of a repo's files at the specified revision.
    This is useful when you want all files from a repo, because you don't know
    which ones you will need a priori.
    All files are nested inside a folder in order to keep their actual filename
    relative to that folder.

    An alternative would be to just clone a repo but this would require that
    the user always has git and git-lfs installed, and properly configured.

    Note: at some point maybe this format of storage should actually replace
    the flat storage structure we've used so far (initially from allennlp
    if I remember correctly).

    Return:
        Local folder path (string) of repo snapshot
    """
    if cache_dir is None:
        cache_dir = HUGGINGFACE_HUB_CACHE
    if isinstance(cache_dir, Path):
        cache_dir = str(cache_dir)

    if isinstance(use_auth_token, str):
        token = use_auth_token
    elif use_auth_token:
        token = HfFolder.get_token()
        if token is None:
            raise EnvironmentError(
                "You specified use_auth_token=True, but a Hugging Face token was not found."
            )
    else:
        token = None

    local_repo_id_prefix = repo_id.replace("/", REPO_ID_SEPARATOR)

    # retrieve cached repo
    if local_files_only:
        # find last modified folder
        storage_folder = max(
            glob.glob(os.path.join(cache_dir, local_repo_id_prefix + ".*")),
            key=os.path.getmtime,
        )

        repo_id_sha = storage_folder.split(".")[-1]
        model_files = os.listdir(storage_folder)
    else:
        _api = HfApi()
        model_info = _api.model_info(repo_id=repo_id, revision=revision, token=token)
        storage_folder = os.path.join(
            cache_dir, local_repo_id_prefix + "." + model_info.sha
        )

        repo_id_sha = model_info.sha
        model_files = [f.rfilename for f in model_info.siblings]

    for model_file in model_files:
        url = hf_hub_url(repo_id, filename=model_file, revision=repo_id_sha)
        relative_filepath = os.path.join(*model_file.split("/"))

        # Create potential nested dir
        nested_dirname = os.path.dirname(
            os.path.join(storage_folder, relative_filepath)
        )
        os.makedirs(nested_dirname, exist_ok=True)

        path = cached_download(
            url,
            cache_dir=storage_folder,
            force_filename=relative_filepath,
            library_name=library_name,
            library_version=library_version,
            user_agent=user_agent,
            proxies=proxies,
            etag_timeout=etag_timeout,
            resume_download=resume_download,
            use_auth_token=use_auth_token,
            local_files_only=local_files_only,
        )

        if os.path.exists(path + ".lock"):
            os.remove(path + ".lock")

    return storage_folder
