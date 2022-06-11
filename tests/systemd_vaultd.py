#!/usr/bin/env python3

import os
import pytest
from pathlib import Path
from typing import Optional
from command import run

BIN: Optional[Path] = None


@pytest.fixture
def systemd_vaultd(project_root: Path) -> Path:
    global BIN
    if BIN:
        return BIN
    bin = os.environ.get("SYSTEMD_VAULTD_BIN")
    if bin:
        BIN = Path(bin)
        return BIN
    run(["go", "build", str(project_root)])
    BIN = project_root / "systemd-vaultd"
    return BIN