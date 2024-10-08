# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent

sys.path.append(str(root_dir))

from rapid_layout_recover import RapidLayoutRecover

layout_recover = RapidLayoutRecover()

test_file_dir = cur_dir / "test_files"


def test_direct_single_column():
    pdf_path = test_file_dir / "direct_extract" / "single_column.pdf"

    result = layout_recover(pdf_path)

    assert len(result) == 1
    assert len(result[0][2]) == 9
    assert result[0][2][0][0][:5] == "星期天早晨"
